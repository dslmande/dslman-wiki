---
title: "RE-303 - not a further clone"
space: "DIY Synth other"
space_key: "DSO"
type: page
created: "2018-08-14T12:16:36"
updated: "2026-05-13T22:50:12"
confluence_id: "1147609"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147609"
attachments: 45
---

# RE-303 - not a further clone

> **Project**
>
> ### Projecttitel: DINSYNC RE-303
>
> ### Status: `done`
>
> ### Startdate: 2016
>
> ### Duedate: 09/2018
>
> ### **last update : 05/2026 (MIDI Wiring)**
>
> ### Manufacture link: [http://privat.bahnhof.se/wb447909/dinsync/re-303/](http://privat.bahnhof.se/wb447909/dinsync/re-303/)
>
> ### Forum : [http://23.235.199.139/~re303c5/forum/](http://23.235.199.139/~re303c5/forum/)

![IMG_0155.JPG](assets/IMG_0155.jpg)

![IMG_8231.jpeg](assets/IMG_8231.jpeg)

# Page Content:

# its not a clone, its a replica of the famous Roland TB-303

The Founder Paul Barker developed in 2016 the RE-303.

the "internal Name" is Space Cadet.

few different case types are avaiable/fits with the pcbs: TT-303 (old version),

you find a german article from me, about the RE-303 here:

[https://www.amazona.de/test-din-sync-re-303-die-beste-tb-303-ever/](https://www.amazona.de/test-din-sync-re-303-die-beste-tb-303-ever/)

## BOM:

#### The PCB set contains: (available on [https://shop.re-303.com/](https://shop.re-303.com/))

RE-303 v1.2 main-board and switch-board PCB.

Sumida coil and adapter.

3pc set of power transistors.

8pc set of potentiometers (tune, cutoff, resonance, env, decay, accent, tempo and volume with switch)

2pc set of rotary switches (pattern/mode)

3pc set of 6.3mm jacks (mix in, headphone, main out)

2pc set of 3.5mm jacks (cv/gate)

1pc DC jack

1pc waveform switch

**Parts what you have to source:**

**the following files are based on the same version but with different office formats:**

[RE-303 BOM\_1.2\_official.pdf](assets/RE-303-BOM_1.2_official.pdf)

[RE-303 BOM\_1.2\_official.xlsx](assets/RE-303-BOM_1.2_official.xlsx)

[RE-303 BOM\_1.2\_official.ods](assets/RE-303-BOM_1.2_official.ods)

**MOUSER BOM project card (very old ):** [https://www.mouser.at/ProjectManager/ProjectDetail.aspx?AccessID=0324e99177](https://www.mouser.at/ProjectManager/ProjectDetail.aspx?AccessID=0324e99177)

**plus tactiles:** 688-SKQEAA 

plus 50K Trimmer SMT for the ba662 - its mentioned in the BOM

> **Info**
>
> ### when you use the PIXIE or Sonic Potions CPU you dont need following parts
>
> ift(y): yellow coil for the original cpu clock
> ic2: cd4556B decoder/multiplexer
> ic3, ic4, ic5: cmos ram
> D4: 1n4148
> R6: 33k
> R7: 100k 
> R23: 22k 
> R39, R40, R41, R44: 3.3k
> C12: 0.01uf film 
> C57: 100uf / 25v electrolytic
> Q4: 2sc536f/2sc945p

## Buildguide v1.2

(source: [https://shop.re-303.com/build-it/](https://shop.re-303.com/build-it/))

[RE-303v1.2BUILDGUIDE.pdf](assets/RE-303v1.2BUILDGUIDE.pdf)

## Issue/Help

| **ID** | **Issue** | **Issue/Mod  Description and fix** |
|---|---|---|
| 1 | Gate | in case you hear the gate signal  - attack clicks  - you can try to connect a 100nF polar cap\*\*  between GND and Trigger.  Measure with an scope to find the best value - maybe you need a bigger value 220-470nf |
| 2 | sporadica addional random notes, accent, slides.<br>which wasn't programmed.<br>how to test:<br>make a video while doing this: clear a pattern and create a new pattern with notes and accent, slides. turn off the machine and play the pattern. compare the pattern with the recorded video. | root cause:<br>its a known issue that one Pixie CPU batch has “few” defect memory chips.<br>part nr:<br>MB85RS64VYPNF-G-BCERE1<br>Digikey ART: 865-MB85RS64VYPNF-G-BCERE1CT-ND<br>MFG : KAGA FEI AMERICA, INC. (VA) / MB85RS64VYPNF-G-BCERE1<br>DESC: IC FRAM 64KBIT SPI 33MHZ 8SOP<br>**you can remove them and install a new FRAM chip.**<br>only pattern was stored on the FRAM memory.<br>**This Issue was confirmed !**<br>![IMG_0742.jpeg](assets/IMG_0742.jpeg)<br>![IMG_0741.jpeg](assets/IMG_0741.jpeg)<br>![4903F71F-0C0A-42F2-A662-91501CEA7E32.jpg](assets/4903F71F-0C0A-42F2-A662-91501CEA7E32.jpg) |
| 3 | Rotary Switches<br>![IMG_1341.jpeg](assets/IMG_1341.jpeg)<br>![IMG_1342.jpeg](assets/IMG_1342.jpeg) | install R48 on the solder side of the PCb, the rotary switch is too close at R48 and can cause a electrical contact - failure here.<br>Furthermore look at the N4148 diodes too, D17 can be in touch  against the rotary switch body (the side where metal body is pressed in the switchPCB)  is at the bottom a risk to get in touch with diodes.<br>mount the diode and resistor from rearside. |
| 4 | Voltage testing 5.333Volt not given | make sure to buy the 6V2 Zener as described in the BOM 1.3. because its less tolerance and we reach 6,3V normal 6v2 zener has 5% and “don't give enough Volt”<br>use a SB596 instead of the TIP30 from the PCB Kit. the most users with voltage failure at the PSU used TIP30.. |
| 5 | Sonic Potions CPU (deprecated) | ***Sonicpotions CPU:  (deprecated )**pls. use the Pixie CPU*<br>*Julian from Sonic Potions developed a CPU for the RE303, this CPU is also an replacement for TB-303*<br>*(more here:*[https://www.sonic-potions.com](https://www.sonic-potions.com) *)*<br>*User guide:*[*SonicPotions\_Re-303\_User\_Guide.pdf*](assets/SonicPotions_Re-303_User_Guide.pdf)<br>*Installation guide:*[*SonicPotions\_Re-303\_Installation\_Guide.pdf*](assets/SonicPotions_Re-303_Installation_Guide.pdf)<br>*Forum about the CPU:*[*http://23.235.199.139/~re303c5/forum/forum/7-re-303-cpu/*](http://23.235.199.139/~re303c5/forum/forum/7-re-303-cpu/)<br>**Important**:  the Sonic potions CPU was available in 2 versions , and the installation is in a other direction/orientation than a PIXIE !!!<br>it depends on your version. the first version was the blue PCB..  the second a black PCB.  the black pcb is installed with the Atmega is at the not visible side.<br>at the first PCB version /blue)  is the atmega shown when you install the cpu.<br>but for both version: the MIDI Connector is at the right side of the  PCB (instead left like on the pixie)  and the MIDI pinout depends on your versions..<br>![IMG_1462.JPG](assets/IMG_1462.jpg)<br>![IMG_1461.JPG](assets/IMG_1461.jpg)<br>ATTENTION: for the newer black CPUs a different firmware image is needed than for the old blue ones<br>**Sonic Potions Firmware**: (not for Pixie)<br>[Version 0.95 =&gt; OLD BLUE CPU!](http://www.sonic-potions.com/public/re303/re303_0.95.syx)<br>[re303\_0.95.syx](assets/re303_0.95.syx)<br>[**Version 0.95\_V2 =&gt;**NEW BLACK CPU!](http://www.sonic-potions.com/public/re303/re303_v2_0.95.syx)<br>[re303\_v2\_0.95.syx](assets/re303_v2_0.95.syx) |
| 6 | 3D Printed case or Synthaur and TT-303 cases doesn't match, the upper note and LEDs doesn't align with the aluminum plate | [https://medium.com/@autoy/dinsync-re-303-adapting-the-kit-to-the-syntaur-replica-case-c593d6c6721b](https://medium.com/@autoy/dinsync-re-303-adapting-the-kit-to-the-syntaur-replica-case-c593d6c6721b)<br>[DinSync RE-303-case-adapting.pdf](assets/DinSync-RE-303-case-adapting.pdf) |

## Pixie CPU (included in the PCB Set)

Knowledge: "The Pixiepowered RE-CPU is a D650C emulator, which will allow you to run original maskrom firmware from original Roland(tm) machines."

Its included with the PCB Set, or you buy it separate to upgrade a TB-303 or swap a Sonic Potion CPU to this : [https://shop.re-303.com/product/pixie-powered-re-cpu/](https://shop.re-303.com/product/pixie-powered-re-cpu/)

###### the bootloader is still installed in the latest versions (purple), you only need to upload the TB-303 sysex file

**Firmware and more:**

 [https://github.com/sunflowr/recpu](https://github.com/sunflowr/recpu)

[http://www.d650.cc](http://www.d650.cc)

**FW manual 1.4.3**

[recpu\_manual.1.4.3.pdf](https://github.com/sunflowr/recpu/releases/download/v1.4.3/recpu_manual.1.4.3.pdf)

## Firmware Installation (on your own risk)

this guide is for the old version, which includes a info howto install everything

1. turn on and send 303.sysx with sysex librian tool
2. turn off and on again
3. send the [boot loader sysex](../re-808-its-a-replica-of-the-tr-808/assets/bootloader.syx)(1.4.3 version)
4. turn off
5. turn on while hold Step1 (all lets flashes like night rider mode)(some older boot loaders don't have the night rider mode)
6. now send the [REEMU 1.3.0 sysex](../re-808-its-a-replica-of-the-tr-808/assets/reemu.syx)
7. machine restarts byself in 1.3.0 mode
8. turn off and on the 303
9. reload the [boot loader 1.4.3](../re-808-its-a-replica-of-the-tr-808/assets/bootloader.1.4.3.syx) in boot loader mode (hold step1) and upload the [REEMU 1.4.3 sysex](../re-808-its-a-replica-of-the-tr-808/assets/reemu.1.4.3.syx)
10. send the TB303.sysx again

**new installation method since 2025:**

1. reload the [boot loader 1.4.3](../re-808-its-a-replica-of-the-tr-808/assets/bootloader.1.4.3.syx) in boot loader mode (hold step1) and upload the [REEMU 1.4.3 sysex](../re-808-its-a-replica-of-the-tr-808/assets/reemu.1.4.3.syx)

## Cases:

different cases are on the market:

**Alu case in black, silver, white, gold.. are available by Andreas.K on kumptronics.com:**
[https://www.kumptronics.com/shop/](https://www.kumptronics.com/shop/)

[http://23.235.199.139/~re303c5/forum/topic/396-re-303-aluminum-case-silver-andor-black-anodized/](http://23.235.199.139/~re303c5/forum/topic/396-re-303-aluminum-case-silver-andor-black-anodized/)

## Buildguide for the case:

[RE-303\_case\_assembly\_guide.pdf](assets/RE-303_case_assembly_guide.pdf)

you can also use a Bassbot TT-303 case (the first 303 style case), this was the first solution until Andreas sold the Alu cases.

the Bassbott Cases doesn't match without a lot of mechanical rework with a Dremel etc.

![](https://www.gearslutz.com/board/attachments/electronic-music-instruments-and-electronic-music-production/658188d1493933750-re-303-project-its-not-tb-303-clone-its-replica-20170504_225754.jpg)

## Modifications:

[http://www.ladyada.net/make/x0xb0x/mods.html](http://www.ladyada.net/make/x0xb0x/mods.html)

## Potentiometer Modification:

Available in my shop: (shipping starts end of June 2020)

[https://www.diysynth.de/pcbs-panels/re-303-pot-adapter.html](https://www.diysynth.de/pcbs-panels/re-303-pot-adapter.html)

![IMG_8207.jpeg](assets/IMG_8207.jpeg)

![IMG_8208.jpeg](assets/IMG_8208.jpeg)

no wobbling potentiometers anymore.. but the movement is stronger, a friend used other knobs too.

you also need for the Midi Jacks, 3.5mm adapter.

**BOM:**

you need one of this Stereo Pot: (VR4 in the 303)

VR4 B50K Stereo !! (linear stereo)

VR2, VR7 = 50KB (lin)

VR3, VR5 =50KA (log)

VR6 = 1MA (log)

in total 6 potentiometers

[https://www.thonk.co.uk/shop/alpha-9mm-pots-vertical-t18/](https://www.thonk.co.uk/shop/alpha-9mm-pots-vertical-t18/)

**and you need:**

To solder the Capacitor on the rear side of the 303 and one resistor.

pinstripes as shown above in my pictures.

2x 3.5mm (1/8inch) stereo jacks    Lumberg KLB-4 which is available worldwide in hundreds of shops - its a quality part.

2x Adapter for the Midi holes to use the 3.5mm jacks - ONLY if you use the RE-303 Aluminum case - this are included with the PCB order in my shop !

2x 3.5mm (1/8 inch) plug to MIDI Cable - thonk or make your own..  [https://www.thonk.co.uk/shop/alm-midi-trs-cable/](https://www.thonk.co.uk/shop/alm-midi-trs-cable/) or DIY: [NYS322](https://www.mouser.de/ProductDetail/568-NYS322) + [172-7435-E](https://www.mouser.de/ProductDetail/172-7435-E) (mouser) 

**update 01/2020:** ground the MIDI IN port too, that's needed because the acrylic's adapter to the stereo 3.5mm jacks are isolated

in case you use silver knobs: they are metalized and make grounding issues, you have to remove from the bottom the paint with a cutter knife.(easy)

the blue cable connects ground from MIDI out to the MIDI IN jack.

![IMG_9788.jpeg](assets/IMG_9788.jpeg)

![IMG_9789.jpeg](assets/IMG_9789.jpeg)

## Calibration VCO Tuning:

### The Easy Way from [https://antonsavov.net/audio\_plugins/as\_x0x\_tune/](https://antonsavov.net/audio_plugins/as_x0x_tune/)

- ❏ **Step1:** adjust TM5 untill low-c and high-C are one octave apart (the exact frequency doesn’t matter, as it’ll be fixed in Step 2)
- ❏ **Step2:** adjust TM4 untill you get the right frequency for an A note against a reference (that’s equivalent to adjusting the TUNE knob on the front)
-

## Battery Tray - optional

You will need 5x 1.2V AA batteries, get the ones from IKEA, they're from the same factory as the Eneloop ones but for a fraction of the cost.

Unless you can find a 5x AA battery tray best bet is to 3d print your own.

Then follow the official guide for installing the battery tray.

It is important to fit a 10 Ohm resistor as in this photo.

[303-BATTERY-TRAY.stl](assets/303-BATTERY-TRAY.stl)

![22473626_10212631833485061_1605834833_o.jpg](assets/22473626_10212631833485061_1605834833_o.jpg)

![RE303Batteries.jpg](assets/RE303Batteries.jpg)

![22251319_1147607008705443_1880324767_o.jpg](assets/22251319_1147607008705443_1880324767_o.jpg)

### **DIN JACK Connector with integrated switch - required for TT cases or TB cases.**

the RE-303 cases have a separate switch for In/OUT Sync.

**assembled versions are available  there and on eBay:**

[https://sfsynthworks.com/store/p/switching-din-sync-jack?utm\_medium=email&utm\_source=customer\_notification](https://sfsynthworks.com/store/p/switching-din-sync-jack?utm_medium=email&utm_source=customer_notification)

[Switching+DIN+Sync+Jack+Assembly+&+Installation.pdf](assets/Switching-DIN-Sync-Jack-Assembly-Installation.pdf)

**or create your own by 3D print it (SLA)**

[Switching DIN Sync Jack - housing.stl](assets/Switching-DIN-Sync-Jack---housing.stl)

[Switching DIN Sync Jack - actuator.stl](assets/Switching-DIN-Sync-Jack---actuator.stl)

- -  Switch: Alps Alpine SPVQ910205
- -  DIN 5 Jack: Multicomp PSG03463

![IMG_7677.jpeg](assets/IMG_7677.jpeg)

![IMG_7676.jpeg](assets/IMG_7676.jpeg)

![IMG_7675.jpeg](assets/IMG_7675.jpeg)

![IMG_1238.jpeg](assets/IMG_1238.jpeg)

**howto use the Sync jack for MIDI instead of separate MIDI I/O connectors**

R29 yellow cable goes to Pin2 at Pixie CPU MIDI IN

R182 red cabe goes to Pixie CPU MIDI IN PIN1

please note: MIDI Slave works when you insert a MIDI Cable to the SYNC24 PORT , with above mod

analog Sync24 doesn't work anymore.

**You have to enable (MIDI) SLAVE MODE for the PIXIE:**

Turn off the machine, hold FUNCTION AND CLEAR - while power on. (Config Mode)

press “Time” to disable the Time MODE LED - (MIDI IN SYNC Mode is on when the LED is off) ,

then press FUNCTION to exit the Config Mode.

## MIDI WIRING

in the Pixie guide is in the first picture the pin. 4-5 wrong labeled but the graphic match

validated:

![2667EC2E-476A-47CA-91DE-D54051340031-20260513-185423.heic](assets/2667EC2E-476A-47CA-91DE-D54051340031-20260513-185423.jpg)

![545BE8AF-2128-49D0-B140-9C0BFA7E4EA9-20260513-185422.heic](assets/545BE8AF-2128-49D0-B140-9C0BFA7E4EA9-20260513-185422.jpg)

### **my own VCF Resonance modification:**

the underlined lines are the value which I installed, you should use milled ic pins to make testing and replacement to your favorite sound easier

![IMG_7673.JPG](assets/IMG_7673.jpg)

**Random pics:**

![15231715_10155030146707439_669681848_o.jpg](assets/15231715_10155030146707439_669681848_o.jpg)

![IMG_2759.jpeg](assets/IMG_2759.jpeg)

![097346EA-CA11-4ACD-9289-F2536D8D12F9.jpg](assets/097346EA-CA11-4ACD-9289-F2536D8D12F9.jpg)

![IMG_2654.jpeg](assets/IMG_2654.jpeg)
