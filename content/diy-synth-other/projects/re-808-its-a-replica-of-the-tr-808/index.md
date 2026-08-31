---
title: "RE-808 its a replica of the TR-808"
space: "DIY Synth other"
space_key: "DSO"
type: page
created: "2022-05-08T14:49:43"
updated: "2026-05-19T20:28:06"
confluence_id: "1147673"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147673"
attachments: 92
---

# RE-808 its a replica of the TR-808

> **Project**
>
> #### Projecttitel: RE-808
>
> #### Status: `done`
>
> #### Startdate: 11/2021
>
> #### Duedate: 12/2022
>
> #### Last Update: 05/2026
>
> #### Manufacture link: [https://shop.re-303.com/product/re-808-bundle-3rd-run-advance-order/](https://shop.re-303.com/product/re-808-bundle-3rd-run-advance-order/)

I built in the last 15 years a lot of Yoctos (808), Nava (909) and a lot of RE-303/606/808/909. Maybe you find here some useful tips and tricks for your build.    

![808-2.jpeg](assets/808-2.jpeg)

![808.jpeg](assets/808.jpeg)

After the RE-303, RE-606, RE-909 we have the RE-808 replica to build.

its an replica, which means 99.9% of everything is a replica - the pcbs, the case, the parts.

the only difference are replacement tactile switch of the sequencer.

but you can repair your TR-808 with the RE-808 parts.

## **Infos and groups:**

[https://www.facebook.com/groups/1095915370823319](https://www.facebook.com/groups/1095915370823319)

## **BOM:**

PCBs and some parts are available from the RE-303 shop

Cases and side panels are available from [Kumptronics](http://www.kumptronics.com/)

[**BOM.RE808.Release v1.0.xlsx**](assets/BOM.RE808.Release-v1.0.xlsx)

in case you need a ba662 clone, I have this for sale populated and PCB only version

[https://www.diysynth.de/advanced\_search\_result.php?categories\_id=0&keywords=ba662&inc\_subcat=1](https://www.diysynth.de/advanced_search_result.php?categories_id=0&keywords=ba662&inc_subcat=1)

about the nichicon capacitors: there's no difference in sound, by the usage of other HQ capacitors, or greenies from taydas.

There's no voodoo with the capacitors, **more important is the usage of 5% Filmcaps and 1% metalfilm resistors** to avoid trouble with tuning issues and you have less thermal noise.

Start/Stop cover and Tap cover for the switches  can be made byself with 3D rosin print, or ask me - I left few spares.

please read this:   [https://shop.re-303.com/files/files/Making\_your\_Start-Stop\_and\_Tap\_buttons.pdf](https://shop.re-303.com/files/files/Making_your_Start-Stop_and_Tap_buttons.pdf)

Standoffs/Spacers (not in the BOM - but supplied with the RE-808 case)

7x  8mm FF Hex Spacer for the mainboard thru switchboard
4x  10mm FF Hex Spacer for the PSU
5x  16.4mm FF Hex Spacer for the mainboard
3x  18mm Hex Spacer for the bottom case part
2x  8mm MF Hex Spacer 8mm w/ 6mm Screw for the EMV shield plate

## **Buildguide:**(uploaded 08.May.2022 by DSL-man)

[**RE-808 Build Guide v1.0.pdf**](assets/RE-808-Build-Guide-v1.0.pdf)

[**RE-808 Wiring Guide v1.1.xlsx**](assets/RE-808-Wiring-Guide-v1.1.xlsx)

[**RE-808 Switchboard Assembling v1.0.pdf**](assets/RE-808-Switchboard-Assembling-v1.0.pdf)

[**Alps Switches Modding Guide v1.0.pdf**](assets/Alps-Switches-Modding-Guide-v1.0.pdf)

[**RE-808-MYC-manual-midicable.pdf**](assets/RE-808-MYC-manual-midicable.pdf)

**RE-808 Case assembling guide.**[**RE-808 assembly guide.pdf**](assets/RE-808-assembly-guide.pdf)

## **Placement guide:**

#### [**RE-808\_Component\_Placement\_Guide\_v1.0.0.pdf**](assets/RE-808_Component_Placement_Guide_v1.0.0.pdf)

## **Firmware Installation**

##### **warning: before you do this make a break and double check all parts, especially IC orientation & Pixie orientation, the wiring - especially power and sync switch and sync jacks.**

use Sysex Liberian to upload the files

settings in SysEx tool:

![Bildschirmfoto 2023-06-02 um 07.18.43.png](assets/Bildschirmfoto-2023-06-02-um-07.18.43.png)

1. turn on and send[808.sysxex](assets/tr808.syx)with sysex librian tool (step1 led is blinking) (when not - check your MIDI wiring)
2. now send the  the [boot loader 1.4.3](assets/bootloader.1.4.3.syx) with sysex librian tool (step led is blinking)
3. turn off the machine
4. in boot loader mode (hold step1 while start) upload the [REEMU 1.4.3 sysex](assets/reemu.1.4.3.syx) (normally step1-9 show the progress while uploading), when it doesn't show the nightrider mode by pushing step1 while starting the machine: check your wiring of the sync switch,

##### [https://github.com/sunflowr/recpu/releases/download/v1.4.3/recpu\_manual.1.4.3.pdf](https://github.com/sunflowr/recpu/releases/download/v1.4.3/recpu_manual.1.4.3.pdf)

## **Issue List**

| **ID** | **Issue** | **Fix** | **date** | **fixed version** |
|---|---|---|---|---|
| 1 | CPU mounting | As you can see you also need to do a jumper wire between the solder point marked A on the pixie cpu and pin 10 (!WE pin) of \*any\* of IC 7,8,9 or 10 (they’re all connected to the same signal)<br>**Please pay attention to :**<br>YOU HAVE TO USE SOCKETS or headers, as shown in my pictures, I used milled Pins on milled IC Sockets or standard headers and standard Pinheaders.<br>Its “Forbidden” to install the CPU without a removable system, thank me later in case your Pixie is defect.. and you destroy your pcb by trying to remove the CPU..<br>![signal-2026-02-26-221956.jpg](assets/signal-2026-02-26-221956.jpg)<br>![IMG_1457.JPG](assets/IMG_1457.jpg)<br>\* **This is on the back of the 808  as shown on bottom**<br>the jumper wire can be soldered directly as it’s just one wire, I use a pin header and patch cable here mainly during development as I can easily remove the cpu without having to desolder anything<br>**as the cpu is upside down**, make sure you connect the midi wires the correct way! (good Din jacks have numbers printed on the black plastic) which should match with the printed numbers on the pixie CPU)<br>**pin 1 and 42 is unused**and can be left unconnected (pin 1 is the hole with a square pad)<br>![257506294_10220039780292309_2623807660755818637_n.jpg](assets/257506294_10220039780292309_2623807660755818637_n.jpg)<br>![257802400_10220039779892299_503743482874567736_n.jpg](assets/257802400_10220039779892299_503743482874567736_n.jpg)<br>![256916612_10220039780132305_4100561509048569219_n.jpg](assets/256916612_10220039780132305_4100561509048569219_n.jpg)<br>![256889540_10220039780732320_2626204296816752405_n.jpg](assets/256889540_10220039780732320_2626204296816752405_n.jpg)<br>![IMG_1459.jpeg](assets/IMG_1459.jpeg) | 01/2022 |   |
| 2 | PSU | Do not fit the DC jack on the PSU circuit board.<br>Its not used and it is not wired correctly.<br>use a cable and connect it to the pcb directly | 01/2022 |   |
| 3 | Tactiles /caps install | heres a tip about the installation of the tactile caps:<br>![270219367_1948924405268244_4913522328705377384_n.jpg](assets/270219367_1948924405268244_4913522328705377384_n.jpg)<br>**i prefer this process:**<br>![IMG_6103.jpeg](assets/IMG_6103.jpeg) | 01/2022 |   |
| 4 | MIDI WIRING | ![IMG_6101.jpeg](assets/IMG_6101.jpeg)<br>credits to a FB User.. | 11/2022 |   |
| 5 | Silkscreen wrong | ![IMG_6102.jpeg](assets/IMG_6102.jpeg) | 11/2022 |   |
| 6 | Mainboard resistors - handclap | ![IMG_6104.jpeg](assets/IMG_6104.jpeg)<br>![IMG_6106.jpeg](assets/IMG_6106.jpeg)<br>in case you have the trimmer on solder side (recommended)<br>Add the R200 (10K) as shown in the left picture above at the 2 red dots.<br>![IMG_8433.jpg](assets/IMG_8433.jpg) | 11/2022 |   |
| 7 | guide /tip | **for the voice board:**<br>- first install all 1/8watt resistors on bottom of the pcb where later is the Switchboard PCB,  **R1-9 are 1/8w**or the switchboard do not fit<br>- use MLCC caps there and no IC socket for IC1<br>**in case you have a solderframe:**<br>install the flat Trannys and IC sockets before you install the other parts<br>**for the Mainboard**<br>use for the noise transistor and muting trannys**ic socket pins**to swap/change the trannys later (select on test)<br>install good trimmers from there rearside(solder side) instead cheap trimmers from component side - in result a better and easier calibration is possible | 11/2022 |   |
| 8 | Transistors - sequencer failure | use sockets for the muting transistors.<br>some users reported issues in combination with the pixie CPU, boot/start problems.<br>the muting Transistors affect this  - you can remove this. | 1.Dec.2022 |   |
| 9 | Power Pinout | ![IMG_6773.jpg](assets/IMG_6773.jpg)<br>![IMG_6772.jpeg](assets/IMG_6772.jpeg)<br>credits by Martin.J.K  - Thank you | 02.Jan.2023 |   |
| 10 | general conclusion of above IDs | install good trimmers on back side (solder side) - for easier calibration<br>install the BA662 clone on solder side - in this was you can use a socket<br>install the muting JFETS and noise Transitor on solder side for easier swapping<br>install R333 on solder side to give you the opportunity to replace this with a trimmer (50k) to change the handclap sound.. | 02.Jan.2023 |   |
| 11 | bugfix | install a jumper as shown to get your 808 working as designed or the START/STOP wont work (check the Issue ID 23 too)<br>![BLWeU-BA.jpeg](assets/BLWeU-BA.jpeg) | 03. Jan.2023 |   |
| 12 | capacitor on Sync jack | install a 10nF polyester cap or bipolar electrolyte cap at the sync jack or on the pcb<br>![Bildschirmfoto 2023-01-03 um 22.11.12.png](assets/Bildschirmfoto-2023-01-03-um-22.11.12.png) |   |   |
| 13 | clock calibration fix | remove C203 on mainboard (39nF) or your clock can't be calibrated, (that's happen by using modern ICs)<br>in case you can't reach 120hz at the trimmer end, install a 2M2 resistor in parallel on R43<br>(check the Issue ID 23 too in case of failure) | 04.Jan.2023 |   |
| 14 | calibration/mod | ![IMG_6739.jpeg](assets/IMG_6739.jpeg)<br>Hi tom noise level = R273<br>Middle tom noise level = R245<br>Low Tom noise level = R216<br>**BassDrum Endless/Extended Decay**-- replaced R170 (470k) with 370k resistor in series with a 100k potentiometer. then i set the potentiometer to the 'sweet spot', where the extra decay sounded best to me, and measured the resistance of the 370k resistor plus the resistance of the potentiometer setting. on my Yocto, 445k was the nicest value for self-oscillating/extreme decay<br>![](https://www.e-licktronic.com/forum/images/smilies/icon_e_wink.gif)<br>. then i removed the 370k resistor and potentiometer from R170, and finally replaced R170 with an SPDT switch that selects between a 470k resistor (the original value/normal setting) and 445k (the 'sweet spot' for extra decay i measured, using a few resistors to achieve the 445k value).<br>**BassDrum Tuning**-- replaced R165 (47k) with SPDT switch that selects between original value (47k) and a 100k potentiometer (audio/log preferably)<br>**BassDrum Tuning Envelope**-- replaced R166 (6.8k) with SPDT switch that selects between original value (6.8k) and a 5k potentiometer in series with a 2k resistor. (in combination with the tuning mod, this mod enables some nice extra-punchy bass drums!)<br>**Clap Noise Offset**-- replaced the 10k trimpot in the clap section with 10k potentiometer..<br>**Closed Hihat filter**-- replaced R147\* (2.7k) with an SPDT switch that selects between original value (2.7k) and a 10k potentiometer in series with a 1k resistor<br>**Open Hihat filter** -- replaced R153\* (2.7k) with an SPDT switch that selects between original value (2.7k) and a 10k potentiometer in series with a 1k resistor<br>source: [https://www.e-licktronic.com/forum/viewtopic.php?f=18&t=143](https://www.e-licktronic.com/forum/viewtopic.php?f=18&t=143) | 02.April 2023 |   |
| 15 | wiring | found on FB - bad quality of the picture...<br>you find on bottom pictures of my builds which can be more helpful - especially for the sync switch wiring<br>**new 07/2023 - HD quality :**[**808-wiring.png**](assets/808-wiring.png)<br>![808-wiring.png](assets/808-wiring.png) |   |   |
| 16 | wiring | **new 07/2023 cable length and color code !**<br>[808 wire sizes.pdf](assets/808-wire-sizes.pdf) |   |   |
| 17 | MIDI connection MOD | the 3D printed part is available in [my shop](https://www.diysynth.de/spezial-re-808-parts/re-808-midi-anschluss-3d-druck.html) [https://www.diysynth.de/spezial-re-808-parts/re-808-midi-anschluss-3d-druck.html](https://www.diysynth.de/spezial-re-808-parts/re-808-midi-anschluss-3d-druck.html)<br>or print it myself (Resin preferred)<br>just use 2 screws to mount this at the typenumber plate holes at the rear and drill a small for the MIDI cables.<br>![IMG_7513.jpeg](assets/IMG_7513.jpeg)<br>![IMG_7514.jpeg](assets/IMG_7514.jpeg)<br>![IMG_53B972AA28C5-1.jpeg](assets/IMG_53B972AA28C5-1.jpeg)<br>![IMG_A0CEE6750F2A-1.jpeg](assets/IMG_A0CEE6750F2A-1.jpeg) |   |   |
| 18 | 3D Print tool rotary switch | this tool make things easier.<br>just drop the rotary switch inside and its easy to saw the switch, but you should need file the length 1-2mm shorter (depends on your knobs and if you want the knob as close as possible against the case)<br>**available in my shop :**<br>[https://www.diysynth.de/spezial-re-808-parts/re808-schaltersaegehilfe-3druck-teil.html](https://www.diysynth.de/spezial-re-808-parts/re808-schaltersaegehilfe-3druck-teil.html)<br>![IMG_7635.jpg](assets/IMG_7635.jpg)<br>![IMG_7636.jpg](assets/IMG_7636.jpg) |   |   |
| 19 | Tip Rotary Switches | for much easier rotary switch assembling, use this knowledge **PLUS** the [ALPS assembly guide](assets/Alps-Switches-Modding-Guide-v1.0.pdf), my infos are a additional tip how to remove and bend the tabs.<br>**you need in total 3 rotary switches 2x 6Positions, 1x12positions endless all 3 switches must have a knurled shaft** and the length must be<br>since we can't buy this from stock we have two buy in total 6 rotary switches and make from this 3 rotary switches.<br>you can follow the alps rotary switch guide which is attached at top of this page but you should read my improved tips how to remove/bend the switch..<br>**Background:**<br>we dont need the upper part of the **D shaft** switches (we need knurled shaft for the 808 knobs)<br>and we don't need the lower part of the mouser/digikey knurled switches.<br>that's how you prepare the switches:<br>**for the D shaft switches**you can bend the tabs at the bottom for removal as close you can - because **we dont need the upper part** - put the upper part (metal) in the trash bin, we only need the base(bottom part incl. blue plastic)<br>![IMG_7691.jpeg](assets/IMG_7691.jpeg)<br>**for the assembled knurled switches**you can cut the pcb on bottom to remove the bottom part without bending the tabs, after you have removed the pcb - you can much easier bend the tabs !!! we only need the top metal part of this switch.<br>![IMG_7690.jpeg](assets/IMG_7690.jpeg)<br>![IMG_7702.jpeg](assets/IMG_7702.jpeg)<br>after you proceed the other steps as described in the [alps rotary switch guide](assets/Alps-Switches-Modding-Guide-v1.0.pdf) , you have to bend back the pins which hold the bottom part and upper part.<br>I used here 2 tools and a hammer.<br>in first step I punched with the smaller hex. and the hammer and later with the bigger hex. and a hammer.<br>![IMG_7705.jpeg](assets/IMG_7705.jpeg)<br>![IMG_7706.jpeg](assets/IMG_7706.jpeg)<br>![IMG_7707.jpeg](assets/IMG_7707.jpeg)<br>In case your switches wobbles, you can add 2K glue on the sides of the switches (metal to pcb) but doublecheck that no glue comes in contact with the blue/green plastic part.<br>furthermore, you have to use a nut and washer to mount the switches on the case |   |   |
| 20 | recommend Mods for Clap and Snare | remove R333 and install a 50K trimmer from solder side - this adds the opportunity of changing the Clap frequency/bandpass<br>Install a header for the Noise Tranny of the PCB Solderside - you can try different Noise transistors of your choice (less white noise at the snare, gain stage between handclap and Snare, a loud Handclap is wrong, too much white noise at the snare is wrong)<br>forget the 133mV AC measurement of the noise Tranny - the important thing is the spectrum of the noise.<br>use a transistor tester (peak tech for example to get the correct polarity or use the datatsheets)<br>**Furthermore: (highly recommend)**<br>you change c51 from 0.47uF to 0.68uF (or up to 1uF) to get more reverb/room on the Snare.<br>use milled pins on the solderside for testing the value.<br>Only do this mod when you are lucky with the snare sound except the reverb part is too small (personal choice)<br>its not recommend to do this mod until you have found a good noise transistor otherwise you have too many variables.<br>![IMG_8956.jpeg](assets/IMG_8956.jpeg) | 02.April 2023 |   |
| 21 | Cowbell bugfixing | in case your cowbell is out of the trimmer range while calibration 800hz/540hz install in parallel to R44 a 10K resistor and the same for R55 (add a 10K in parallel)<br>since we connect a scope there, let enough space to clip the probe there.<br>![IMG_8974.jpg](assets/IMG_8974.jpg)<br>![IMG_8975.jpg](assets/IMG_8975.jpg)<br>in case you have failures in the cowbell, here's a good page:<br>visit [http://frisnit.com/roland-tr-808-cowbell-rebuild/](http://frisnit.com/roland-tr-808-cowbell-rebuild/)<br>![IMG_8413.PNG](assets/IMG_8413.png)<br>![IMG_8414.jpeg](assets/IMG_8414.jpeg) | 02.April 2023 |   |
| 22 | Grounding /wiring | Connect the "Chassis GND" from the safety PSU directly into the Jacks A "Chassis GND". Do not wire it thru the chassis.<br>Connect Jacks A to Jacks B.<br>![IMG_2647.PNG](assets/IMG_2647.png) | 02.April 2023 |   |
| 23 | Cymbal Mod | source:<br>[https://www.modwiggler.com/forum/viewtopic.php?t=264016](https://www.modwiggler.com/forum/viewtopic.php?t=264016)<br>**change:**The modification involves changing C40 (in the middle branch next to the 33k resistor) from 1µF to 100nF<br>Raising C41 gives a longer decay- (**not tested by me**)<br>**Technical paper:**<br>[tr\_808\_cymbal\_a\_physically\_informed\_circuit\_bendable\_digital.pdf](assets/tr_808_cymbal_a_physically_informed_circuit_bendable_digital.pdf) | 04.April 2023 |   |
| 24 | general tip | mount the DIN jack from inside of the Case - don´t install the DIN socket thru the metal case, in case of trouble shooting its much easier with the wiring - otherwise you have to disconnect/desolder some cables. | 06.April 2023 |   |
| 25 | general | Here are few pictures, how I installed LED resistors on sockets, to change easily the brightness of the LEDs.<br>recommended: 680R instead of 68R for the step led brightness and 1k or more for the 4 other LEDs.<br>I used in one of my builds flathat LEDs for the variable/pattern LEDs with 1K resistor and there's no issue that other leds are still on/glow.<br>![IMG_8958.jpeg](assets/IMG_8958.jpeg) | 2023 |   |
| 26 | wiring | few users requested some pictures of the wiring..<br>![IMG_9316.jpeg](assets/IMG_9316.jpeg)<br>![IMG_9321.jpeg](assets/IMG_9321.jpeg)<br>![IMG_9309.jpeg](assets/IMG_9309.jpeg)<br>![IMG_9319.jpeg](assets/IMG_9319.jpeg)<br>![IMG_9318.jpeg](assets/IMG_9318.jpeg)<br>![IMG_9347.jpeg](assets/IMG_9347.jpeg)<br>![IMG_9320.jpeg](assets/IMG_9320.jpeg) | 2023 |   |
| 27 | MIDI | **Midi In Mode: (Sync)**<br>1.turn the Pattern write switch to "Manual Play"<br>2. hold the Pattern Clear Pushbutton and Press Step16 - the Step16 LED must be off<br>3. turn the Pattern write switch to "1 st PART"<br>4. move the Sync Switch on the rear side of the 808 to Input<br>5. now the 808 reacts on incoming Midi Sync Signals<br>**MIDI Out Mode (Sync)**<br>by default the 808 sends MIDI Out Sync Signals.<br>otherwise check this:<br>The Rear Sync Switch must be to Out<br>1. turn the Pattern write switch to "Manual Play"<br>2. hold the Pattern Clear Pushbutton  - the Step16 LED must be ON<br>in case its still not working, check the MIDI OUT wiring (MIDI In Wiring must be ok, since you flashed the Pixie CPU in this way) | 2023 |   |
| 28 | Switchboard | the Switchboard is green, which can be seen thru the slots of the Stepswitches in some circumstances.<br>**on the original TR-808 is a felt cover installed on all parts (Instrument switches, basic variation switch, I/F Variation )**<br>**For the RE-808 switchboard is a solution to use black paint/spray for the pcb, or use a Edding pen or black tape, or nail paint.**<br>![IMG_6442.jpeg](assets/IMG_6442.jpeg)<br>![IMG_6443.jpeg](assets/IMG_6443.jpeg) | 2024 |   |
| 29 | General | **DO NOT INSTALL the Knobs before everything is 100% working and calibrated. The Knobs at the 3 Rotary switches  can't be easily removed.**<br>Do not installed the Side panels and don't close the case too. | 10/2024 |   |
| 30 | General | in case everything is working and calibrated, use nuts at the  screws which is at both bare steel rails (which holds the pcbs) Furthermore use lock washers (check that no trace is too close there) at the pcbs and use Screwpaint, to avoid loose screws over the years or while transportation. | 10/2024 |   |
| 31 | PIXIE memory failure | in few pixie CPUs is the memory corrupt - defect pattern - random notes is one symptom ,<br>look in my [RE-303 page](../re-303-not-a-further-clone/index.md) - issue tracker to find out more | 01/2025 |   |
| 32 | BD sound “fat” improvement | make sure your R169 47K resistor is at minimum 47K<br>the most 47K resistors are less than 47k - 46.5k for example, that's not enough to get a punchy Decay. (or use a 100K Trimmer and dial to 47K or 48K) | 04/2026 |   |
| 33 | Troubleshooting Clock - Start Stop | in case that your Clock is only 10hz and you still have added the 2.2M resistor in parallel on R43, you have to check this:<br>the Sync Jack have a ground connector thru a 10nF cap. Its absolute important that the 10nF cap get a ground connection, or the clock speed is wrong.<br>Next one: the Start/Stop jack and the fill-in jack use a switched Pin - that means, without an attached 6.3mm plug, the signals flows to ground. That means its absolutely important that you connect the cables to the PCB while testing or troubleshooting -  or the sequencer won't start from the internal clock, but you can still use MIDI Sync and start/stop over midi.<br>![Bildschirmfoto 2026-05-19 um 22.17.30-20260519-201844.png](assets/Bildschirmfoto-2026-05-19-um-22.17.30-20260519-201844.png) |   |   |

**Gallery from above Pictures**

![Bildschirmfoto 2026-05-19 um 22.17.30-20260519-201844.png](assets/Bildschirmfoto-2026-05-19-um-22.17.30-20260519-201844.png)

![256916612_10220039780132305_4100561509048569219_n.jpg](assets/256916612_10220039780132305_4100561509048569219_n.jpg)

![256889540_10220039780732320_2626204296816752405_n.jpg](assets/256889540_10220039780732320_2626204296816752405_n.jpg)

![277704086_10158873135074422_3842388984428524569_n.jpg](assets/277704086_10158873135074422_3842388984428524569_n.jpg)

![257506294_10220039780292309_2623807660755818637_n.jpg](assets/257506294_10220039780292309_2623807660755818637_n.jpg)

![257802400_10220039779892299_503743482874567736_n.jpg](assets/257802400_10220039779892299_503743482874567736_n.jpg)

![272629301_10159608849224431_310854521237969341_n.jpg](assets/272629301_10159608849224431_310854521237969341_n.jpg)

![270219367_1948924405268244_4913522328705377384_n.jpg](assets/270219367_1948924405268244_4913522328705377384_n.jpg)

![IMG_6101.jpeg](assets/IMG_6101.jpeg)

![IMG_6104.jpeg](assets/IMG_6104.jpeg)

![IMG_6102.jpeg](assets/IMG_6102.jpeg)

![IMG_6106.png](assets/IMG_6106.png)

![IMG_6105.jpeg](assets/IMG_6105.jpeg)

![IMG_6103.jpeg](assets/IMG_6103.jpeg)

![IMG_6106.jpeg](assets/IMG_6106.jpeg)

![IMG_6773.jpg](assets/IMG_6773.jpg)

![IMG_6772.jpeg](assets/IMG_6772.jpeg)

![BLWeU-BA.jpeg](assets/BLWeU-BA.jpeg)

![Bildschirmfoto 2023-01-03 um 22.11.12.png](assets/Bildschirmfoto-2023-01-03-um-22.11.12.png)

![IMG_6739.jpeg](assets/IMG_6739.jpeg)

![Fix-HC.jpg](assets/Fix-HC.jpg)

![IMG_7067.jpg](assets/IMG_7067.jpg)

![IMG_7513.jpeg](assets/IMG_7513.jpeg)

![IMG_7514.jpeg](assets/IMG_7514.jpeg)

![IMG_7635.jpg](assets/IMG_7635.jpg)

![IMG_7636.jpg](assets/IMG_7636.jpg)

![IMG_A0CEE6750F2A-1.jpeg](assets/IMG_A0CEE6750F2A-1.jpeg)

![IMG_53B972AA28C5-1.jpeg](assets/IMG_53B972AA28C5-1.jpeg)

![IMG_7702.jpeg](assets/IMG_7702.jpeg)

![IMG_7707.jpeg](assets/IMG_7707.jpeg)

![IMG_7706.jpeg](assets/IMG_7706.jpeg)

![IMG_7705.jpeg](assets/IMG_7705.jpeg)

![IMG_7691.jpeg](assets/IMG_7691.jpeg)

![IMG_7690.jpeg](assets/IMG_7690.jpeg)

![IMG_7876.PNG](assets/IMG_7876.png)

![IMG_8413.PNG](assets/IMG_8413.png)

![IMG_8414.jpeg](assets/IMG_8414.jpeg)

![IMG_8433.jpg](assets/IMG_8433.jpg)

![IMG_8434.jpg](assets/IMG_8434.jpg)

![D658FEAC-2724-491D-91CE-8BF72623DFDF.jpg](assets/D658FEAC-2724-491D-91CE-8BF72623DFDF.jpg)

![IMG_8434.jpeg](assets/IMG_8434.jpeg)

![IMG_8584.JPG](assets/IMG_8584.jpg)

![IMG_8585.jpeg](assets/IMG_8585.jpeg)

![IMG_8603.jpeg](assets/IMG_8603.jpeg)

![IMG_8596.PNG](assets/IMG_8596.png)

![IMG_8630.jpeg](assets/IMG_8630.jpeg)

![IMG_8668.jpeg](assets/IMG_8668.jpeg)

![adde758a-c904-4e8f-97da-178880d492b5.jpg](assets/adde758a-c904-4e8f-97da-178880d492b5.jpg)

![9b04135e-f054-4740-8e70-c37e28c4f57a.jpg](assets/9b04135e-f054-4740-8e70-c37e28c4f57a.jpg)

![728cc426-bd1f-4881-8572-a310d60bb114.jpg](assets/728cc426-bd1f-4881-8572-a310d60bb114.jpg)

![3e4d63fb-1213-47d1-b122-c79bfa706c47.jpg](assets/3e4d63fb-1213-47d1-b122-c79bfa706c47.jpg)

![IMG_8956.jpeg](assets/IMG_8956.jpeg)

![IMG_8958.jpeg](assets/IMG_8958.jpeg)

![IMG_8974.jpg](assets/IMG_8974.jpg)

![IMG_8975.jpg](assets/IMG_8975.jpg)

![IMG_9318.jpeg](assets/IMG_9318.jpeg)

![IMG_9347.jpeg](assets/IMG_9347.jpeg)

![IMG_9320.jpeg](assets/IMG_9320.jpeg)

![Bildschirmfoto 2023-06-02 um 07.18.43.png](assets/Bildschirmfoto-2023-06-02-um-07.18.43.png)

![IMG_9317.jpeg](assets/IMG_9317.jpeg)

![IMG_9316.jpeg](assets/IMG_9316.jpeg)

![IMG_9321.jpeg](assets/IMG_9321.jpeg)

![IMG_9308.jpeg](assets/IMG_9308.jpeg)

![IMG_9309.jpeg](assets/IMG_9309.jpeg)

![IMG_9319.jpeg](assets/IMG_9319.jpeg)

![808-wiring.png](assets/808-wiring.png)

![IMG_2647.PNG](assets/IMG_2647.png)

![808.jpeg](assets/808.jpeg)

![808-2.jpeg](assets/808-2.jpeg)

![IMG_6443.jpeg](assets/IMG_6443.jpeg)

![IMG_6442.jpeg](assets/IMG_6442.jpeg)

![IMG_1457.JPG](assets/IMG_1457.jpg)

![signal-2026-02-26-221956.jpg](assets/signal-2026-02-26-221956.jpg)

![IMG_1459.jpeg](assets/IMG_1459.jpeg)
