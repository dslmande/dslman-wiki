---
title: "DDRM Expander"
space: "DDRM Build Doc"
space_key: "DDRM"
type: page
created: "2018-05-09T13:25:15"
updated: "2024-01-15T13:42:46"
confluence_id: "1704865"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DDRM/pages/1704865"
attachments: 30
---

# DDRM Expander

Successful Build : 04/2019 

> **tech:**
>
> it adds an envelope controllable Ring Modulator, Chorus, Tremolo, Delay, and Reverb effects. It is designed to work seamlessly with Deckard’s Dream, but it also works as a standalone audio effects device.

**Schematics:**

[DD-EXPANDER-SCHEMATICS-REV1.zip](assets/DD-EXPANDER-SCHEMATICS-REV1.zip) for rev.1.0

**BOM:**

[DD-EXP-BOM-REV1.0.1.pdf](assets/DD-EXP-BOM-REV1.0.1.pdf) latest version for rev.1.0 and **YOU MUST ADD** 2x TL071 and 1x 4.7uF MLCC capacitor RM5
~~[DD-EXP-BOM-REV1.0.0.xlsx](assets/DD-EXP-BOM-REV1.0.0.xlsx) (Old version) for rev.1.0~~

~~⚠️~~For all DDRM Expander : remove the 6N138 and buy 6N139 to avoid Midi issues (stucking notes)

### BOM LATEST BOARD VERSION INFO

> **rev.1.1 changes**
>
> **the new PCB Version is 1.1 !! (midi noise fixed)**
>
> it use following changes which affect the above BOM, you have to respect this:
>
> IC33 and IC37 is TL071 (DIP8)
>
> C166 not in BOM 4.7uF ceramic (MLCC) RM5

## latest firmware

[ExpanderMK1\_2.0.hex](assets/ExpanderMK1_2.0.hex)

It's for all Expander versions 

**DDRM Expander VC Placement Guide V2 from Kevin Looney:**

[DDRM Expander VC Placement Guide V2.pdf](assets/DDRM-Expander-VC-Placement-Guide-V2.pdf)

**DDRM FAQ and Build tipps from Todd**

[Deckard’s Dream Expander FAQ and Build Guide V1-7.docx](assets/Deckard-s-Dream-Expander-FAQ-and-Build-Guide-V1-7.docx)

**Trimmer Values (was requested by a user)**

SIG= 501 = 500Ohm

REF: 201 = 200R

0.2Khz =103 = 10K

2.5k = 103 = 10K

**Further Build Infos (was requested by a user)**

Distance between Panel and Slider/control PCB = 10mm

Distance between Controlpcb and analog pcb = 12mm

**MIDI-NOISE FIX pictures:**

**only for DIY PCB Version 1.0**

**is fixed in DIY PCB Version 1.1**

If you want a fix of your factory assembled Version, contact me 

**Click expand for Pictures from rev1.0 pcb Modification FIX**

<details>
<summary>Mehr anzeigen</summary>

![2pyM974zSAqQ8s84hUe03w.jpg](assets/2pyM974zSAqQ8s84hUe03w.jpg)

![P5S3ukldSw2HPuJcN8kKjQ.jpg](assets/P5S3ukldSw2HPuJcN8kKjQ.jpg)

![S7BjlRV4T3iAwkJdldaSuQ.jpg](assets/S7BjlRV4T3iAwkJdldaSuQ.jpg)

![UUD7BWGFSeuawbftlyu51g.jpg](assets/UUD7BWGFSeuawbftlyu51g.jpg)

**Addional pics 2021:**

![IMG_4289.jpeg](assets/IMG_4289.jpeg)

![IMG_4290.jpeg](assets/IMG_4290.jpeg)

![IMG_4291.jpeg](assets/IMG_4291.jpeg)

![IMG_4293.jpeg](assets/IMG_4293.jpeg)

![IMG_4292.jpeg](assets/IMG_4292.jpeg)

![IMG_4294.jpeg](assets/IMG_4294.jpeg)

 

![IMG_4295.jpeg](assets/IMG_4295.jpeg)

![IMG_4296.jpeg](assets/IMG_4296.jpeg)

</details>

**Power LED Installation:**

**remove the 12V LED from the Card PCB and drill a 4,5mm hole in the frontpanel - which is the standard size for 3mm LED-holders (****available in most electronic shops)**

**![UB7L3UbEQ%SQlZ52yx1eDQ.jpg](assets/UB7L3UbEQ-SQlZ52yx1eDQ.jpg)**

**psu DC-DC alternative part:**

DKMW30F-12 meanwell (approval ✅ - tested ✅)

The DSP chip, potentiometer, AS3310, As3340 from Musikding too ✅ confirmed

**Case:  169 USD**

[http://siddarthianinnovations.bigcartel.com/product/deckard-s-dream-expander-case-and-panel-pre-order](http://siddarthianinnovations.bigcartel.com/product/deckard-s-dream-expander-case-and-panel-pre-order)

**First Design Concept:**

![image2018-5-9_15-25-12.png](assets/image2018-5-9_15-25-12.png)

**Final:**

![36229582_10214477097855110_4460830948627316736_o.jpg](assets/36229582_10214477097855110_4460830948627316736_o.jpg)

![image2018-5-9_15-25-12.png](assets/image2018-5-9_15-25-12.png)

![36229582_10214477097855110_4460830948627316736_o.jpg](assets/36229582_10214477097855110_4460830948627316736_o.jpg)

![fullsizeoutput_632e.jpeg](assets/fullsizeoutput_632e.jpeg)

![D9dR7PhfShi3NGQFSlmyHA.jpg](assets/D9dR7PhfShi3NGQFSlmyHA.jpg)

![1B86B693-5119-4520-BF1E-48421701A8ED.jpg](assets/1B86B693-5119-4520-BF1E-48421701A8ED.jpg)

![K75AcTLiQti11nfF94DGXg.jpg](assets/K75AcTLiQti11nfF94DGXg.jpg)

![UUD7BWGFSeuawbftlyu51g.jpg](assets/UUD7BWGFSeuawbftlyu51g.jpg)

![2pyM974zSAqQ8s84hUe03w.jpg](assets/2pyM974zSAqQ8s84hUe03w.jpg)

![P5S3ukldSw2HPuJcN8kKjQ.jpg](assets/P5S3ukldSw2HPuJcN8kKjQ.jpg)

![S7BjlRV4T3iAwkJdldaSuQ.jpg](assets/S7BjlRV4T3iAwkJdldaSuQ.jpg)

![PeLWG0+gSwCDHjcr3gDnwg.jpg](assets/PeLWG0-gSwCDHjcr3gDnwg.jpg)

![UB7L3UbEQ%SQlZ52yx1eDQ.jpg](assets/UB7L3UbEQ-SQlZ52yx1eDQ.jpg)

![DDRM FX LEDs.png](assets/DDRM-FX-LEDs.png)

![Expander patch.png](assets/Expander-patch.png)

![IMG_4289.jpeg](assets/IMG_4289.jpeg)

![IMG_4290.jpeg](assets/IMG_4290.jpeg)

![IMG_4291.jpeg](assets/IMG_4291.jpeg)

![IMG_4293.jpeg](assets/IMG_4293.jpeg)

![IMG_4292.jpeg](assets/IMG_4292.jpeg)

![IMG_4294.jpeg](assets/IMG_4294.jpeg)

![IMG_4295.jpeg](assets/IMG_4295.jpeg)

![IMG_4296.jpeg](assets/IMG_4296.jpeg)
