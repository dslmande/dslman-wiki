---
title: "DDRM rev.2 guide"
space: "DDRM Build Doc"
space_key: "DDRM"
type: page
created: "2018-05-09T12:48:53"
updated: "2022-07-04T17:18:23"
confluence_id: "1704653"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DDRM/pages/1704653"
attachments: 29
---

# DDRM rev.2 guide

**Page History:**

| Date | Autor | what |   |
|---|---|---|---|
| May 9.  2018 | LED-man | DDRM 2.0 guide initial |   |
| Oct 25. 2018 | LED-man | BOM added |   |
| July 30 2019 | LED-man | software |   |
| Feb 2020 | LED-man | BOM pricing |   |
| June 2020 | LED-man | structure |   |
| Oktober 2021 | LED-man | BOM 6N138 to 6N139 |   |

### Table of Contents

> **Deckard's Dream Synthesizer**
>
> Hi all, this is the place to find the latest building documents for Black Corporation's Deckard's Dream polyphonic synthesizer.Currently, this project is at **rev 1.0**, PCB's are currently being released to builders. (18.Oct. 2017) and are being constructed.A new PCB version **rev. 2.1** is planned and the release is planned for July 2018, **this page is only for rev.2.x**

> **Info**
>
> Product Info:the Deckard's Dream product is available as Build to order and DIY KIT Version, both released in 2017.Its also known or coined as the "DDRM".The difference in the DIY KIT and assembled (Build to order) are:
>
> - the component format, the DIY KIT is mostly THT, the build to order synth is mostly in SMT.
> - The case size is not as deep for the build to order as it is for the DIY.
>
> Note: Although the DIY has most of the SMT devices pre-installed onto the PCBs, there are over 675 SMT decoupling capacitors (0805) and one small (SOIC8) power switch device that MUST be installed by the builder, in addition to the through hole componentsA addional 1U expander is planned - release in 2018Examples of Presets and voices: [https://soundcloud.com/deckardsdream](https://soundcloud.com/deckardsdream)

## Technical Specs:

<details>
<summary>Mehr anzeigen</summary>

### Synthesizer features

- 8-voice polyphonic analogue synthesizer
- Fully analogue signal path
- 2 synthesis layers per voice
- 256 presets

### Layer architecture

- VCO with square, saw and sine waveforms
- PWM with sine-wave LFO
- Manual PW (50-90%)
- 12dB HP and LP discrete filters with separate resonance controls
- ADSR filter envelope with adjustable initial and attack levels
- ADSR VCA envelope
- Velocity and aftertouch controls for filter brilliance and volume levels

### Master controls

- Global coarse/fine tune
- VCO2 detune
- LFO with sine, saw, ramp, square and stepped random waveforms
- LFO destinations: VCO, VCF, VCA
- Crossfade between layers 1 and 2
- Global filter brilliance and resonance control for additional resonance
- Polyphonic aftertouch destinations: LFO speed, LFO to VCO amount, LFO to VCF amount, filter brilliance, volume level
- Keyboard tracking adjustment for VCF and VCA

### Controls

- MIDI/MPE with polyphonic aftertouch
- Polyphonic pitchbend
- Unison
- MIDI over USB
- 128 factory and 128 user presets
- Alternate scales and tunings
- Software editor by [Spektro Audio](http://spektroaudio.com)

### Display

- 128×64 OLED display

### Connectors

- DC input jack (9-24V)
- External modulation input jack (1/4″)
- Expander jack (DIN5)
- USB jack (type B, device/host)
- MIDI IN jack (DIN5)
- MIDI THRU jack (DIN5)
- AUDIO OUT LOW jack (1/4″)
- AUDIO OUT HIGH jack (1/4″)

### Physical specifications \* the DIY VERSION is different for the depth and weight

- 19″ 4U rack-mount
- Width: 483mm / 19″
- Height: 178mm / 7″
- Depth: 200mm / 7.8″
- Weight: ~ 4.8 kg / 10.6 lbs incl external PSU brick.

</details>

## **Current identified Errors/Omissions/Errata:**

| Date | Location | Identified issue | Resolution |
|---|---|---|---|
| Oktober 2021 |   | BOM failure | change the 6N138 to 6N139 or you run in stucking notes |
|   |   |   |   |

## **Assembly Voicecard Guide: (credits to Trey Petty)**

**[DDRM Voice Card Guide.pdf](assets/DDRM-Voice-Card-Guide-1.pdf) updated 04 July 2022**

**the  10K resistor diagram, was incorrectly indicates the R185 position.**

## **User Manual**

[Deckards\_dream\_manual\_130.pdf](assets/454865_deckards_dream_manual_130.pdf)

## **Bugtracker**

further bugs, issues, problems are reported here (here are user reported issues due to soldering failures or other issues reported too)[https://github.com/ffont/ddrm-issues/issues](https://github.com/ffont/ddrm-issues/issues)
**Deckard's Dream Home and Store**: [http://www.deckardsdream.com](http://www.deckardsdream.com)

## ****Current BOM (last version valid 2.1.4 - Sep.2019)****

[DD-BOM-REV2.1.4.pdf](assets/DD-BOM-REV2.1.4.pdf)  [DD-BOM-REV2.1.4.xlsx](assets/DD-BOM-REV2.1.4.xlsx).  **change the 6N138 to 6N139 !!**

**Shared Mouser Basket:** [https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=15f70d6513](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=15f70d6513) (made by me - 09/2019 from 2.1.4 BOM, not checked by me - but the amount of parts looks ok)
Ultravox reply: "The cart doesn't include items that the BOM says are sourced from eBay, Small Bear, synthcube, etc."About partsourcing:  check the price for the next price break ( 3 resistors are more expensive than 10)for EU users: order from www.TME.eu standard parts, its cheaper as mouser
**Prices incl. 19% VAT(Germany) and shipping (combined)**Mouser 630€
OLED 10€
bracket 15€
spacers 25€
screws 10€
psu ext. 20€
v2164 x35 120€
CEM3340 x16 250€ or AS3340 120€
poti 100K   1x 2€
slidercaps set 12€
pushbuttons x5  5€
noise PIC x1 10€**t. TOTAL : 1.111€**
plus DIY PCB SET 999USD netto (no VAT/TAX calculated)plus Case 270USD netto (no VAT/TAX calculated)

## **OLED Display:**

make sure your OLED folow this pinout  **VCC-GND-SCL-SDA**, very often shows the shop the correct pinout but deliver another type.**AND short the pins on the display side (where the Frontpanel is) to prevent shorts to the Frontpanel.**if you cant source the correct display  (pin) use restore legs and bend they - use cable shrink tube to protect this for shorts
*(please note the version and changes at the bottom of the sheets. Also see Errors/Omission and Errata above)*

## **Powersuply Warning**

don't mix the external PSU bricks or you destroy your Device.

The Kijimi use a 24V DC PSU

DDRM v1 DIY use a 12V DC

PSU DDRM v2 DIY use a 12V DC 

## **Official Build Guide:**

~~[http://www.deckardsdream.com/build](http://www.deckardsdream.com/build)~~  use my tips:[DDRM v2 build tips](ddrm-v2-build-tips/index.md)

## **Firmware:**

**moved to separate page: [User Manual and Firmware](../user-manual-and-firmware/index.md)**

## **Knowledge and other links**

Build: [Deckards Dream General Build Thread](https://www.muffwiggler.com/forum/viewtopic.php?t=189382)Discussion: [DIY CS-80 imminent...(Deckard's Dream)](https://www.muffwiggler.com/forum/viewtopic.php?t=177810)[https://www.facebook.com/groups/deckardsdream/](https://www.facebook.com/groups/deckardsdream/)

## **Parts Resources:**

Synthcube complete parts kits: [http://synthcube.com/cart/ddrm-deckard-s-dream-kit](http://synthcube.com/cart/ddrm-deckard-s-dream-kit)Thonk Group Buys for CEM3340: [https://www.thonk.co.uk/shop/curtis-cem3340-ic-vco-chip/](https://www.thonk.co.uk/shop/curtis-cem3340-ic-vco-chip/)Metal Case: DIY Hub [http://siddarthianinnovations.bigcartel.com/product/deckard-s-dream-front-panel-and-rack-case-rev-2](http://siddarthianinnovations.bigcartel.com/product/deckard-s-dream-front-panel-and-rack-case-rev-2)Wooden Case: Ross Lammond (UK) [http://www.lamonddesign.co.uk/index/](http://www.lamonddesign.co.uk/index/)
**a very helpful Tool for the SMD Soldering**: (and sponsoring for this website hosting)([link here](https://www.amazon.de/gp/product/B01AL2YAQ6/ref=as_li_tl?ie=UTF8&tag=ledman-21&camp=1638&creative=6742&linkCode=as2&creativeASIN=B01AL2YAQ6&linkId=24106e9b77f9981031face0643a172db))
[![](https://images-na.ssl-images-amazon.com/images/I/71%2ByZAFinBL._SX522_.jpg)](https://www.amazon.de/gp/product/B01AL2YAQ6/ref=as_li_tl?ie=UTF8&tag=ledman-21&camp=1638&creative=6742&linkCode=as2&creativeASIN=B01AL2YAQ6&linkId=24106e9b77f9981031face0643a172db)

## Wooden Case: contact me if you want it

![IMG_0885.jpg](../../kijimi/assets/IMG_0885.jpg)

## Recent space activity

## Space contributors
