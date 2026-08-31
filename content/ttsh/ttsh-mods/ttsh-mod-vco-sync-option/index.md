---
title: "TTSH Mod  VCO Sync Option"
space: "TTSH"
space_key: "TTSH"
type: page
created: "2014-08-28T13:56:11"
updated: "2021-05-27T05:58:24"
confluence_id: "1310751"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/TTSH/pages/1310751"
attachments: 15
---

# TTSH Mod  VCO Sync Option

## **TTSH Mod Sync Option**

**from Muffwiggler thanks to all supporters specially "Altitude" and "sduck"**

**i prefer Sync:**  for syncing  VCO 3 to VCO2 and VCO1   jumper (set a bridge) JP2,  V1 = out from VCO3(61k9 resistor), S1 to VCO1 sync input, S2 to VCO2 sync input  (at input = 1k5 resistor)

> **Info**
>
> **This MOD works in TTSH rev.1, rev.2, rev.3 8pcb version 7-8.x)**

> **Achtung**
>
> **its very important  to use shielded cable for VCO I/O connections to the sub vco boards (dont forget to ground the shield ob both sides)**
>
> **About the wiring to switches, do not  twist the cables, otherwise you get softsync issues.**
>
> **don‘t twist the cables for the switches ! or you get some soft sync.**
>
> **its a difficult MOD and there´re few risk to destroy your rare trannys of the VCO Cores  (2N4125, 2n5459, CA3046) if you do it wrong.**

for all users who got my TTSH SYNC PCB, only use the resistor values as shown (the VCO SYNC Version2 PCB use a different PCB designator layout)

![IMG_8587.jpg](assets/IMG_8587.jpg)

| **BOM** |
|---|
| 6x 100k resistors<br>4x 150k<br>2x 2N3904<br>2x 2N5459<br>2x 100nf X7R bypass cap MLCC<br>2x 10uf electrolyt cap<br>3 x MTA100 power header  and jack 3 pin<br>2x 2pin mta or 1x 4 pin mta header/jack<br>spacers, screws, nuts<br>shielded cables RG174<br>cables for power, switch<br>2x switches (UM 3pole) |

![535_11571_ttshsyncconnect_1_2.jpg](assets/535_11571_ttshsyncconnect_1_2.jpg)

![0E7D780F-A99B-4CB7-AE61-9D189A7A1ACA.jpeg](assets/0E7D780F-A99B-4CB7-AE61-9D189A7A1ACA.jpeg)

![osc_sync2.png](assets/osc_sync2.png)

**Thanks to Steve (sduck) for sharing this helpful picture:**

![535_syncwiring_1.jpg](assets/535_syncwiring_1.jpg)

---

![cut_vco_sync.png](assets/cut_vco_sync.png)
