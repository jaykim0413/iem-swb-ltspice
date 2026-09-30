# LTSpice Simulation Results

Compiled from 25 log file(s) under `iem-swb-ltspice`. 25 OK, 0 failed or empty.

Values use SI prefixes (m = milli, u = micro, n = nano, k = kilo, M = mega). Step columns are the `.step` parameters in LTSpice's run order.

## 1_wheel_supply

### 1_wheel_supply_1_hotplug_undamped

`1_wheel_supply/1_hotplug_undamped/1_wheel_supply_1_hotplug_undamped.log` · ✅ OK · run Wed Sep 30 01:30:50 2026 · 14.5 s

| step | lhar | rhar | vpk<br><sub>MAX(V(c))</sub> | ipk<br><sub>MAX(I(Lh))</sub> |
|---|---|---|---|---|
| 1 | 1u | 50m | 5.669 | 8.988 |
| 2 | 2u | 50m | 5.911 | 6.636 |
| 3 | 5u | 50m | 6.145 | 4.367 |
| 4 | 1u | 100m | 5.131 | 8.09 |
| 5 | 2u | 100m | 5.482 | 6.138 |
| 6 | 5u | 100m | 5.842 | 4.148 |
| 7 | 1u | 300m | 3.832 | 5.719 |
| 8 | 2u | 300m | 4.299 | 4.688 |
| 9 | 5u | 300m | 4.897 | 3.441 |

### 1_wheel_supply_2_hotplug_bounce

`1_wheel_supply/2_hotplug_bounce/1_wheel_supply_2_hotplug_bounce.log` · ✅ OK · run Wed Sep 30 01:31:59 2026 · 13.2 s

| step | lhar | rhar | vpk<br><sub>MAX(V(c))</sub> | ipk<br><sub>MAX(I(Lh))</sub> |
|---|---|---|---|---|
| 1 | 1u | 50m | 5.669 | 8.988 |
| 2 | 2u | 50m | 5.911 | 6.636 |
| 3 | 5u | 50m | 6.145 | 4.367 |
| 4 | 1u | 100m | 5.131 | 8.09 |
| 5 | 2u | 100m | 5.482 | 6.138 |
| 6 | 5u | 100m | 5.842 | 4.148 |
| 7 | 1u | 300m | 3.832 | 5.719 |
| 8 | 2u | 300m | 4.299 | 4.688 |
| 9 | 5u | 300m | 4.897 | 3.441 |

### 1_wheel_supply_3_damping_options

`1_wheel_supply/3_damping_options/1_wheel_supply_3_damping_options.log` · ✅ OK · run Wed Sep 30 01:33:50 2026 · 38.3 s

| step | cbulk | esr | rdamp | vpk<br><sub>MAX(V(c))</sub> | ipk<br><sub>MAX(I(Lh))</sub> | vled<br><sub>V(c)</sub> |
|---|---|---|---|---|---|---|
| 1 | 10u | 5m | 1m | 6.138 | 4.363 | 3.294 |
| 2 | 330u | 5m | 1m | 4.658 | 18.59 | 3.294 |
| 3 | 10u | 50m | 1m | 5.877 | 4.169 | 3.294 |
| 4 | 330u | 50m | 1m | 4.032 | 15.3 | 3.294 |
| 5 | 10u | 300m | 1m | 4.891 | 3.328 | 3.294 |
| 6 | 330u | 300m | 1m | 3.3 | 7.491 | 3.294 |
| 7 | 10u | 5m | 500m | 4.127 | 2.822 | 3.242 |
| 8 | 330u | 5m | 500m | 3.298 | 5.213 | 3.242 |
| 9 | 10u | 50m | 500m | 4.027 | 2.734 | 3.242 |
| 10 | 330u | 50m | 500m | 3.298 | 4.882 | 3.242 |
| 11 | 10u | 300m | 500m | 3.633 | 2.326 | 3.242 |
| 12 | 330u | 300m | 500m | 3.298 | 3.601 | 3.242 |

### 1_wheel_supply_4_load_step

`1_wheel_supply/4_load_step/1_wheel_supply_4_load_step.log` · ✅ OK · run Wed Sep 30 01:35:23 2026 · 2.8 s

| step | cbulk | vw_min<br><sub>MIN(V(vd))</sub> | gnd_off<br><sub>MAX(V(gw))</sub> |
|---|---|---|---|
| 1 | 10u | 3.237 | 31.41m |
| 2 | 330u | 3.28 | 11.01m |

### 1_wheel_supply_5_ride_through

`1_wheel_supply/5_ride_through/1_wheel_supply_5_ride_through.log` · ✅ OK · run Wed Sep 30 11:17:13 2026 · 2.2 s

| step | ild | cbulk | tdrop | vw_min<br><sub>MIN(V(vw))</sub> |
|---|---|---|---|---|
| 1 | 1m | 10u | 100u | 3.29 |
| 2 | 100m | 10u | 100u | 2.427 |
| 3 | 1m | 330u | 100u | 3.299 |
| 4 | 100m | 330u | 100u | 3.245 |
| 5 | 1m | 10u | 1m | 3.202 |
| 6 | 100m | 10u | 1m | 163.1m |
| 7 | 1m | 330u | 1m | 3.297 |
| 8 | 100m | 330u | 1m | 2.988 |

### 1_wheel_supply_6_limiter_softstart

`1_wheel_supply/6_limiter_softstart/1_wheel_supply_6_limiter_softstart.log` · ✅ OK · run Wed Sep 30 11:08:04 2026 · 29.5 s

| step | ilim | tau | cbulk | vpk<br><sub>MAX(V(c))</sub> | ipk<br><sub>MAX(I(Lh))</sub> | t_up<br><sub>V(c)=3.0</sub> |
|---|---|---|---|---|---|---|
| 1 | 250m | 1u | 10u | 3.459 | 1.696 | 1.094m |
| 2 | 500m | 1u | 10u | 3.62 | 1.776 | 1.05m |
| 3 | 1 | 1u | 10u | 3.942 | 1.938 | 1.028m |
| 4 | 250m | 10u | 10u | 6.081 | 4.322 | 1.011m |
| 5 | 500m | 10u | 10u | 6.081 | 4.322 | 1.011m |
| 6 | 1 | 10u | 10u | 6.081 | 4.322 | 1.011m |
| 7 | 250m | 100u | 10u | 6.081 | 4.322 | 1.011m |
| 8 | 500m | 100u | 10u | 6.081 | 4.322 | 1.011m |
| 9 | 1 | 100u | 10u | 6.081 | 4.322 | 1.011m |
| 10 | 250m | 1u | 330u | 3.316 | 1.725 | 4.933m |
| 11 | 500m | 1u | 330u | 3.333 | 1.805 | 2.965m |
| 12 | 1 | 1u | 330u | 3.366 | 1.987 | 1.985m |
| 13 | 250m | 10u | 330u | 3.316 | 6.767 | 4.403m |
| 14 | 500m | 10u | 330u | 3.333 | 6.877 | 2.708m |
| 15 | 1 | 10u | 330u | 3.366 | 7.109 | 1.864m |
| 16 | 250m | 100u | 330u | 3.844 | 14.88 | 1.096m |
| 17 | 500m | 100u | 330u | 3.877 | 15.04 | 1.094m |
| 18 | 1 | 100u | 330u | 3.939 | 15.37 | 1.09m |

## 2_spi_lines

### 2_spi_lines_1_sclk_unterminated

`2_spi_lines/1_sclk_unterminated/2_spi_lines_1_sclk_unterminated.log` · ✅ OK · run Mon Sep 28 21:14:48 2026 · 2.2 s

| step | td | vmax_chip1<br><sub>MAX(V(c))</sub> | vmin_chip1<br><sub>MIN(V(c))</sub> | vmax_chip2<br><sub>MAX(V(d))</sub> | vmin_chip2<br><sub>MIN(V(d))</sub> |
|---|---|---|---|---|---|
| 1 | 5n | 5.883 | -2.574 | 5.94 | -2.644 |
| 2 | 10n | 5.892 | -2.599 | 5.956 | -2.663 |
| 3 | 15n | 5.901 | -2.595 | 5.951 | -2.655 |

### 2_spi_lines_2_sclk_terminated

`2_spi_lines/2_sclk_terminated/2_spi_lines_2_sclk_terminated.log` · ✅ OK · run Mon Sep 28 22:37:13 2026 · 6.6 s

| step | rser | z0 | vmax_chip1<br><sub>MAX(V(c))</sub> | vmin_chip1<br><sub>MIN(V(c))</sub> | vmax_chip2<br><sub>MAX(V(d))</sub> | vmin_chip2<br><sub>MIN(V(d))</sub> | plateau_chip2<br><sub>MIN(V(d) )</sub> |
|---|---|---|---|---|---|---|---|
| 1 | 50 | 80 | 3.3 | -101u | 3.3 | -106.8u | 3.281 |
| 2 | 90 | 80 | 3.3 | 0 | 3.3 | 0 | 2.625 |
| 3 | 100 | 80 | 3.3 | 0 | 3.3 | 0 | 2.5 |
| 4 | 120 | 80 | 3.3 | 0 | 3.3 | 0 | 2.283 |
| 5 | 50 | 120 | 4.117 | -816.4m | 4.129 | -827.4m | 3.828 |
| 6 | 90 | 120 | 3.3 | -23.37u | 3.3 | -24.07u | 3.19 |
| 7 | 100 | 120 | 3.3 | 0 | 3.3 | 0 | 3.062 |
| 8 | 120 | 120 | 3.3 | 0 | 3.3 | 0 | 2.835 |
| 9 | 50 | 150 | 4.571 | -1.274 | 4.579 | -1.285 | 4.018 |
| 10 | 90 | 150 | 3.751 | -450.6m | 3.753 | -453.9m | 3.423 |
| 11 | 100 | 150 | 3.588 | -287.6m | 3.589 | -289.6m | 3.301 |
| 12 | 120 | 150 | 3.3 | -10.55u | 3.3 | -10.7u | 3.081 |

### 2_spi_lines_3_miso_roundtrip

`2_spi_lines/3_miso_roundtrip/2_spi_lines_3_miso_roundtrip.log` · ✅ OK · run Mon Sep 28 22:37:00 2026 · 0.2 s

| step | td | rser | t_hi<br><sub>V(c)=2.31</sub> | t_lo<br><sub>V(c)=0.99</sub> |
|---|---|---|---|---|
| 1 | 5n | 1m | 38.49n | 88.53n |
| 2 | 10n | 1m | 48.49n | 98.66n |
| 3 | 15n | 1m | 58.49n | 108.1n |
| 4 | 5n | 80 | 38.98n | 88.98n |
| 5 | 10n | 80 | 48.98n | 98.98n |
| 6 | 15n | 80 | 58.98n | 109n |

### 2_spi_lines_4_cs_backpower

`2_spi_lines/4_cs_backpower/2_spi_lines_4_cs_backpower.log` · ✅ OK · run Mon Sep 28 23:07:09 2026 · 32.9 s

| step | rser | rload | cbulk | ipk<br><sub>MAX(I(Vsense))</sub> | vend<br><sub>V(vccw)</sub> | t_wake<br><sub>V(vccw)=1.35</sub> |
|---|---|---|---|---|---|---|
| 1 | 1m | 3.3k | 10u | 85.48m | 2.743 | 222.8u |
| 2 | 100 | 3.3k | 10u | 20.52m | 2.664 | 935.7u |
| 3 | 200 | 3.3k | 10u | 11.69m | 2.589 | 1.66m |
| 4 | 430 | 3.3k | 10u | 5.897m | 2.432 | 3.391m |
| 5 | 1m | 330k | 10u | 85.48m | 2.886 | 221.9u |
| 6 | 100 | 330k | 10u | 20.52m | 2.885 | 919.3u |
| 7 | 200 | 330k | 10u | 11.69m | 2.884 | 1.609m |
| 8 | 430 | 330k | 10u | 5.897m | 2.882 | 3.182m |
| 9 | 1m | 3.3k | 330u | 85.48m | 2.743 | 7.283m |
| 10 | 100 | 3.3k | 330u | 20.52m | 2.627 | 30.58m |
| 11 | 200 | 3.3k | 330u | 11.69m | 2.404 | 54.25m |
| 12 | 430 | 3.3k | 330u | 5.897m | 1.86 | 110.8m |
| 13 | 1m | 330k | 330u | 85.48m | 2.83 | 7.252m |
| 14 | 100 | 330k | 330u | 20.52m | 2.743 | 30.05m |
| 15 | 200 | 330k | 330u | 11.69m | 2.543 | 52.58m |
| 16 | 430 | 330k | 330u | 5.897m | 1.996 | 104m |

### 2_spi_lines_5_combined_termination

`2_spi_lines/5_combinted_termination/2_spi_lines_5_combined_termination.log` · ✅ OK · run Mon Sep 28 23:12:08 2026 · 5.4 s

| step | rsrc | rwheel | t_rise<br><sub>t_rise</sub> | vmax_chip2<br><sub>MAX(V(d))</sub> | vmin_chip2<br><sub>MIN(V(d))</sub> | iclamp_max<br><sub>MAX(I(Vcl))</sub> | iclamp_min<br><sub>MIN(I(Vcl))</sub> |
|---|---|---|---|---|---|---|---|
| 1 | 1m | 1m | 1.523n | 3.955 | -652.7m | 30.28m | -29.33m |
| 2 | 100 | 1m | 5.133n | 3.3 | 559p | 4.301p | -4.3p |
| 3 | 1m | 100 | 2.69n | 3.897 | -596.4m | 7.77m | -7.661m |
| 4 | 100 | 100 | 9.369n | 3.3 | 989p | 4.301p | -4.3p |
| 5 | 1m | 330 | 5.481n | 3.872 | -572.3m | 3.531m | -3.542m |
| 6 | 100 | 330 | 19.17n | 3.3 | 1.978n | 4.301p | -4.3p |
| 7 | 1m | 1k | 13.66n | 3.844 | -543.8m | 1.285m | -1.287m |
| 8 | 100 | 1k | 42.87n | 3.3 | 4.859n | 4.301p | -4.3p |

### 2_spi_lines_6_backpower_tristate

`2_spi_lines/6_backpower_tristate/2_spi_lines_6_backpower_tristate.log` · ✅ OK · run Mon Sep 28 23:12:56 2026 · 1924.6 s

| step | rb | vrail_end<br><sub>V(vccw)</sub> | vrail_max<br><sub>MAX(V(vccw))</sub> |
|---|---|---|---|
| 1 | 22k | 397.7m | 475.6m |
| 2 | 47k | 739.2m | 804.8m |
| 3 | 100k | 1.173 | 1.222 |
| 4 | 1G | 2.148 | 2.152 |

## 3_esd_switch_lines

### 3_esd_switch_lines_1_no_protection

`3_esd_switch_lines/1_no_protection/3_esd_switch_lines_1_no_protection.log` · ✅ OK · run Mon Sep 28 23:54:25 2026 · 0.5 s

| step | vesd | vpin_max<br><sub>MAX(V(pin))</sub> | vpin_min<br><sub>MIN(V(pin))</sub> | iint_max<br><sub>MAX(I(Vsu))</sub> | idn_max<br><sub>MAX(I(Vsd))</sub> |
|---|---|---|---|---|---|
| 1 | -8k | 3.3 | -12.87 | 5.457p | 12.09 |
| 2 | 2k | 14.23 | 0 | 6.01 | 0 |
| 3 | 4k | 20.29 | 0 | 12.05 | 0 |
| 4 | 8k | 32.38 | 0 | 24.12 | 0 |

### 3_esd_switch_lines_2_series_r_only

`3_esd_switch_lines/2_series_r_only/3_esd_switch_lines_2_series_r_only.log` · ✅ OK · run Mon Sep 28 23:55:31 2026 · 0.4 s

| step | rser | vesd | vpin_max<br><sub>MAX(V(pin))</sub> | vpin_min<br><sub>MIN(V(pin))</sub> | iint_max<br><sub>MAX(I(Vsu))</sub> | idn_max<br><sub>MAX(I(Vsd))</sub> | vr_max<br><sub>MAX(V(vr))</sub> | vr_min<br><sub>MIN(V(vr))</sub> |
|---|---|---|---|---|---|---|---|---|
| 1 | 100 | 8k | 26.78 | 0 | 18.52 | 0 | 1.86k | 0 |
| 2 | 1k | 8k | 14.23 | 0 | 6.002 | 0 | 6.012k | 0 |
| 3 | 100 | -8k | 3.3 | -10.06 | 5.457p | 9.285 | 0 | -1.859k |
| 4 | 1k | -8k | 3.3 | -3.749 | 5.457p | 3.006 | 0 | -6.015k |

### 3_esd_switch_lines_3_series_r_tvs

`3_esd_switch_lines/3_series_r_tvs/3_esd_switch_lines_3_series_r_tvs.log` · ✅ OK · run Tue Sep 29 00:01:39 2026 · 0.8 s

| step | rser | vesd | vpin_max<br><sub>MAX(V(pin))</sub> | vpin_min<br><sub>MIN(V(pin))</sub> | iint_max<br><sub>MAX(I(Vsu))</sub> | idn_max<br><sub>MAX(I(Vsd))</sub> | itvs_max<br><sub>MAX(I(Vst))</sub> | itvs_min<br><sub>MIN(I(Vst))</sub> |
|---|---|---|---|---|---|---|---|---|
| 1 | 1m | 8k | 14.97 | 0 | 6.74 | 0 | 17.44 | -366.2u |
| 2 | 100 | 8k | 8.221 | 0 | 101.8m | 0 | 24.08 | 0 |
| 3 | 1k | 8k | 8.067 | 0 | 9.349m | 0 | 24.19 | 0 |
| 4 | 1m | -8k | 3.3 | -6.818 | 7.276p | 6.056 | 6.585 | -12.1 |
| 5 | 100 | -8k | 3.3 | -712.6m | 7.276p | 67.57m | 32.84m | -24.05 |
| 6 | 1k | -8k | 3.3 | -587.7m | 7.276p | 5.874m | 3.298m | -24.18 |

### 3_esd_switch_lines_4_leakage_margin

`3_esd_switch_lines/4_leakage_margin/3_esd_switch_lines_4_leakage_margin.log` · ✅ OK · run Tue Sep 29 00:03:18 2026 · 1.3 s

| step | rpu | rser | ileak | r_margin<br><sub>V(ctl)</sub> | v_high<br><sub>V(pino)</sub> |
|---|---|---|---|---|---|
| 1 | 70k | 1m | 0 | 30k | 3.3 |
| 2 | 100k | 1m | 0 | 42.86k | 3.3 |
| 3 | 140k | 1m | 0 | 60k | 3.3 |
| 4 | 70k | 1k | 0 | 29k | 3.3 |
| 5 | 100k | 1k | 0 | 41.86k | 3.3 |
| 6 | 140k | 1k | 0 | 59k | 3.3 |
| 7 | 70k | 1m | 1u | 30.94k | 3.23 |
| 8 | 100k | 1m | 1u | 44.8k | 3.2 |
| 9 | 140k | 1m | 1u | 63.87k | 3.16 |
| 10 | 70k | 1k | 1u | 29.91k | 3.23 |
| 11 | 100k | 1k | 1u | 43.75k | 3.2 |
| 12 | 140k | 1k | 1u | 62.81k | 3.16 |
| 13 | 70k | 1m | 10u | 43.04k | 2.6 |
| 14 | 100k | 1m | 10u | 75.57k | 2.3 |
| 15 | 140k | 1m | 10u | 152.3k | 1.9 |
| 16 | 70k | 1k | 10u | 41.61k | 2.6 |
| 17 | 100k | 1k | 10u | 73.81k | 2.3 |
| 18 | 140k | 1k | 10u | 149.8k | 1.9 |

### 3_esd_switch_lines_5_edge_speed

`3_esd_switch_lines/5_edge_speed/3_esd_switch_lines_5_edge_speed.log` · ✅ OK · run Tue Sep 29 00:04:39 2026 · 8.2 s

| step | rpu | rser | ctvs | t_fall<br><sub>t_fall</sub> | t_rise<br><sub>t_rise</sub> |
|---|---|---|---|---|---|
| 1 | 70k | 1m | 1f | 247.9p | 504.2n |
| 2 | 140k | 1m | 1f | 247.9p | 1.009u |
| 3 | 70k | 1k | 1f | 7.309n | 504.2n |
| 4 | 140k | 1k | 1f | 7.235n | 1.009u |
| 5 | 70k | 1m | 10p | 248.7p | 1.097u |
| 6 | 140k | 1m | 10p | 248.7p | 2.195u |
| 7 | 70k | 1k | 10p | 7.305n | 1.102u |
| 8 | 140k | 1k | 10p | 7.247n | 2.199u |
| 9 | 70k | 1m | 50p | 251.9p | 3.47u |
| 10 | 140k | 1m | 50p | 251.9p | 6.941u |
| 11 | 70k | 1k | 50p | 7.364n | 3.506u |
| 12 | 140k | 1k | 50p | 7.3n | 6.977u |

## 4_wheel_short

### 4_wheel_short_1_short_circuit

`4_wheel_short/1_short_circuit/4_wheel_short_1_short_circuit.log` · ✅ OK · run Wed Sep 30 01:21:27 2026 · 16.6 s

| step | ilim | cbulk | vdash_min<br><sub>MIN(V(g) )</sub> | i_qd_max<br><sub>MAX(I(Lh) )</sub> | i_short_max<br><sub>MAX(I(Vss))</sub> |
|---|---|---|---|---|---|
| 1 | 250m | 10u | 3.283 | 314.3m | 218.9 |
| 2 | 500m | 10u | 3.27 | 566.8m | 218.9 |
| 3 | 1 | 10u | 3.245 | 1.071 | 218.9 |
| 4 | 250m | 330u | 3.283 | 270.5m | 219.5 |
| 5 | 500m | 330u | 3.27 | 528.9m | 219.6 |
| 6 | 1 | 330u | 3.245 | 1.026 | 219.3 |

### 4_wheel_short_2_recovery

`4_wheel_short/2_recovery/4_wheel_short_2_recovery.log` · ✅ OK · run Wed Sep 30 01:23:50 2026 · 16.4 s

| step | ilim | cbulk | vrec_max<br><sub>MAX(V(c) )</sub> | t_rec<br><sub>V(c)=3.0</sub> | vdash_min_rec<br><sub>MIN(V(g) )</sub> |
|---|---|---|---|---|---|
| 1 | 250m | 10u | 3.373 | 30.12m | 3.283 |
| 2 | 500m | 10u | 3.453 | 30.06m | 3.27 |
| 3 | 1 | 10u | 3.612 | 30.03m | 3.245 |
| 4 | 250m | 330u | 3.294 | 33.98m | 3.283 |
| 5 | 500m | 330u | 3.294 | 31.98m | 3.27 |
| 6 | 1 | 330u | 3.294 | 30.99m | 3.245 |

## 5_rotary_encoder

### dc-sweep

`5_rotary_encoder/1_dc_sweep/dc-sweep.log` · ✅ OK · run Fri Sep 18 16:52:51 2026 · 1.6 s

| step | rpu | i_wet<br><sub>I(R1)</sub> | r_margin<br><sub>V(ctl)</sub> |
|---|---|---|---|
| 1 | 70k | 47.14u | 30k |
| 2 | 100k | 33u | 42.86k |
| 3 | 140k | 23.57u | 60k |

### dc-sweep-extended

`5_rotary_encoder/2_dc_sweep_extended/dc-sweep-extended.log` · ✅ OK · run Wed Sep 30 01:28:15 2026 · 1.0 s

| step | rpu | i_wet<br><sub>I(R1)</sub> | r_margin<br><sub>V(ctl)</sub> |
|---|---|---|---|
| 1 | 4.99k | 661.3u | 2.137k |
| 2 | 2k | 1.65m | 858 |
| 3 | 1.65k | 2m | 707.4 |

### clean-edge

`5_rotary_encoder/4_clean-edge/clean-edge.log` · ✅ OK · run Wed Sep 30 01:26:06 2026 · 87.6 s

| step | rpu | t_fall<br><sub>t_fall</sub> | t_rise<br><sub>t_rise</sub> |
|---|---|---|---|
| 1 | 70k | 428.7p | 553.4n |
| 2 | 100k | 440.7p | 826.2n |
| 3 | 140k | 456.8p | 1.233u |

### bounce

`5_rotary_encoder/5_bounce/bounce.log` · ✅ OK · run Wed Sep 30 01:25:16 2026 · 8.2 s

| step | rpu | t_first_low<br><sub>V(IN)=0.99</sub> | t_settled_low<br><sub>V(IN)=0.99</sub> |
|---|---|---|---|
| 1 | 70k | 1.027m | 1.177m |
| 2 | 100k | 1.027m | 1.177m |
| 3 | 140k | 1.027m | 1.177m |

### shared-return

`5_rotary_encoder/6_shared_return/shared-return.log` · ✅ OK · run Wed Sep 30 01:30:17 2026 · 0.4 s

| step | r_shared_fail<br><sub>V(ctl)</sub> | v_open_at_fail<br><sub>V(A1)</sub> | v_knob2_at_fail<br><sub>V(B7)</sub> | i_total<br><sub>I(V1)</sub> |
|---|---|---|---|---|
| 1 | 14.99k | 3.3 | 990m | -94.36u |

## LED_MOSFET

### pMOS_Button_LED

`LED_MOSFET/pMOS_Button_LED.log` · ✅ OK · run Wed Sep 30 12:59:29 2026 · 0.2 s

| step | i_pressed<br><sub>AVG(I(D1) )</sub> | i_released<br><sub>AVG(I(D1) )</sub> | v_in_pressed<br><sub>AVG(V(IN) )</sub> | t_press<br><sub>WHEN V(press)=1.65</sub> | t_led_on<br><sub>WHEN I(D1)=1m</sub> |
|---|---|---|---|---|---|
| 1 | 2.99m | 4.769p | 3.3u | 1.025m | 1.027m |
