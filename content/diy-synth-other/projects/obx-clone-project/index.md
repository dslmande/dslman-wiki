---
title: "Obx clone Project"
space: "DIY Synth other"
space_key: "DSO"
type: page
created: "2013-11-06T10:27:22"
updated: "2025-02-25T15:42:03"
confluence_id: "1147160"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147160"
---

# Obx clone Project

> **Project OBX Clone**
>
> ### OBX CLONE 4Voice
>
> ### `Status` : stopped
>
> ### Startdate: 15.10.2013
>
> ### Duedate: 01.03.2014
>
> ### Manufacture link:[http://www.bild-schall.com/product/digi-eins](http://www.bild-schall.com/product/digi-eins)[http://www.cs80.com/crowbx/](http://www.cs80.com/crowbx/)
>
> #### Projectdescription: Planning and build a 4Voice OBX Clone in 5U format and one addionaly voicecard for replacement

## ***This build was stopped***

***pcb sodering was outsourced, this part failed - more than 150hours spends - Return on invest failed.***

***at last: voice cards dont work correct - some wrong caps and resistors, ic placements***

***please doublecheck BOM and read all muffwiggler postings about known issues..***

### SUBPAGES & GALLERY:

*COPY from cs.80.com:*

### Construction Hints

Fair warning: altogther there are about 3,000 components in a 4-voice crOwBX which includes the electronic components, hardware (screws, etc.) jacks, wiring--what have you. It took me 3 weeks of evenings soldering and physical assembly to build the rev2. Not trying to scare anyone, but it is important to understand the scope of the build from the outset.

That being said, linked here are files for making the crOwBX voice card and host board. Note: I do not make flashy web sites: I am an electrical engineer, not a web monkey. ;)

For all boards my usual build order is:
 1) Install all SMT parts. (0.1uF caps, two 1K tempco resistors on voice boards)
 2) Check V+ to GND, V- to GND and +5V to GND (host board) to be certain there are no power rail shorts.
 2) Install all resistors and diodes
 3) Install voltage regulators and aluminum capacitors. Observe capacitor mounting guildlines in the parts lists.
 4) Apply +/-19V to the power connector with clip leads, verify the regulated voltages are present at their proper values. Optionally check each IC position for the correct voltages on the expected supply pads.
 5) Install trimmer potentiometers.
 6) Install remaining through-hole capacitors.
 7) Install transistors. Pay attention to J112 FET orientation notes in the parts lists.
 8) Install ICs. Be aware not all ICs orient in the same direction. Recommend socket for the PIC. Optionally socket LM13600s and 4051/4052/4053s.
 9) Install Molex headers and connectors. Be careful to align these Molex parts as best as possible with respect to the silkscreen.
 10) Host board: install 9mm potentiomters.

The host board switches, if using my .fpd panel, need to be dropped into their positions on the board but not yet soldered. The panel is then placed over the switches and each switch is nudged until it seats into its drilled hole. This part is somewhat tricky as there are 17 switches to deal with. When properly seated, all the switches (with a lock washer and lip washer between the switch and panel) can then have a panel nut placed on the bushing but do not tighten them fully until the alignment of each switch in its solder pads is adjusted. I like to choose two switches at opposing corners, such as the LFO wave select and mute, line them up and solder them in then work with the remaining switches. It will take a while.

### Powersupply Modification:

The crOwBX requires a +/-19VDC power supply as the boards use local voltage regulators to obtain +/-15V and +5V for the host board. The Power One HAA15-0.8-A linear power supply, which is well-suited to operating the traditional +/-15V modular setup, can be modified to provide +/-19V by simply soldering a 10K 1% resistor across R20 and another 10K 1% resistor across R28 on the power supply board, as shown. The trimmers R21 and R26 are then adjusted such that +19.00V and -19.00V are observed on the DC output pins with respect to common. Be careful not to wire this power supply to +/-15V hardware!

The 4-voice crOwBX draws 420mA at +19V and 380mA at -19V, well within the load range (600mA per rail) of the modified HAA15-0.8-A.
