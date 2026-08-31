---
title: "Build guide"
space: "KIJIMI"
space_key: "KIJIMI"
type: page
created: "2019-06-06T08:32:18"
updated: "2022-04-10T16:31:04"
confluence_id: "1015857"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/KIJIMI/pages/1015857"
attachments: 54
---

# Build guide

Page Contents:

**That’s not an official guide.**

It’s more an best practice guide, you find infos about the firmware/software on the main page: [KIJIMI Documentation](../index.md)

1. Sourcing parts, order higher quantities to get the best price and more parts for free or for a better condition than ordering later single parts and you have spares (tactile switch, encoder, potentiometer, opamps 3340,3360)
2. Sort all parts, one carton with resistors, one for capacitors...one for mechanical parts, one for Ics/semis.
3. Sort the values like 1R-999R, 1K-9.9K, 10K-99K.... same for capacitors
4. Start with the mainboard and hardwareboard and next Breakoutboard and PSU.. so you left less plastic bags for the voices which makes things easier
5. Use lead based solder core or you get trouble with the ground pads and in case of failure or wrong part placements it’s more complicated to desolder the part.
6. Use for the voice cards a mounting frame which costs 50-250€.

> **Important**
>
> **You have to respect the Known Issues/current Error List on this page  - when you build an Kijimi, install at the beginning the Sub Osc Fix - and fill the holes of the resistors which you don't need anymore or use an edding pen and strikethrough the resistor numbers on the pcb.**

## **BOM:**

~~[KIJIMI-BOM-REV1.0.xlsx](../assets/KIJIMI-BOM-REV1.0.xlsx)~~

new BOM from July 2019 with improved Sound, i renamed the File because Roman used the same Filename as before which can confuse and ends in mistakes when you open accidentally an older file with same name.

BOM from 23.July 2019

**[KIJIMI-BOM-REV1.01\_DSLMANxlsx.xlsx](../assets/KIJIMI-BOM-REV1.01_DSLMANxlsx.xlsx)**

please add 16x 1M resistors for theSUB OSC FIX

the Difference between first (v1.02) and latest BOM (xxx\_DSLmanxlsx.) which improve the sound:

**MOUSER Basket: (imported from above xls) (updated 28.May 05:40PM GMT+1) updated see issue list 1.June.2019 this BOM doesnt match with the SUB OSC fix and addional Panned Voice Outputs (there´s a separate Mouser project for the MOD)**

[https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=6285be713e](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=6285be713e)

**the mouser project was improved for more parts** - same price, the quantity is noted as "customer note" on each bag.

## **Voicecard change - must be used in your build !**

replace R108 from 10K to 20K

replace R111, R52 from 91K to 20K

replace R38, R97 from 330K to 576K (i used a 560K plus a 20K resistor in series which was measured to 575k (1% resistors)    (only 576K when you want TL074 for IC2 and IC9 otherwise use 330k)

remove R60 , R119 (220R) → not installed 

replace IC2 and IC9 from TL064 to TL074

picture source: Facebook Luther Stevebennett

click to enlarge - this picture doesn't include the Sub OSC Fix !!!

![KJMI_pcb_scan_voice_top.jpg](assets/KJMI_pcb_scan_voice_top.jpg)

  

![IMG_7309.jpg](assets/IMG_7309.jpg)

## **VOICE BOM ssi2140 Version**

## **please note, this BOM only contains the the new ssi2140 Voicecard PCB parts**

**[KIJIMI-VOICE-BOM-REV2.0.xlsx](assets/KIJIMI-VOICE-BOM-REV2.0.xlsx)**

**[KIJIMI-VOICE-BOM-REV2.0.pdf](assets/KIJIMI-VOICE-BOM-REV2.0.pdf)**

Mouser BOM: [https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=c757799ef6](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=c757799ef6)

(without ssi2140,AS3360,AS3340 available from: [http://www.soundsemiconductor.com/buy.html](http://www.soundsemiconductor.com/buy.html)

> **Attention**
>
> you have to change on the Mainboard one resistor as described in the above KIJIMI-VOICE-BOM-REV2.
>
> this change the output Gain - the new cards are quiter than the old ssi2144 cards.
>
> C61 on the  Voicecard is 1nF film instead of C62

**![B1993A20-7A62-4CCD-B616-50703E133556.JPG](assets/B1993A20-7A62-4CCD-B616-50703E133556.jpg)

  

![KIJIMI_2040_VOICE_CARD.jpg](assets/KIJIMI_2040_VOICE_CARD.jpg)**

## **Total costs of Material:**

<details>
<summary>Mehr anzeigen</summary>

600€ plus VAT Mouser (€ incl.19% german VAT)

AS3360 100€ 

AS3340 80€

ssi2144 ICs (VCF) 55€

OLED 5€

Potentiometer - 35€

Knobs 55€

Noise IC   10€

IC Sockets 20€

XMOS Programmer 22€

metalparts 20€

EDGE card holder 10€

PCBs with vat and tax 1250€

case with vat/tax 300€

\_\_\_\_

**TOTAL around: 2563€**

</details>

**Don´t miss the Frontpanel and case from DIYHUB** [http://siddarthianinnovations.bigcartel.com/](http://siddarthianinnovations.bigcartel.com/)

> **Hinweis**
>
> please respect your local requirements/laws for a powersupply  (110V AC/ 230V AC) and
>
> doublecheck the power input jack polarity (inside +) and
>
> the diameter of 2.1mm or 2.5mm of the plug/jack  or you learn it in the hard way 😉

## **Modification**

check out [this page](../kijimi-modifications/index.md) [Kijimi Modifications](../kijimi-modifications/index.md)

## **Powersuply Warning**

don't mix the external PSU bricks or you destroy your Device.

The Kijimi use a 24V DC PSU

DDRM v1 DIY use a 12V DC PSU 

DDRM v2 DIY use a 12V DC PSU

## **Display OLED**

make sure your OLED folow this pinout  **VCC-GND-SCL-SDA**, very often shows the shop the correct pinout but deliver another type.

**AND short the pins on the display side (where the Frontpanel is) to prevent shorts to the Frontpanel.**

if you cant source the correct display  (pin) use restore legs and bend they - use cable shrink tube to protect this for shorts

##### **before you start**, drill the 4 holes of the Mainboard to 4mm - that the mounting brackets can be attached with the supplied mouser screws.

![IMG_7452.jpg](assets/IMG_7452.jpg)

 

![72235735_2447224058889144_7604308110886305792_n.jpg](assets/72235735_2447224058889144_7604308110886305792_n.jpg)

## Hardwareboard (often called Mainboard by me) and Controlboard

![IMG_6550.jpg](assets/IMG_6550.jpg)

remove the PCB production (panelizing) stripes

![IMG_6545.jpg](assets/IMG_6545.jpg)

100K resistors 

![IMG_6634.jpg](assets/IMG_6634.jpg)

all resistors (the change from the lastest BOM wasn't included here)

![IMG_6640.jpg](assets/IMG_6640.jpg)

Dont install the IC socket on the location where you find on the nearside the SMT IC !! this socket isn't needed and its easier while soldering the SMT IC.

![IMG_6707.jpg](assets/IMG_6707.jpg)

remove the panellising pcb parts from the mainboard/controlboard or it will not fit in the case later. (use a pliers and bend it carefully step by step)

![IMG_6545.jpg](assets/IMG_6545.jpg)

### Controlboard Infos

The front panel distance to the controlboard is 6mm, use a 5mm spacer and a washer or you can also use 6mm, 12mm Spacers between mainboard and Controlboard.

At this hole : **DO NOT** mount at the rearside a 12mm spacer, only use at top side a 5-6mm spacer and from rear a screw/nut (depends on what you have on hand) otherwise a 12mm spacer will short the voice card slot pins

![kEGMOmU1SqCI8i8LwRqH5w.jpg](assets/kEGMOmU1SqCI8i8LwRqH5w.jpg)

![IMG_6671.jpg](assets/IMG_6671.jpg)

## **POTENTIOMETER:**

install all potis and solder only one pin, then check the orientation of all pots in a row - maybe you have to change the alignment.. solder a groundpad and check the orientation again.

DISPLAY, make sure your pinout is correct - **VCC-GND-SCL-SDA**! otherwise bend the 2 pins as shown in the picture and use shrink tube, double check it for shorts - or your 3.3V rail will be destroyed 

dont install 5mm spacer between the display and PCB - you only need 3-4mm.. wait with the display until you have the front panel..

when you have the front panel: install all pots and all switches, put the OLED as shown in the place (dont solder it yet), put the front panel on the controlboard, fix the panel with screws,

the front panel must be in the same height as the switches or use washers/remove the washer to get the correct height. if everything is ok - solder the display at the outer pins and check the orientation again.

![cATlCSXYRKWvBn68aB6xiA.jpg](assets/cATlCSXYRKWvBn68aB6xiA.jpg)

The Software/Firmware Installation process is described on the [Mainpage](../index.md)

## **Current identified Errors/Omissions/Errata:**

| Date | Location | Identified Issue | Resolution | update |
|---|---|---|---|---|
| May 29, 2018 | BOM hw board | R119, R120, R121 not in BOm 1.02 | R119 4K7  R120 100R  R121 2K2 | BOM project updated-1June2019 |
| May2019 | OLED DISPLAY<br>**major** | Double check the OLED pinout | rin case of wrong pinout - remove 2 oled pinheader pins and use a resistor leg and cable tube shrink<br>correct is:<br>**VCC-GND-SCL-SDA** |   |
|   |   | BAT43 x2 missing D3 D4 on Harware board |   | BOM project updated-1June2019 |
| 12 Jun2019 | BOM hw board | C34 missing in BOM | 560pf mlcc RM5 |   |
| 30 July 2019 | Controlboard | dont install a Metal spacer between controlboard and mainboard in the middle of the pcb - otherwise it touch the card slot adapter pins<br>![kEGMOmU1SqCI8i8LwRqH5w.jpg](assets/kEGMOmU1SqCI8i8LwRqH5w.jpg) | use only the short 7mm spacer and a screw/nut from rear. |   |
| 30 July | Audio output | install on both locations a 2pin header<br>if you use the flat ribbon cable for the audio signal you have to bridge the pins with a jumper.<br>when you use the MTA100 headers with coax cable, dont install the jumpers !<br>Connect only at the mainboard side (MTA100 header)the ground of your shielded cable. Don’t connect the GND at the MTA100 header at the breakoutboard or you get a groundloop (more noise, risk of hum) | ![IMG_7307.jpg](assets/IMG_7307.jpg)<br>![IMG_7308.jpg](assets/IMG_7308.jpg) |   |
| 30 July 2019 | info | use a 24V Center positive Powersupply with 2Ampere or more | don't use the 12V PSU from DDRM DIY Version. |   |
| 1 Aug 2019 | **major bug** | on the PSU card is the -9V Capacitor silkscreen wrong, this was happen on my PSU card and the capacitor leaked, thx to Ando for the picture. | install the positive pin of C8 on the left side (as shown in the bottom picture)<br>![67449772_2230211047077377_2789159123596345344_o.jpg](assets/67449772_2230211047077377_2789159123596345344_o.jpg) | reported to Roman and Bob |
| 15 Aug. 2019 | mainboard | mounting holes for brackets do not fit with the Mouser screws. carefully drill a bigger hole as shown here: (marked) only this 4 holes | ![IMG_7452.jpg](assets/IMG_7452.jpg) |   |
| 15 Aug | PSU | the fuse must be around 1.2Ampere,<br>the current of the kijimi on 24V DC is 950mA |   |   |
| August 2019<br>**Major BUG** | Voices | improve the sound (from Roman.F - the developer) | **Voicecard:**<br>replace R108 from 10K to 20K<br>replace R111, R52 from 91K to 20K<br>replace R38, R97 from 330K to 576K (i used a 560K plus a 20K resistor in series which was measured to 575k (1% resistors)  (only 576K when you want TL074 for IC2 and IC9 otherwise use 330k)<br>remove R60 , R119 (220R) → not installed<br>replace IC2 and IC9 from TL064 to TL074 |   |
| January 2020<br>**Major BUG** | Voices | fix the Subosc. Problem (glitches and artifacts) | Here is the SUBOSC fix Janne and I worked out. Details below:<br>**the addional parts are not included in the BOM (16x 1M resistor)**<br>(click to enlarge)<br>![SUBOSC_fix2019.jpg](assets/SUBOSC_fix2019.jpg)<br>1. Remove these components: Q1, Q2, R126, R139<br>2. Add two 1M resistors as shown (to PCB solder side)<br>3. Add two jumper wires as shown (to PCB solder side)<br>4. R131, R133, R146, and R149 are not needed. If you already have them installed, no need to remove them (they don't do anything). If you are starting to build, don't install them.<br>NOTES:<br>This fix is for DIY REV1 KIJIMI only. Prebuilt Kijimi does not have this issue.<br>You can omit all these highlighted parts and test your voice card without the SUBOSC feature. Everything else should still work.<br>When modifying your voice card, do the modification on one card first and then test for any glitches (there shouldn't be any). Then modify the others.<br>Please report back if you have any issues.<br>Thanks to Janne for the hard work in helping to test and develop this fix.<br>Technically this mod disconnects the saw waveform and routes the pulse waveform instead into the 4013 divider. The 1M resistors enhance the rise and fall time of the pulse waveform. The original problem was caused by transient noise on the saw waveform that triggered the 4013 divider. | thanks to Janne and Ando |
| December2021 |   | LED orientation for the mouser BOM LEDs | ![kijimi-led.jpg](assets/kijimi-led.jpg) |   |

## **Bootloader:**

**(the Firmware is on a other page to minimize confusion by rebuild Owners) : [Manuals and Firmware](../manuals-and-firmware/index.md)**

**you need both files: (****boot loader and the "DIY" Firmware)**

**[Kijimi1.1.0.xe](../assets/Kijimi1.1.0.xe)**

**[sst25vf080](../assets/sst25vf080)**

Download for (OSX) [XMOS TIME COMPOSER](https://www.xmos.com/file/xtimecomposer-community_14-macosx-installer?ver=latest) and copy it to you Application folder.

Install JAVA 6 from:

[https://support.apple.com/kb/DL1572?locale=de\_DE](https://support.apple.com/kb/DL1572?locale=de_DE)

turn the power off , install the xmas programmer in the IDC Socket, connect a USB cable to the xmas programmer, then:

**OSX how-to**

1. Open terminal

2. Type cd /Applications/XMOS\_xTIMEcomposer\_Community\_14.3.3/

3. Press enter

4. Type 

```
./SetEnv.command
```

5. Press enter

6. Type cd /Path/to/fw/folder

7. Press enter

8. type    

```
xflash Kijimi1.1.0.xe --spi-spec sst25vf080
```

(power on Kijimi yet)

9. Press enter

10. wait - after 30seconds or one minute your terminal starts with same infos - ignore the first message (Warning: F0398 Factory...) see on bottom the picture.

 message, after further seconds the terminal shows you some memory addresses which are written, and then: **finished successfully, on the KIJIMI the OLED Display must show you some graphics (PNL mode etc)**

![IMG_7305.jpg](assets/IMG_7305.jpg)

Here´s  a Video from me about the Firmware Installation:

[https://www.youtube.com/watch?v=hZtAMaiQXBA&t=24s](https://www.youtube.com/watch?v=hZtAMaiQXBA&t=24s)

## **Microsoft Windows 7/10 howto intall the "bootloader/Firmware": (credits to [Konrad K'sadhu Zientara](https://www.facebook.com/konrad.zientara?fref=gs&__tn__=%2CdC-R-R&eid=ARCyWsA8Yc6HZlx1ro-xrloBmUmK2-lqj0r_AeIdhdL8zlRLJDxb4coo4R89tmSqa514hmEcvYxW9LM0&hc_ref=ARSimMS2Gt9GXB1GqShzj0_E7IgROGUQIpSsUDGXm3Tb7HLUlOpcxUV6N-HCC3MbeOY&dti=369660250197513&hc_location=group))**

In order to do that, one needs the XMOS's xTIMEcomposer utility bundle and Java 6 32bit.

steps: (after you have installed the xmos timecomposer on your PC)

1 - turn Kijimi power OFF

2 - plug the programmer into Kijimi

3 - connect the programmer to the PC via USB

4 - open a windows powershell (console/terminal) and type:

```
xTIMEcomposer
```

in the command prompt (this runs SetEnv.bin in the command line terminal. If You experience problems go to the xmos folder to locate the file and run it. &gt;see Image)

the setenv command sets the Environment for the Java process/applications (the path of your Java and more)

5 - go to the folder, where the Kijimi firmware and flash setup files are located. (with the cd command like:  cd C:\\Users\\patrick\\Downloads\\kijimi) or as shown in the bottom screenshot

6 - type in the powershell:

```
xflash Kijimi1.1.0.xe --spi-spec sst25vf080
```

7 - power ON the Kijimi

8 - the programmer will be disconnected for a while by the program

9 - the programmer will be reconnected and more LEDs will light up.

10 - there will be 2 error messages displayed in the terminal (F03098 and F03148 &gt;see image) - ignore it

11 - adresses will show in terminal as being written into

12 - "finished successfully"

13 - the Kijimi will display it's menu on the OLED display

14 - turn OFF the Kijimi

15 - disconnect the programmer

DONE

Now the Kijimi is programmed and ready for calibration.

![win7_flashkijimi.jpg](assets/win7_flashkijimi.jpg)

## **Calibration**

everything is available in the software menu

1. Potentiometer Calibration :  **Important**: turn all pots to the right side (max) then only turn the center detent knobs to middle position for the center detent calibration. for the second step turn all knobs to right (max) position
2. set the Voicecard amount to the value what you have installed
3. set the Midi Settings to MPE or CP etc. (Channel pressure for standard keyboards)
4. calibrate OSC 1 ..2 ..3...
5. calibrate VCF

![IMG_6545.jpg](assets/IMG_6545.jpg)

![IMG_6550.jpg](assets/IMG_6550.jpg)

![kEGMOmU1SqCI8i8LwRqH5w.jpg](assets/kEGMOmU1SqCI8i8LwRqH5w.jpg)

![67449772_2230211047077377_2789159123596345344_o.jpg](assets/67449772_2230211047077377_2789159123596345344_o.jpg)

![A8C3C228-ABF8-4737-A4C4-280FFAC358A7.jpg](assets/A8C3C228-ABF8-4737-A4C4-280FFAC358A7.jpg)

![IMG_6633.jpg](assets/IMG_6633.jpg)

![IMG_6634.jpg](assets/IMG_6634.jpg)

![IMG_6640.jpg](assets/IMG_6640.jpg)

![IMG_6641.jpg](assets/IMG_6641.jpg)

![IMG_6646.jpg](assets/IMG_6646.jpg)

![IMG_6647.jpg](assets/IMG_6647.jpg)

![IMG_6670.jpg](assets/IMG_6670.jpg)

![IMG_6671.jpg](assets/IMG_6671.jpg)

![IMG_6691.jpg](assets/IMG_6691.jpg)

![IMG_6692.jpg](assets/IMG_6692.jpg)

![IMG_6693.jpg](assets/IMG_6693.jpg)

![IMG_6694.jpg](assets/IMG_6694.jpg)

![IMG_6707.jpg](assets/IMG_6707.jpg)

![IMG_6985.jpg](assets/IMG_6985.jpg)

![IMG_7289.jpg](assets/IMG_7289.jpg)

![IMG_7291.jpg](assets/IMG_7291.jpg)

![IMG_7292.jpg](assets/IMG_7292.jpg)

![IMG_7304.jpg](assets/IMG_7304.jpg)

![IMG_7307.jpg](assets/IMG_7307.jpg)

![IMG_7308.jpg](assets/IMG_7308.jpg)

![IMG_7309.jpg](assets/IMG_7309.jpg)

![IMG_7332.jpg](assets/IMG_7332.jpg)

![IMG_7367.jpg](assets/IMG_7367.jpg)

![IMG_7452.jpg](assets/IMG_7452.jpg)

![IMG_7453.jpg](assets/IMG_7453.jpg)

![IMG_7454.jpg](assets/IMG_7454.jpg)

![IMG_7455.jpg](assets/IMG_7455.jpg)

![IMG_7456.jpg](assets/IMG_7456.jpg)

![IMG_7457.jpg](assets/IMG_7457.jpg)

![IMG_7459.jpg](assets/IMG_7459.jpg)

![IMG_7460.jpg](assets/IMG_7460.jpg)

![IMG_7461.jpg](assets/IMG_7461.jpg)

![IMG_7462.jpg](assets/IMG_7462.jpg)

![IMG_7463.jpg](assets/IMG_7463.jpg)

![IMG_7467.jpg](assets/IMG_7467.jpg)

![cATlCSXYRKWvBn68aB6xiA.jpg](assets/cATlCSXYRKWvBn68aB6xiA.jpg)

![72235735_2447224058889144_7604308110886305792_n.jpg](assets/72235735_2447224058889144_7604308110886305792_n.jpg)

![SUBOSC_fix2019.jpg](assets/SUBOSC_fix2019.jpg)

![image.jpeg](assets/image.jpeg)

![image.png](assets/image.png)

![KJMI_pcb_scan_voice_top.jpg](assets/KJMI_pcb_scan_voice_top.jpg)

![IMG_7305.jpg](assets/IMG_7305.jpg)

![win7_flashkijimi.jpg](assets/win7_flashkijimi.jpg)

![B1993A20-7A62-4CCD-B616-50703E133556.JPG](assets/B1993A20-7A62-4CCD-B616-50703E133556.jpg)

![KIJIMI_2040_VOICE_CARD.jpg](assets/KIJIMI_2040_VOICE_CARD.jpg)

![IMG_9254.jpg](assets/IMG_9254.jpg)

![kijimi-led.jpg](assets/kijimi-led.jpg)
