---
title: "Syncussion SY-1M"
space: "DIY Synth other"
space_key: "DSO"
type: page
created: "2018-05-15T06:38:42"
updated: "2024-11-18T16:22:14"
confluence_id: "1147006"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147006"
attachments: 35
---

# Syncussion SY-1M

> **Project**
>
> ### Projecttitel: Syncussion SY-1M
>
> ### Status: `finished`
>
> ### Startdate: 10 May 2018
>
> ### Duedate: 15 Jun 2018
>
> ### last update: 18.Nov.2024 Mods added
>
> ### Manufacture link: [http://www.psycox.co.uk](http://www.psycox.co.uk)
>
> ### Facebook group: [https://www.facebook.com/groups/237916856594386/?ref=bookmarks](https://www.facebook.com/groups/237916856594386/?ref=bookmarks)

> **Achtung**
>
> Attention, this guide is only for the psycox Version **SY-1M** , the main difference on this Version is the addional Midi function, Matched SMD Transistors  and improved powersupply.
>
> check my [SY-1 page](../syncussion-sy-1-clone/index.md) for the thehumancomparator version.

> **Info**
>
> if you need help in SMT soldering or looking for a person who build the device, feel free to ask me Impressum - Info

**Table of contents**

## further links:

general discussion

[https://www.muffwiggler.com/forum/viewtopic.php?t=195208&start=0](https://www.muffwiggler.com/forum/viewtopic.php?t=195208&start=0)

### [http://www.psycox.co.uk](http://www.psycox.co.uk)

## BOM:

### make sure you know which PCB Version you have

**for SY-1M  rev.1** (sold in Arpil 2018) MOUSER BOM [https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=1305 e9618c](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=1305e9618c)

**or use rev.1** MOUSER/DIGIKEY BOM Cross-reference :[VIEW IN GOOGLE DOCS](https://docs.google.com/spreadsheets/d/15zy5_tkfOnWfvXh9dKe76XyZd1_T_WJLmkKGcOxtFRc/edit?usp=sharing)

**for  rev.2** (sold since 05.September 2018) [https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=b83daa5bf6](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=b83daa5bf6)

**for rev.1. and rev.2:**

add 2x Multiturntrimmer for CV V/Oct or 4x if you want multiturn for V/OCT Midi too.

order: T67W-100K from tme.eu or from mouser:

Mouser-Nr.:

 858-67YR100KLFTB

![IMG_1950.JPG](assets/IMG_1950.jpg)

**rev.1 customers from europe:**

|   |
|---|
| they seem correct now and save you nearly 50€ when ordering parts.<br>part 1: [https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=F6C0 4804D7](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=F6C04804D7)<br>part 2: [https://www.reichelt.de/my/1476644](https://www.reichelt.de/my/1476644)<br>remove from **one** list (because the´re few parts double)<br>the 220uF caps<br>the CD4069UBE<br>10uF capacitors<br>change the PSU DC-JACK to the same as powersupply is (2.1mm or 2.5mm)<br>add 4x 1nF styroflex or C0G capactors for the CD4069UBE VCOs |

**for both versions:** (not in BOM)

> **Achtung**
>
> C1 C2 C8 C10 must be a C0G/NP0 or Styrene   (polypropylene caps do not fit due to their size, maybe)
>
> order 4xC0G :  [810-FK28C0G2A102JN06](https://www.mouser.de/ProductDetail/TDK/FK28C0G2A102JN006?qs=sGAEpiMZZMvsSlwiRhF8qrzDtqoSAGGa%252bKks0jhsUjtjoknf6x%252bJ2Q%3d%3d)
>
> or  4x Styrene: [23PS210](https://www.mouser.de/ProductDetail/Xicon/23PS210?qs=sGAEpiMZZMv1cc3ydrPrF9hNhJC57Qe1v0pekX2vS2Q%3d)

## Important files:

#### rev.1 Build doc [SY-1M-BG.pdf](assets/SY-1M-BG.pdf)

#### rev.2 Build doc. [DOWNLOAD](assets/SY-1M_rev2.pdf)

### Midi Reference doc [Sy1M-Midi-Ref.pdf](assets/Sy1M-Midi-Ref.pdf)

#### Board Reference sheet: [sy\_1m\_board\_reference\_sheets\_825.zip](assets/sy_1m_board_reference_sheets_825.zip)

#### Original Schematics Pearl Syncussion: [schematics.pdf](assets/schematics.pdf)

## Usage VCO modes:

#### A VCO 1 only B VCO 1 modulates VCO 2 frequency, the latter is routed to the VCF C Both VCO to the filter but VCO1 at reduced level. D EG 1 modulates VCO1, EG2 modulates VCO2. Both VCO to the filter E VCO 1 modulates VCO 2 which has a sawtooth wave. VCO 2 to VCF F Noise to VCF, no oscillators

## HOWTO SMT ASSEMBLY:

[https://www.youtube.com/watch?v=B5xpuZQiFcY](https://www.youtube.com/watch?v=B5xpuZQiFcY)

## my addional build tipps:

- [ ] the first provided BOM was wrong, the included FLAT pushbutton (this ~7mm height switches aren´t needed), the correct 2 pushbutton switches (~12mm height ) are included for the first batch. (ordered until April 2018)
- [ ] the groundpads are not easy to solder, i prefer to use leadfree soldercore for this pads (clean this pcb sections after soldering)
- [ ] Change R63  to 1K to get the best noise gain or use a 2SC1815 like in the original  (with reversed pinout and a 10K resistor for R63) ![noise.jpg](assets/noise.jpg)
- [ ] **for calibration:** R10 and R42 must  be grounded or the VCO frequency goes down and down  - also you can try to trigger with a sequencer while calibration the syncussion.

![IMG_2212.jpg](assets/IMG_2212.jpg)

![IMG_2215.jpg](assets/IMG_2215.jpg)

#### **Power Input**

#### the BOM use a 2,5mm middle Pin powerconnector **BUT** the most powersupplys use a 2.1mm middle pin, you can´t use a 2.1mm powersupply with a 2.5mm connector.

#### the most webshops have more 2.1mm powersupplys in stock and 2.1mm is the defacto standard.

#### middlepin is +

#### Spec: DC 9V output with 300mA or more, 12v Powersupplys works too, but the regulators only waste the voltage to heat

**Pinheader assembly**

- [ ] solder one the pin header to the pcb
- [ ] shorten the pin stripes by 1mm-2mm ![EFD6EBDE-25B9-4F5F-A962-A49D98EB9F93.jpeg](assets/EFD6EBDE-25B9-4F5F-A962-A49D98EB9F93.jpeg)
- [ ] plug the pin stripes in the hader, it has to be full in it - like this: ![C3813308-6BA2-427C-8B6A-C78B8E4E3A5E.jpeg](assets/C3813308-6BA2-427C-8B6A-C78B8E4E3A5E.jpeg)

- [ ] now attach on the top a further pinheaderlike this: (the same is on the right side with the 3pin header,  the 4pin header dont must be shorten because the header don´t have the same height.

       

![E06C713E-846D-4BAA-8BAA-190CA9111DC4.jpeg](assets/E06C713E-846D-4BAA-8BAA-190CA9111DC4.jpeg)

before you solder the pinheaders to the top pcb

make sure the pcb is flat and do not bend.

![CC2BA188-5833-4C68-A916-482EDB57F2AA.jpeg](assets/CC2BA188-5833-4C68-A916-482EDB57F2AA.jpeg)

make sure you solder the MIDI channnel switch, midi input jack and power input to the bottom side like :

![DC7A9D6C-A091-4D68-BFAB-4DC1E642F4DA.jpeg](assets/DC7A9D6C-A091-4D68-BFAB-4DC1E642F4DA.jpeg)

![A344537D-68FE-48F4-ACB2-7E6E11EAEA22.jpeg](assets/A344537D-68FE-48F4-ACB2-7E6E11EAEA22.jpeg)

if you have everything soldered and you´re ready for the first test, make sure all IC´s and THT Trannys have the correct orientation, dont install the ATMEGA for the first test

please doublecheck the polarity of your powersupply, middle pin is +

set the powerswitch to off,

connect the powersupply

## Changes/mods

- the original Syncussion use a 2SC1815 in the noise section, i tried it in one build  type (with reversed pinout) and a 10K resistor for R63, the result is the same like with BC547 (no difference in sound, gain etc.)
- use Multiturn trimmer for CV V/OCT and Midi v/oct
- [https://maffez.com/?page\_id=3864](https://maffez.com/?page_id=3864)   → MODS
- Cv Decay Modifikation:
  [Syncussion Decay CV Input Mod.pdf](assets/Syncussion-Decay-CV-Input-Mod.pdf)

## Power Modification (available by [DIYsynth.de](http://DIYsynth.de) )

install on new build to get a much cleaner signal without fizz, hum, less noise on audio outputs

![IMG_7232.jpg](assets/IMG_7232.jpg)

![IMG_7234.jpg](assets/IMG_7234.jpg)

![IMG_7233.jpg](assets/IMG_7233.jpg)

(click to enlarge)

![59007666144__E9518E0A-12FB-414A-81F1-5E597E0F576F.jpg](assets/59007666144__E9518E0A-12FB-414A-81F1-5E597E0F576F.jpg)

![IMG_7855.jpeg](assets/IMG_7855.jpeg)

![59007665195__6B1D1053-224F-4292-BCF2-1B989A0CF13D.jpg](assets/59007665195__6B1D1053-224F-4292-BCF2-1B989A0CF13D.jpg)

![IMG_7852.jpeg](assets/IMG_7852.jpeg)

#### Dustcover mats:

#### [http://synthronics.de/dust-covers\_syncussion\_sy-1m/](http://synthronics.de/dust-covers_syncussion_sy-1m/)

![fullsizeoutput_6230.jpeg](assets/fullsizeoutput_6230.jpeg)

![fullsizeoutput_622f.jpeg](assets/fullsizeoutput_622f.jpeg)

#### Gallery

![noise.jpg](assets/noise.jpg)

![IMG_2212.jpg](assets/IMG_2212.jpg)

![IMG_2215.jpg](assets/IMG_2215.jpg)

![F3F65252-A829-4410-99DF-22EB6B20AAF3.jpeg](assets/F3F65252-A829-4410-99DF-22EB6B20AAF3.jpeg)

![F6446814-DB98-47CF-97CC-AF40784B0C6C.jpeg](assets/F6446814-DB98-47CF-97CC-AF40784B0C6C.jpeg)

![94671F48-E9EF-4C43-8D83-B296DAE3CA66.jpeg](assets/94671F48-E9EF-4C43-8D83-B296DAE3CA66.jpeg)

![C3813308-6BA2-427C-8B6A-C78B8E4E3A5E.jpeg](assets/C3813308-6BA2-427C-8B6A-C78B8E4E3A5E.jpeg)

![E06C713E-846D-4BAA-8BAA-190CA9111DC4.jpeg](assets/E06C713E-846D-4BAA-8BAA-190CA9111DC4.jpeg)

![IMG_1950.JPG](assets/IMG_1950.jpg)

![66A778C5-A384-4469-BDE5-7FD12979F09A.jpeg](assets/66A778C5-A384-4469-BDE5-7FD12979F09A.jpeg)

![F801EC19-5F7D-4EF3-96A3-A0A6527CFE42.jpeg](assets/F801EC19-5F7D-4EF3-96A3-A0A6527CFE42.jpeg)

![CC2BA188-5833-4C68-A916-482EDB57F2AA.jpeg](assets/CC2BA188-5833-4C68-A916-482EDB57F2AA.jpeg)

![A344537D-68FE-48F4-ACB2-7E6E11EAEA22.jpeg](assets/A344537D-68FE-48F4-ACB2-7E6E11EAEA22.jpeg)

![DC7A9D6C-A091-4D68-BFAB-4DC1E642F4DA.jpeg](assets/DC7A9D6C-A091-4D68-BFAB-4DC1E642F4DA.jpeg)

![67F59ED5-479C-4C05-8CB3-FFDD308F572D.jpeg](assets/67F59ED5-479C-4C05-8CB3-FFDD308F572D.jpeg)

![F3F9AC36-829C-4E30-BFE6-8EFEF3F7BB23.jpeg](assets/F3F9AC36-829C-4E30-BFE6-8EFEF3F7BB23.jpeg)

![EFD6EBDE-25B9-4F5F-A962-A49D98EB9F93.jpeg](assets/EFD6EBDE-25B9-4F5F-A962-A49D98EB9F93.jpeg)

![IMG_7232.jpg](assets/IMG_7232.jpg)

![IMG_7234.jpg](assets/IMG_7234.jpg)

![IMG_7233.jpg](assets/IMG_7233.jpg)

![59007666144__E9518E0A-12FB-414A-81F1-5E597E0F576F.jpg](assets/59007666144__E9518E0A-12FB-414A-81F1-5E597E0F576F.jpg)

![IMG_7852.jpeg](assets/IMG_7852.jpeg)

![IMG_7855.jpeg](assets/IMG_7855.jpeg)

![59007665195__6B1D1053-224F-4292-BCF2-1B989A0CF13D.jpg](assets/59007665195__6B1D1053-224F-4292-BCF2-1B989A0CF13D.jpg)

![fullsizeoutput_5bdb.jpg](assets/fullsizeoutput_5bdb.jpg)

![IMG_4103.jpg](assets/IMG_4103.jpg)

![fullsizeoutput_622f.jpeg](assets/fullsizeoutput_622f.jpeg)

![fullsizeoutput_6230.jpeg](assets/fullsizeoutput_6230.jpeg)

![SY-1M.jpg](assets/SY-1M.jpg)

![SY-1M.jpg](assets/SY-1M.jpg)
