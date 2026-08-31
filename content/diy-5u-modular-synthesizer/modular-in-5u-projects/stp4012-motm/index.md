---
title: "STP4012 MOTM"
space: "DIY 5U Modular Synthesizer"
space_key: "MAIN"
type: page
created: "2018-07-16T10:38:05"
updated: "2019-03-04T17:28:49"
confluence_id: "1705300"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/MAIN/pages/1705300"
attachments: 20
---

# STP4012 MOTM

> **Info**
>
> | ID | Date | change | by |
> |---|---|---|---|
> | 1 | initial 2018 |   |   |
> | 2 | 04 nov.2018 | failure in BOM and Schematics | LED-man |
> | 3 | 06 nov 2018 | BOM - review |   |
>
> **please contact me****if you want a assembled Module**
>
> **The PCB and Panel is exclusively avaible from www.diysynth.de**

The Schematics are only available for users who ordered the PCB or Module, contact me.

**Module Description:**

**5U MOTM format  3U width (221,87mm x 132,97mm)**

based on the Arp 4012 Idea

LED Slider

Resonance CV Vactrol based

easy to build

less wiring

skiff friendly

powder coated and silkscreened Aluminium panel

only 2 SMT components (led driver)

10/11mm leadspace (no bloody fingers like eurorack 7mm leadspace)

leadfree pcbs

MOTM Power header (-15V/15V)

**Connections:**

3 Audio Inputs

3 CV Inputs

1 Resonance CV input

1 Output

**BOM:**

[Controlboard\_1.1.8.xlsx](assets/Controlboard_1.1.8.xlsx)

~~[BOM\_potted\_Module\_4012\_v1.1.xlsx](assets/BOM_potted_Module_4012_v1.1.xlsx)~~

~~[BOM\_potted\_Module\_4012\_v1.2.xlsx](assets/BOM_potted_Module_4012_v1.2.xlsx) one typo fixed  R2 = must be 470R instead 420R~~

[BOM\_potted\_Module\_4012\_v1.3.xlsx](assets/BOM_potted_Module_4012_v1.3.xlsx)  R2 must be 470R, R1 must 470R instead of 100K

(Double check with this file: [![4012-potted.png](assets/4012-potted.png)](assets/4012-potted.png)

> **warning**
>
> There was a failure in old BOM and Schematics for the Controlpanel PCB, before 06.Nov.2018
>
> R7 must be 3M3
>
> R14 must be 150K
>
> R29 to be doublechecked with JMLS in schematics 5K
>
> c11 must be 22-47pf
>
> R20 on controlboard is 100K - not listed in BOM.

**Info for rare parts:**

|   |   |   |   |
|---|---|---|---|
| QUANTITY | VALUE | DESCRIPTION | OTHER |
| 1 | 2N3958 | JFET N-Channel Dual | rare part, ask Patrick aka DSL-man/LED-man |
| 1 | 1k87 | Tempco | rare part, ask Patrick aka DSL-man/LED-man |
|   |   |   |   |

## Buildguide:

Short version:

Controlboard:

start with the SMT Parts: 2 x LED driver diode on controlboard

assembly the controlboard, SW input pin 2 must be connected to SW output pin 2 (see picture)

mount all spacers for frontpanel and potted module, the 4x 12mm spacer are between controlboard and potted module, the other 4x 12mm spacer between potted pcb and DIYSYNTH cover pcb.

note: theres a LED above from the Vactrol, positive/negative is the same as the vactrol pinout marking, you can place it in the lower or upper position (its in parallel)

**assembly the potted PCB:**

place all resistors and 1N4148, solder this parts.

capacitors next, then IC socket, transistors.

**The Ladder contains matched transistor pairs, match them to less 2mV VBE difference, or ask me for help.**

**test your 2N3958 tranistor and dont overheat them while soldering.**

**[4012\_potted\_module.png](assets/4012_potted_module.png)**

**Note,  there´s one 2N3906 on left side of the tempco (from the pair the transistor on top)**

![fullsizeoutput_5eae.jpeg](assets/fullsizeoutput_5eae.jpeg)

![fullsizeoutput_5eaf.jpeg](assets/fullsizeoutput_5eaf.jpeg)

  

![4012-potted.png](assets/4012-potted.png)

![5E32B750-3344-41A8-B60A-C1A6E081EF48.jpeg](assets/5E32B750-3344-41A8-B60A-C1A6E081EF48.jpeg)

![230FB55F-484F-468D-81B8-12C63808FC99.jpeg](assets/230FB55F-484F-468D-81B8-12C63808FC99.jpeg)

![47E378EC-AE4A-4143-B696-6F33BDA193F4.jpeg](assets/47E378EC-AE4A-4143-B696-6F33BDA193F4.jpeg)

![9C9FC3FD-A7C0-4A4A-95A0-4317F2924487.jpeg](assets/9C9FC3FD-A7C0-4A4A-95A0-4317F2924487.jpeg)

![87FFF037-C4B7-4868-A907-AF5DE99CCE1F.jpeg](assets/87FFF037-C4B7-4868-A907-AF5DE99CCE1F.jpeg)

![ACFEEBDF-8298-4E8A-805F-B7853C2ECDF3.jpeg](assets/ACFEEBDF-8298-4E8A-805F-B7853C2ECDF3.jpeg)

![56DBB574-06EC-449D-963B-63EF3E363FA8.jpeg](assets/56DBB574-06EC-449D-963B-63EF3E363FA8.jpeg)

![10D6604A-594B-43FD-B3ED-355A4BE609FC.jpeg](assets/10D6604A-594B-43FD-B3ED-355A4BE609FC.jpeg)

![fullsizeoutput_5eae.jpeg](assets/fullsizeoutput_5eae.jpeg)

![fullsizeoutput_5eaf.jpeg](assets/fullsizeoutput_5eaf.jpeg)

![4012-potted.png](assets/4012-potted.png)

![56DBB574-06EC-449D-963B-63EF3E363FA8.jpeg](assets/56DBB574-06EC-449D-963B-63EF3E363FA8.jpeg)
