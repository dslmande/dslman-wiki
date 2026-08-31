---
title: "SynthiA building tips"
space: "DIY Synth other"
space_key: "DSO"
type: page
created: "2014-10-06T13:47:32"
updated: "2014-10-06T14:29:05"
confluence_id: "1147802"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147802"
---

# SynthiA building tips

> **Project**
>
> ### Projecttitel:
>
> ### Status: `hier ändern`
>
> ### Startdate:
>
> ### Duedate:
>
> ### Manufacture link:

Explanation of errors and difficult to obtain parts. **Compiled 4th Sept 2012**

1) Small signal germanium diode – long obsolete – use 1N34A or similar.

2) 2.5μf 64V Electrolytic capacitor – long obsolete – use 2.2μf 25V-100V.

3) 80μf obsolete – use 100μf.

4) 16μf obsolete – use 15μf.

5) 5K Potentiometers – obsolete - use 4K7.

6) 2000μf – obsolete – use 2200μf.

7) 200μf – obsolete – use 220μf.

8) D1 marked 1N4148 wrong type – use 1N4002.

9) C15 and R32 are drawn the wrong way round.

10) 9V1 ZD9 added on –9V Op-Amp pin 7 (positive supply).

11) Obsolete Japanese Twin Spring Reverb Tank use Accutronics 1BC2D1B.

12) C8 shown connected to MFC6070 Pin 6, should be connected to Pin 1 and 3.

13) Ring Modulator Transistors Q34 and Q35 **shown as 2C746, use two BC169C’s,** closely matched for Gain if possible (but modern transistor tend to be made with Laser technology, thus the gains are pretty well matched)

14) It’s not necessary to use a**2C746 or equivalent on Oscillator 3, use two BC169C’s**epoxy them together for thermal stability. This is because Osc. 3 tracks at a different voltage to Osc. 1 and Osc. 2, and is used mostly as a LFO (Low Frequency Oscillator).

15) Pay special attention to screening I/O particularly to the Reverb flying leads, DO NOT USE REVERB TANK WHICH HAVE ONE SIDE OF THE PICKUP WIRING EARTHED TO THE TANK, this will blow the MFC6070 chip. If you do have the correct reverb tank the reverb tank chassis should be earthed and even better a metal lid should be made to completely enclose the reverb tank, this helps with nearby RF radiation i.e. Radio Mics etc, etc.

16) Connect Q1 and Q6 to a flying lead, and mount the transistors on a big heat sink, not forgetting to isolate the transistor bodies from the metal of the heat sink, use generous amounts of Silicon Heat conducting grease between the Mica sheet and the heat sink, if you don’t isolate the transistors from the heat sink, you are connecting the Q1 and Q6 collectors together, have a look at the schematic, and see what that would do to the circuit. It’ll blow the fuse at least, and blow the transistors and several other components in the power supply if you’re very unlucky, so don’t do it. The wiring to the T1 connector is as follows CBE-slot-EBC. Look up the Pin out info for the TIP3055, the pinout can vary depending on the type you buy, so be careful.

18) I’m probably wasting my time adding this, but DO check with a DVM set on resistance, across 0V +12V and –9V points on the wiring and on the boards prior to plugging them in and turning on the power.

19) I also do a visual check on the colour coding on the resistors, just to make sure I’ve got the rough values soldered into the right places, this I do by checking the 3rd colour band (usually the multiplier), and ignoring the 1st and 2nd bands.

20) Well that all I can think of at the moment, good luck and happy cloning.

Q81 = 1K tempco 3500ppm
