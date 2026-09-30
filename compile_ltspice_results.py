#!/usr/bin/env python3
"""
Compile LTSpice .log files into one results report.

Walks a folder tree (default: current directory), parses every *.log that
LTSpice wrote, and produces:

  RESULTS.md    - one section per simulation: status, step parameters and
                  every .meas result in a table, in folder order
  results.json  - the same data, machine-readable (for scripts or Claude Code)

Handles:
  * UTF-16 and UTF-8 logs (LTSpice on Windows often writes UTF-16LE)
  * stepped runs     ("Measurement: name" tables, one row per .step)
  * non-stepped runs ("name: V(x)=1.23 at 4.56" single-line results)
  * failed runs      (singular matrix, timestep too small, etc.) - flagged,
                     because LTSpice discards ALL measurements if any step fails

Usage:
  python compile_ltspice_results.py                 # scan current folder
  python compile_ltspice_results.py path/to/tests   # scan another folder
  python compile_ltspice_results.py -o report.md    # choose output name

Standard library only.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ERROR_PATTERNS = [
    r"singular matrix",
    r"timestep too small",
    r"fail'?ed",
    r"^error",
    r"convergence failed",
    r"analysis aborted",
    r"unknown (parameter|subcircuit|model)",
]

SI = [(1e9, "G"), (1e6, "M"), (1e3, "k"), (1, ""), (1e-3, "m"),
      (1e-6, "u"), (1e-9, "n"), (1e-12, "p"), (1e-15, "f")]


# ---------------------------------------------------------------- reading --

def read_log(path: Path) -> str:
    """Decode a log regardless of whether LTSpice wrote UTF-16 or UTF-8."""
    raw = path.read_bytes()
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        text = raw.decode("utf-16")
    elif len(raw) > 1 and raw[1:2] == b"\x00":       # UTF-16LE without BOM
        text = raw.decode("utf-16-le", errors="replace")
    else:
        text = raw.decode("utf-8", errors="replace")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def to_number(tok: str):
    try:
        return float(tok)
    except ValueError:
        return tok


def eng(x) -> str:
    """Format a number with an SI prefix, 4 significant figures."""
    if not isinstance(x, float):
        return str(x)
    if x == 0:
        return "0"
    ax = abs(x)
    for scale, prefix in SI:
        if ax >= scale * 0.9995:
            return f"{x / scale:.4g}{prefix}"
    return f"{x:.3g}"


# ---------------------------------------------------------------- parsing --

def parse_log(path: Path) -> dict:
    text = read_log(path)
    lines = text.split("\n")
    out = {
        "file": str(path),
        "circuit": None,
        "start_time": None,
        "elapsed_s": None,
        "options": None,
        "steps": [],          # list of {param: value}
        "measurements": {},   # name -> {"expr": str, "values": [..], "extra": [..]}
        "errors": [],
    }

    for ln in lines:
        s = ln.strip()
        if s.startswith("Circuit:"):
            out["circuit"] = s.split(":", 1)[1].strip()
        elif s.startswith("Start Time:"):
            out["start_time"] = s.split(":", 1)[1].strip()
        elif s.startswith("Total elapsed time:"):
            m = re.search(r"([\d.]+)", s)
            out["elapsed_s"] = float(m.group(1)) if m else None
        elif s.startswith("Options:"):
            out["options"] = s.split(":", 1)[1].strip()
        elif s.startswith(".step"):
            params = dict(re.findall(r"(\w+)=(\S+)", s))
            out["steps"].append({k: to_number(v) for k, v in params.items()})
        elif any(re.search(p, s, re.I) for p in ERROR_PATTERNS):
            out["errors"].append(s)

    # Stepped measurement tables:
    #   Measurement: name
    #     step  <expr> [FROM TO | at]
    #        1  value  ...
    i = 0
    while i < len(lines):
        m = re.match(r"\s*Measurement:\s*(\S+)", lines[i])
        if not m:
            i += 1
            continue
        name = m.group(1)
        header = lines[i + 1].split("\t") if i + 1 < len(lines) else []
        expr = header[1].strip() if len(header) > 1 else ""
        values, extra = [], []
        j = i + 2
        while j < len(lines):
            row = lines[j].strip()
            if not row or row.startswith("Measurement:"):
                break
            cells = re.split(r"\t+|\s{2,}", row)
            if cells and cells[0].isdigit():
                values.append(to_number(cells[1]) if len(cells) > 1 else None)
                extra.append([to_number(c) for c in cells[2:]])
            j += 1
        out["measurements"][name] = {"expr": expr, "values": values, "extra": extra}
        i = j

    # Non-stepped single-line results. LTSpice prints three shapes:
    #   FIND/MAX/AVG ...   name: AVG(V(x))=1.23 FROM 0.005 TO 0.045
    #   FIND ... AT/WHEN   name: V(x) =1.23 at 4.56          (lowercase "at")
    #   WHEN only          name: V(x)=1.65  AT 0.001025      (uppercase "AT";
    #                      the number after "=" is the threshold, the result
    #                      is the time after "AT")
    for ln in lines:
        m = re.match(r"^(\w+):\s*(.+?)\s*=\s*(\S+)(.*)$", ln.strip())
        if not m or m.group(1) in ("Circuit", "Start", "Options", "Total", "Files"):
            continue
        name, expr, first, tail = m.groups()
        if name in out["measurements"]:
            continue
        when = re.match(r"\s+AT\s+(\S+)", tail)
        if when:
            value, expr = to_number(when.group(1)), f"WHEN {expr.strip()}={first}"
            extra = []
        else:
            value, extra = to_number(first), ([tail.strip()] if tail.strip() else [])
        if isinstance(value, float):
            out["measurements"][name] = {"expr": expr.strip(), "values": [value], "extra": [extra]}

    n_meas = len(out["measurements"])
    if out["errors"]:
        out["status"] = "FAILED"
    elif n_meas == 0:
        out["status"] = "NO MEASUREMENTS"
    else:
        out["status"] = "OK"
    return out


# ---------------------------------------------------------------- output --

def natural_key(p: Path):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", str(p))]


def section_md(r: dict, root: Path) -> str:
    rel = Path(r["file"]).relative_to(root)
    title = Path(r["file"]).stem
    badge = {"OK": "✅ OK", "FAILED": "❌ FAILED", "NO MEASUREMENTS": "⚠️ NO MEASUREMENTS"}[r["status"]]
    md = [f"### {title}", "",
          f"`{rel}` · {badge} · run {r['start_time'] or '?'}"
          + (f" · {r['elapsed_s']:.1f} s" if r["elapsed_s"] is not None else "")
          + (f" · options: {r['options']}" if r["options"] else ""), ""]

    if r["errors"]:
        md += ["**Errors reported by LTSpice** (all measurements are discarded when any step fails):", ""]
        md += [f"- `{e}`" for e in dict.fromkeys(r["errors"])]
        md.append("")
        if r["steps"]:
            md.append(f"Steps started before the failure: {len(r['steps'])}.")
            md.append("")
        return "\n".join(md)

    meas = r["measurements"]
    if not meas:
        md += ["No `.meas` results found in this log.", ""]
        return "\n".join(md)

    names = list(meas)
    n_rows = max(len(m["values"]) for m in meas.values())
    params = list(r["steps"][0]) if r["steps"] else []

    head = ["step"] + params + [f"{n}<br><sub>{meas[n]['expr']}</sub>" for n in names]
    md.append("| " + " | ".join(head) + " |")
    md.append("|" + "---|" * len(head))
    for k in range(n_rows):
        row = [str(k + 1)]
        step = r["steps"][k] if k < len(r["steps"]) else {}
        row += [eng(step.get(p, "")) for p in params]
        for n in names:
            v = meas[n]["values"]
            row.append(eng(v[k]) if k < len(v) and v[k] is not None else "—")
        md.append("| " + " | ".join(row) + " |")
    md.append("")
    return "\n".join(md)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root", nargs="?", default=".", help="folder to scan (default: current)")
    ap.add_argument("-o", "--output", default="RESULTS.md", help="markdown report path")
    ap.add_argument("--json", default="results.json", help="JSON output path")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    logs = sorted(root.rglob("*.log"), key=natural_key)
    if not logs:
        sys.exit(f"No .log files found under {root}")

    results = [parse_log(p) for p in logs]

    # Group by top-level folder (e.g. 1_wheel_supply, 2_spi_lines, ...)
    groups = {}
    for r in results:
        rel = Path(r["file"]).relative_to(root)
        groups.setdefault(rel.parts[0] if len(rel.parts) > 1 else ".", []).append(r)

    ok = sum(r["status"] == "OK" for r in results)
    bad = [r for r in results if r["status"] != "OK"]
    md = ["# LTSpice Simulation Results", "",
          f"Compiled from {len(results)} log file(s) under `{root.name}`. "
          f"{ok} OK, {len(bad)} failed or empty.", ""]
    if bad:
        md += ["**Needs attention:**", ""]
        md += [f"- `{Path(r['file']).relative_to(root)}` — {r['status']}" for r in bad]
        md.append("")
    md += ["Values use SI prefixes (m = milli, u = micro, n = nano, k = kilo, M = mega). "
           "Step columns are the `.step` parameters in LTSpice's run order.", ""]

    for g, rs in groups.items():
        md += [f"## {g}", ""]
        md += [section_md(r, root) for r in rs]

    Path(args.output).write_text("\n".join(md), encoding="utf-8")
    Path(args.json).write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Parsed {len(results)} logs: {ok} OK, {len(bad)} need attention.")
    print(f"Wrote {args.output} and {args.json}")


if __name__ == "__main__":
    main()
