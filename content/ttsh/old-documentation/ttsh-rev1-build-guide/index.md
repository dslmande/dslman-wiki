---
title: "TTSH rev1 build guide"
space: "TTSH"
space_key: "TTSH"
type: page
created: "2014-03-04T11:13:21"
updated: "2024-11-21T07:16:46"
confluence_id: "1311098"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/TTSH/pages/1311098"
attachments: 62
---

# TTSH rev1 build guide

> ##### `STATUS` finished
>
> **Released 11/2013**
>
> ##### the buildguide is only for rev.1 - check for TTSH rev.2 [this PAGE](../ttsh-rev2-build-guide/index.md) rev3 [here](../ttsh-rev3-build-guide/index.md)
>
> **last Modification Date:** 20.June 2017 - Voltage processor TL071 instead of LM301
>
> **updated** 21-November 2024 for new design after server change
>
> **BOM from me:** [BOM TTSH modified rev.1](../../../diy-synth-other/bom-ttsh-modified-rev-1/index.md)
>
> **Dokumentation:**[**http://thehumancomparator.net/building/**](http://thehumancomparator.net/building/)
>
> **Schematic:**[**TTSH-schematics.pdf**](assets/TTSH-schematics.pdf)**(also avaiable on zthees webserver)**
>
> **PCB reference designators:**[**TTSHcompplc.zip**](assets/TTSHcompplc.zip)**thx to**[**http://tauntek.com/TTSH.htm**](http://tauntek.com/TTSH.htm)
>
> **Muffwiggler Forum infos: (first page)**[**http://www.muffwiggler.com/forum/viewtopic.php?t=98954&postdays=0&postorder=desc&start=2130**](http://www.muffwiggler.com/forum/viewtopic.php?t=98954&postdays=0&postorder=desc&start=2130)
>
> `ATTENTION`
>
> **wiring from PSU to the module headers are wrong "silkreen error"  +/-  must crossed - doublecheck before power up modules,**
>
> **you find other issues in the second tab here**

Please read Buildings tips and known [Issues site](ttsh-rev1-known-issues/index.md)to save time and money.

I have completed few TTSHs and can share my experiences here.

Don´t solder switches, Pushbutton, faders and jacks prior finally assembly - the orientation is only correct by placing all jacks/faders together with the Frontpanel because the pcb bends a bit.

**Result from Widy/DSL-man:**

BOM failure - following parts arent listed

----------------------------------------

1x BC558b S&H  missing ( need 9 ..  BOM say 8)
1x 150K S&H missing ( not in building doc)
1x100p (missing part )

 bc337 for noise fix

**parts left DSL-man/widy**

------------------

1x 47K

2x 100N

optional parts from power input (hum modification)

optional parts from VCO bleed fix (caps)

**BOM**

<details>
<summary>click to expand the BOM</summary>

Here is the Original BOM from the great TTSH (Arp2600 clone)

[TTSH\_rev1.BOM.pdf](assets/TTSH_rev1.BOM.pdf)

Mouser cart

[https://de.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=4998691276](https://de.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=4998691276)

please add:

- 1x Powerswitch 633-CWT12AAS1
- 1x BC558 (in sum 9 )

some missing parts like Transistors, ICs, Reverb Spring, PSU, connectors, jacks and many more:

- Spring reverbs are avaiable from [Banzai](http://www.banzaimusic.com/)
- PJ301BM Jacks are avaiable from [thonk.co.uk](http://thonk.co.uk) or [http://erthenvar.com/store](http://erthenvar.com/store/jack35mmv?filter_name=3.5mm%20nuts)
- Screws are avaiable from me 😉
- for speakers you can use Visaton FC8 /FS8 or similar
- tempcos are avaible by me and rare parts - send me email patrick at dsl-man   dot   de

</details>

> **Tipp**
>
> ### Tip
>
> **check the pcb for failures !**

![ttshbarepcb.jpeg](assets/ttshbarepcb.jpeg)

**you have to mark the pcb with labels or sticker by**[**using Mods/bugfixes.**](ttsh-rev1-known-issues/index.md)**otherwise you have to desolder parts.**

![markings.JPG](assets/markings.jpg)

**Starts soldering the VCO Boards:**

**Online building documentation failure:**

**for VCO pcbs in zthees building website shows 1x61k9  but needed on each pcb 2x 61k9 resistors**

[**http://thehumancomparator.net/4027-2/**](http://thehumancomparator.net/4027-2/)

**TTSH VCO potted modules, I  have new - empty bare pcbs on**[**diysynth.de**](http://diysynth.de)**for sale or drop me a email.**

![TTSHvco.jpeg](assets/TTSHvco.jpeg)

### **Start assembly Main PCB**

Use standoffs/Spacers while assembling

![spacer.JPG](assets/spacer.jpg)

Add the Jumper close to the power section (left hand of ferrite beads)

### **Mounting VCO-1 pcb with long headers, but solder before 150K & 3m3**

**please read at first the known issue page -**[**VCO2/VCO3 issue**](#)

( i use long headers instead of zthees preferred headers to have more space between subvco parts and mainpcb, zthees solution is better for troubleshooting, but you have to unmount the frontpanel due to cutting the cabletie)

![vco-mount.JPG](assets/vco-mount.jpg)

![subvco2.JPG](assets/subvco2.jpg)

### **PSU with DC-DC Voltage "regulator"**

### **right picture shows the X-crossed ferrite bead to fix the -15/+15V silkscreen error,**

**cross one Ferrite on top pcb side - the ferrite on other pcb site (not shown here)**

![powerheaders.JPG](assets/powerheaders.jpg)

### **VCO testing - connect a + 15v cable to power distribution header and at the other side to the resistor as shown**

further: dont solder the VCOs  jack complete - solder only a bit, because the frontpanel don´t fit with this position 100%

![ttsh10.jpeg](assets/ttsh10.jpeg)

![ttsh9.jpeg](assets/ttsh9.jpeg)

### **VCF picture - handle with care - 2n3904/06 - BC558 doublecheck the position near Tempco**

further please read careful Jons building guide for VCF - there is a issue with matched pair 2N3906 - silkscreen error etc**-**[**check here**](http://thehumancomparator.net/vcf/)

![ttsh8.jpeg](assets/ttsh8.jpeg)

![ttsh7.jpeg](assets/ttsh7.jpeg)

### **AR/ADSR**

![20140309_233609.jpg](assets/20140309_233609.jpg)

### **VCA**

for testing: test with probe a VCO (you a need +15V/-15V power cable as shown above)

feed the VCO signal with a patch cable to the VCA input and check the waveform with a oscilloscope.

![ttsh5.jpeg](assets/ttsh5.jpeg)

![ttsh6.jpeg](assets/ttsh6.jpeg)

![ttsh4.jpeg](assets/ttsh4.jpeg)

![ttsh3.jpeg](assets/ttsh3.jpeg)

### **Ringmod, Preamp, Envelope Follower**

![20140310_232532.jpg](assets/20140310_232532.jpg)

### **Mixer**

Don´t solder the pot, switch, jacks - the frontpanel doesn´t match with the Partposition yet.

![TTSH2.jpeg](assets/TTSH2.jpeg)

![ttsh1.jpeg](assets/ttsh1.jpeg)

### **Noise, Voltage Processor**

> **Achtung**
>
> ### Warning
>
> with the 2n5172 the noise is distorted and have a very high gain..

**tested Rolution:**

leave out the 2n5172 - use a bc337/16, - bend right leg to top, solder a 10K resistor in series to the 1uF cap.

![ttsh-bc337.jpg](assets/ttsh-bc337.jpg)

![ttsh-noise-10k.jpg](assets/ttsh-noise-10k.jpg)

![20140523_002232.jpg](../../../diy-synth-other/projects/minimoog-restauration/assets/20140523_002232.jpg)

Change in the voltage processor section the LM301 for a TL071 and dont assemble the 30pf capacitor. (its only one IC to be changed)

![rev1-tl071.jpg](assets/rev1-tl071.jpg)

### first Panel mounting test

![20140311_232625.jpg](assets/20140311_232625.jpg)

### **S/H - Clock - Noise**

> **Achtung**
>
> ### Warning
>
> Due to some issues from the clock LED driver - we bridge the 2n5172.
>
> see here: [http://thehumancomparator.net/modifications/](http://thehumancomparator.net/modifications/)

All Parts soldered, Panel mounted, need to solder the jacks.

![ttsh-pcb-panelside.jpeg](assets/ttsh-pcb-panelside.jpeg)

## **Build tip:**

if you want hear the sound of your TTSH before you have finished the headphone jack wiring,

you have to switch with a jumper the T/TN  or R/RN header, otherwise your Amplifier dont have a audiosignal.

![20140930_221722_LLS.jpg](assets/20140930_221722_LLS.jpg)

> **Tipp**
>
> ### Building Tip
>
> place each row of faders on PCB and solder 2 pins, place the Panel in right way and mount all screws,-- solder the Faders complete.
>
> remove the panel and plug all jacks in position, place the panel - mount all screws and few jacks with screws - turn the device, solder the jacks.
>
> solder the LED at last.
>
> Use on all sides spacers, for a faster panel un/mounting use spacers (with plastic/silicon washers) instead of screws and you can turn the panel on table without breaking some faders.

![20140313_231658.jpg](assets/20140313_231658.jpg)

![20140313_235126.jpg](assets/20140313_235126.jpg)

> **Tipp**
>
> **If  your NOISE leds and left Volume led dont work.., connect the 470r resistor near  amp/noise to the unlabeled solder hole (ground)**
>
> **its a grounding issue by removing the 10R and cap in power section due to hum issue (described in next step)**

![470R_fix.JPG](assets/470R_fix.jpg)

> **Tipp**
>
> ### **HUM Issue:**
>
> **by using of both amplifiers for integrated speakers i had massiv hum, by touching the panel the hum sound changes. (hum is only in speakers not in main out)**
>
> **a workarround from zthee,  was tested by me - it helps.**

**Solutions:**

make a small bridge between the 10Ω resistor and 100pF capacitor as in the attached picture shown

 for the reverb tank use RG174 cables or shielded microphone cable for the wiring, cheap thin RCA cable  isn't good enough - because the shielding was not designed for this impedance.

![gndfix.jpg](assets/gndfix.jpg)

![20140331_231051.jpg](assets/20140331_231051.jpg)

## Planned Case:

![TTSH case.png](assets/TTSH-case.png)

**Finalcase..**

![20140513_234649.jpg](../../../diy-synth-other/projects/ttsh-arp-2600-clone/assets/20140513_234649.jpg)
