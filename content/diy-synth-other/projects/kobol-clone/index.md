---
title: "Kobol Clone"
space: "DIY Synth other"
space_key: "DSO"
type: page
created: "2018-11-22T22:18:38"
updated: "2024-02-16T21:51:32"
confluence_id: "1147703"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147703"
attachments: 38
---

# Kobol Clone

> **Project**
>
> ### Projecttitel: RSF KOBOL Clone
>
> ### Status: `finished`
>
> ### Startdate: 01/2019
>
> ### Duedate: 02/2020
>
> **Updated: 02/2023**
>
> ### Manufacture link: deliandiver.com
>
> [https://www.muffwiggler.com/forum/viewtopic.php?t=203509&highlight=](https://www.muffwiggler.com/forum/viewtopic.php?t=203509&highlight=)
>
> ### Summary:
>
> ### works, but its not for beginners and until the developer do not change the PSU from Main AC to Walwart psu its definitely not for beginners.
>
> you need 2x SSM2050 or use 2055/2056 with a mod.

This documentation is only for myself, to have some notes about changes and mods

This PCB which I used isn't available anymore !!

Theres no support available and much knowledge needed.

[https://www.youtube.com/watch?v=JGwuZxu\_NM0&t=4s](https://www.youtube.com/watch?v=JGwuZxu_NM0&t=4s)

Sync sounds:

[https://www.youtube.com/watch?v=JGwuZxu\_NM0&t=4s](https://www.youtube.com/watch?v=JGwuZxu_NM0&t=4s)

**Backup from Crazy.P incl. SSM.-SSI adapter pinout**

[expander1.zip](assets/expander1.zip)

## ISSUES

| Nr. | Description | Priority |   | Solution |
|---|---|---|---|---|
| 1 | Switches - use other pcbs footprint size and/or change panel to toggle switch | 1 |   |   |
| 2 | BOM : LOG for Volume LFO and VP out gain | 3 |   | fixed |
| 3 | missing mounting holes for pcbs | 2 |   | open ❌ |
| 4 | LED driver needed for gate led | 2 |   | fixed |
| 5 | leds polarity on pcb | 3 |   | fixed ? |
| 6 | LFO speed inverted pot, left is fast on the prototype | 1 | Or use reveresed Poti | fixed |
| 7 | panel holes too big for potis | 1 |   | open ❌ |
| 8 | powersupply design not allowed - | 2 |   | open - use a own PSU - Yamaha PA30 and resctifier, capactitors |
| 9 | markers for voltage test points missing | 3 |   | open ❌ |
| 10 | more clearly infos about matched trannys and resistors | 3 |   |   |
| 11 | envelope change too CEM3310 or digital | 1 |   | open ❌ |
| 12 | capacitors are too close next to the power supply section on mainboard | 1 |   | fixed |
| 13 | use bigger traces | 1 |   | open ❌ |
| 14 | Gate signal bleed in LFO | 1 | Blocker | fixed |
| 15 | V/oct unstable - waveforms wobbling - | 1 | Blocker | fixed |
| 16 | Lfo led not working | 3 |   | fixed |
| 17 | Holes in vcf board and VCO board to mount on metal spacers - for better mounting | 2 |   | open ❌ |
| 18 | Case doesn't fit with the panel | 1 |   | workaround possible |
| 19 | ua726 | 1 |   | use normal matched pair trannys |
| 20 | ssm2040 | 1 |   | use the new SSI 2040 !! |
| 21 |   |   |   |   |
| 22 | knobs ask Patrick\_H |   |   |   |
| 23 | connector 2pin | 13x | **JST XH2** | [https://www.reichelt.de/jst-stiftleiste-gerade-1x2-polig-xh-jst-xh2p-st-p185073.html?search=jst+st](https://www.reichelt.de/jst-stiftleiste-gerade-1x2-polig-xh-jst-xh2p-st-p185073.html?search=jst+st) |
| 24 | connector plug 2pin | 13 | **JST plug** | [https://www.reichelt.de/jst-buchsengehaeuse-1x2-polig-xh-jst-xh2p-bu-p185085.html?&nbc=1&trstct=lsbght\_sldr::185073](https://www.reichelt.de/jst-buchsengehaeuse-1x2-polig-xh-jst-xh2p-bu-p185085.html?&nbc=1&trstct=lsbght_sldr::185073) |
| 25 | pin connector | 26x for 2 pin<br>2x 3pin | **JST** | [https://www.reichelt.de/jst-crimpkontakt-buchse-xh-jst-xh-ckb-p185091.html?&nbc=1&trstct=lsbght\_sldr::185085](https://www.reichelt.de/jst-crimpkontakt-buchse-xh-jst-xh-ckb-p185091.html?&nbc=1&trstct=lsbght_sldr::185085) |
| 26 | connector 3pin | 2 | **JST** | [https://www.reichelt.de/jst-stiftleiste-gerade-1x3-polig-xh-jst-xh3p-st-p185074.html?&nbc=1&trstct=lsbght\_sldr::185086](https://www.reichelt.de/jst-stiftleiste-gerade-1x3-polig-xh-jst-xh3p-st-p185074.html?&nbc=1&trstct=lsbght_sldr::185086) |
| 27 | connector plug 3pin | 2 | **JST** | [https://www.reichelt.de/jst-buchsengehaeuse-1x3-polig-xh-jst-xh3p-bu-p185086.html?search=JST+XH](https://www.reichelt.de/jst-buchsengehaeuse-1x3-polig-xh-jst-xh3p-bu-p185086.html?search=JST+XH) |

## BOM: 11-2020

[rsf-kobol.xlsx](assets/rsf-kobol.xlsx)

changes:  

 in crazy.p clone R135 ---&gt; 68pF

 in Crazy.p clone R207 ---&gt; 22nF

## Panel Wiring 11-2020

[Project schematics RSF Kobol Expander I Clone.pdf](assets/Project-schematics-RSF-Kobol-Expander-I-Clone.pdf)

please note the 3Pin Connectors are wrong in the Wiring guide !! 

Ground is the middle pin on the 3Pole connectors.

for all jacks:

S is to be connected on TIP Pin (hot)

SW is the Tip Switch Pin (for grounding when no plug is in the jack inserted)

**Switches**

needed:  1x 2 rows with 3 pins (ON/OFF) power (DPST)

|   |   | mouser | RS |
|---|---|---|---|
| power |   | SSSU022800 |   |
| 4x normal |   |   | SSSU015100 |

**or:**

|   | mouser | ordered ✅ |   |
|---|---|---|---|
| power | MHS222K not avail. | ```<br>06-MHS22204<br>``` | [https://www.kynix.com/Detail/176774/MHS222K.html](https://www.kynix.com/Detail/176774/MHS222K.html) |
| 4x normal | ```<br>MHS122K<br>```<br>apem | home stock |   |
|   |   |   |   |

| Nr |   |   |   |   |
|---|---|---|---|---|
|   | Pots |   |   | 50€ thonk T18 shaft or round shaft- you need 2 center pots and 1-2 Log<br>100KB<br>2xx 100kA<br>100KB center detent for tune and vco2 beat optional for Freq. its up to you.<br>look at crazy patroches pic and in the BOM |
|   | jacks |   |   | 45€ |
|   | resistors |   |   | 30 |
|   | capacitors | 2,2MF | reichelt | 5euro |
|   | ICs: 3080, lm324, lmxxx |   |   | estimated 100€ |
|   | trannys, Power reg. |   |   | 5 |
|   | diodes |   |   | 2 |
|   | switches mouser |   |   | 10-20 |
|   | cable and headers |   |   | 20 |
|   | SSM2050 | 2x |   | 480€ or ask me for a replacement VCA/ADSR PCB to use CEM3310/AS3310 |
|   | heatsinks | 2x |   | 5 |
|   | external Yamaha PA30 |   |   | 50€ |
|   | SSM2040 |   |   | Ebay 50 or use new SSI2140 with adapter 10€ |
|   | case |   |   | Buchla boat from SAMODULAR - cut the frame to make it fit 100€ |
|   | ic sockets |   |   | 10-15€ |
|   | Yamaha PA-20 powersupply |   |   | 40€ |
|   | knobs tme |   |   | GWB19BK |
|   | LEDS | 3x |   | red |
|   |   |   |   |   |

## Calibration

1. **VCO: linearity** = High Freq. compensation. = there's a 1Mega Resistor which is connect to the Trimmer - adjust the Trimmer as close to 0V  (which is a OFFSET and affect the V/Oct calibration)

![image-2024-2-16_14-11-28.png](assets/image-2024-2-16_14-11-28.png)

2. VCO 1V/Oct as normal with Guitar tuner method or Freq. Counter/DMM

## Schematics:

[ob\_345da9\_schemas-carte-kobol-expander-1.pdf](assets/ob_345da9_schemas-carte-kobol-expander-1.pdf)

- [kobold-crazy-patroche.png](assets/kobold-crazy-patroche.png)
- [fullsizeoutput_6010.jpeg](assets/fullsizeoutput_6010.jpeg)
- [fullsizeoutput_601c.jpeg](assets/fullsizeoutput_601c.jpeg)
- [fullsizeoutput_6002.jpeg](assets/fullsizeoutput_6002.jpeg)
- [IMG_4167.JPG](assets/IMG_4167.jpg)
- [IMG_4128.JPG](assets/IMG_4128.jpg)
- [IMG_4127.JPG](assets/IMG_4127.jpg)
- [IMG_4124.JPG](assets/IMG_4124.jpg)
- [IMG_4109.JPG](assets/IMG_4109.jpg)
- [IMG_4041.JPG](assets/IMG_4041.jpg)
- [ob_044dfc_schemas-embase-et-sous-embase-expande.pdf](assets/ob_044dfc_schemas-embase-et-sous-embase-expande.pdf)
- [ob_cbd009_carte-lfo-noise-103-x-41.jpg](assets/ob_cbd009_carte-lfo-noise-103-x-41.jpg)
- [ob_5c5879_pcb-noise-lfo-avec-valeur-des-composan.pdf](assets/ob_5c5879_pcb-noise-lfo-avec-valeur-des-composan.pdf)
- [ob_97745d_pcb-recto-verso.pdf](assets/ob_97745d_pcb-recto-verso.pdf)
- [ob_c907a4_carte-vco-avec-valeur-composants.pdf](assets/ob_c907a4_carte-vco-avec-valeur-composants.pdf)
- [ob_52885e_photo-pcb-arriere-169-x-116.jpg](assets/ob_52885e_photo-pcb-arriere-169-x-116.jpg)
- [ob_75af04_photo-pcb-panel-avant-423-x-123.jpg](assets/ob_75af04_photo-pcb-panel-avant-423-x-123.jpg)
- [kobol-panel.pdf](assets/kobol-panel.pdf)
- [ob_00250d_carte-vco-avec-numero-des-composants.pdf](assets/ob_00250d_carte-vco-avec-numero-des-composants.pdf)
- [ob_78c71f_img025.jpg](assets/ob_78c71f_img025.jpg)
- [pcb-traces.pdf](assets/pcb-traces.pdf)
- [panel-parts.pdf](assets/panel-parts.pdf)
- [kobol-inside.jpg](assets/kobol-inside.jpg)
- [7hgNXffDTWSGkh3BAhVQEA.jpg](assets/7hgNXffDTWSGkh3BAhVQEA.jpg)
- [gJtar6PaTbOlUP5un4eAGA.jpg](assets/gJtar6PaTbOlUP5un4eAGA.jpg)
- [DKYnDwq4Qn6UsgnZXNMdGA.jpg](assets/DKYnDwq4Qn6UsgnZXNMdGA.jpg)
- [btqqy%owSCC3vztiLgzTnA.jpg](assets/btqqy-owSCC3vztiLgzTnA.jpg)
- [bts%PM7GSIysWGkNpXCYWQ.jpg](assets/bts-PM7GSIysWGkNpXCYWQ.jpg)
- [OYINPgdtRK26FKriqG4GrQ.jpg](assets/OYINPgdtRK26FKriqG4GrQ.jpg)
- [JuLhfmKKQJ2gV51sNMP4jQ.jpg](assets/JuLhfmKKQJ2gV51sNMP4jQ.jpg)
- [5048003E-0547-42C7-BC3E-823B4239BA12.jpg](assets/5048003E-0547-42C7-BC3E-823B4239BA12.jpg)
- [rsf-kobol.xlsx](assets/rsf-kobol.xlsx)
- [Project schematics RSF Kobol Expander I Clone.pdf](assets/Project-schematics-RSF-Kobol-Expander-I-Clone.pdf)
- [ob_345da9_schemas-carte-kobol-expander-1.pdf](assets/ob_345da9_schemas-carte-kobol-expander-1.pdf)
- [rect101.jpg](assets/rect101.jpg)
- [expander1.zip](assets/expander1.zip)
- [LJyMrzm.jpg](assets/LJyMrzm.jpg)
- [image-2024-2-16_14-11-28.png](assets/image-2024-2-16_14-11-28.png)

**MODS**:

from [http://www.crazy-patroche.com/2017/07/etude-des-racks-rsf-expander-1.html](http://www.crazy-patroche.com/2017/07/etude-des-racks-rsf-expander-1.html)

in case of the SSM2050 (2x needed)

you can use SSM2055/56 with changes

[https://oshpark.com/shared\_projects/N9Tw7FAP](https://oshpark.com/shared_projects/N9Tw7FAP)

or by hand wiring

Pin 2 to GND not shown - importend

![LJyMrzm.jpg](assets/LJyMrzm.jpg)

![kobold-crazy-patroche.png](assets/kobold-crazy-patroche.png)

Final Pictures:

![5048003E-0547-42C7-BC3E-823B4239BA12.jpg](assets/5048003E-0547-42C7-BC3E-823B4239BA12.jpg)

![gJtar6PaTbOlUP5un4eAGA.jpg](assets/gJtar6PaTbOlUP5un4eAGA.jpg)

![JuLhfmKKQJ2gV51sNMP4jQ.jpg](assets/JuLhfmKKQJ2gV51sNMP4jQ.jpg)

![bts%PM7GSIysWGkNpXCYWQ.jpg](assets/bts-PM7GSIysWGkNpXCYWQ.jpg)

![7hgNXffDTWSGkh3BAhVQEA.jpg](assets/7hgNXffDTWSGkh3BAhVQEA.jpg)

![btqqy%owSCC3vztiLgzTnA.jpg](assets/btqqy-owSCC3vztiLgzTnA.jpg)

![OYINPgdtRK26FKriqG4GrQ.jpg](assets/OYINPgdtRK26FKriqG4GrQ.jpg)

![DKYnDwq4Qn6UsgnZXNMdGA.jpg](assets/DKYnDwq4Qn6UsgnZXNMdGA.jpg)

![kobold-crazy-patroche.png](assets/kobold-crazy-patroche.png)

![fullsizeoutput_6010.jpeg](assets/fullsizeoutput_6010.jpeg)

![fullsizeoutput_601c.jpeg](assets/fullsizeoutput_601c.jpeg)

![fullsizeoutput_6002.jpeg](assets/fullsizeoutput_6002.jpeg)

![IMG_4167.JPG](assets/IMG_4167.jpg)

![IMG_4128.JPG](assets/IMG_4128.jpg)

![IMG_4127.JPG](assets/IMG_4127.jpg)

![IMG_4124.JPG](assets/IMG_4124.jpg)

![IMG_4109.JPG](assets/IMG_4109.jpg)

![IMG_4041.JPG](assets/IMG_4041.jpg)

![ob_cbd009_carte-lfo-noise-103-x-41.jpg](assets/ob_cbd009_carte-lfo-noise-103-x-41.jpg)

![ob_52885e_photo-pcb-arriere-169-x-116.jpg](assets/ob_52885e_photo-pcb-arriere-169-x-116.jpg)

![ob_75af04_photo-pcb-panel-avant-423-x-123.jpg](assets/ob_75af04_photo-pcb-panel-avant-423-x-123.jpg)

![ob_78c71f_img025.jpg](assets/ob_78c71f_img025.jpg)

![kobol-inside.jpg](assets/kobol-inside.jpg)

![7hgNXffDTWSGkh3BAhVQEA.jpg](assets/7hgNXffDTWSGkh3BAhVQEA.jpg)

![gJtar6PaTbOlUP5un4eAGA.jpg](assets/gJtar6PaTbOlUP5un4eAGA.jpg)

![DKYnDwq4Qn6UsgnZXNMdGA.jpg](assets/DKYnDwq4Qn6UsgnZXNMdGA.jpg)

![btqqy%owSCC3vztiLgzTnA.jpg](assets/btqqy-owSCC3vztiLgzTnA.jpg)

![bts%PM7GSIysWGkNpXCYWQ.jpg](assets/bts-PM7GSIysWGkNpXCYWQ.jpg)

![OYINPgdtRK26FKriqG4GrQ.jpg](assets/OYINPgdtRK26FKriqG4GrQ.jpg)

![JuLhfmKKQJ2gV51sNMP4jQ.jpg](assets/JuLhfmKKQJ2gV51sNMP4jQ.jpg)

![5048003E-0547-42C7-BC3E-823B4239BA12.jpg](assets/5048003E-0547-42C7-BC3E-823B4239BA12.jpg)

![rect101.jpg](assets/rect101.jpg)

![LJyMrzm.jpg](assets/LJyMrzm.jpg)

![image-2024-2-16_14-11-28.png](assets/image-2024-2-16_14-11-28.png)
