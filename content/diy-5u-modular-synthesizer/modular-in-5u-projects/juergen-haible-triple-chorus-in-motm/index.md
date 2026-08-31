---
title: "Juergen Haible Triple Chorus in MOTM"
space: "DIY 5U Modular Synthesizer"
space_key: "MAIN"
type: page
created: "2014-02-28T14:00:53"
updated: "2019-07-31T13:54:02"
confluence_id: "1705493"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/MAIN/pages/1705493"
attachments: 22
---

# Juergen Haible Triple Chorus in MOTM

> **Project**
>
> ### Projecttitel: Juergen Haible Triple Chorus in MOTM
>
> ### Status: `finished one`
>
> ### Startdate: 28.04.2014
>
> ### Duedate: 01 December 2014 /the last build was 02/2019
>
> ### Manufacture link: [http://jhaible.com/legacy/triple\_chorus/triple\_chorus.html](http://www.jhaible.com/triple_chorus/triple_chorus.html)

further links: [http://www.dragonflyalley.com/jHTripleChorusConstruction.htm](http://www.dragonflyalley.com/jHTripleChorusConstruction.htm)

backup here:[Dragonfly Alley MOTM Synthesizer Jurgen Haible \_Triple Chorus\_ Construction.pdf](assets/Dragonfly-Alley-MOTM-Synthesizer-Jurgen-Haible-_Triple-Chorus_-Construction.pdf)

**BOM:**

The Equalizer potentiometers are 10k linear each (3 in total).
You may want to add an input level potentiometer: 10k log ... 50k log are good values.
Input / output jacks depending on what signals you want to bring out.
Mode and bypass switch can be realized with a rotary switch or with a set of toggle switches - more about this later.

List:

[jh\_triple\_chorus\_bom.pdf](assets/jh_triple_chorus_bom.pdf)

Reichelt shoppingbasket

[http://www.reichelt.de/?ACTION=20;AWKID=41401;PROVID=2084](http://www.reichelt.de/?ACTION=20;AWKID=41401;PROVID=2084)

> **Tipp**
>
> u1 = 100nF ,  u1 near CD4011  is MLCC c0g or WIMA mks (polyester)

[https://www.youtube.com/watch?v=YmRSArFFm5k](https://www.youtube.com/watch?v=YmRSArFFm5k)

**Building Tip from Juergen.H**

The PCB board - power on-board. 
 It all fits onto a 160mm x 100mm board. It contains a power supply (less transformer and primary fuse). You only have to connect 18V AC from a transformer. (And you must be qualified to handle the mains voltage - fuses, insulation, safety aspects. If in doubt, don't wire the mains voltage, but use an insulated 18V AC wallwart instead. Mains voltage can be lethal.)
Here's a (preliminary) component overlay:
(click on the image for a full size version.)

Alternative +/-15V supply (MOTM and Synthesizers.com, etc.) 
 I've also included the footprints of MOTM and .COM power connectors, if you want to run the board directly from 15V, without a transformer of its own.
I've placed the footprint for the connectors beneath the (secondary) fuse, because you never need both at the same time.
When connecting to 15V DC, you must omit a lot of the power supply components, too.
Click on the following links for the alternative component overlay for 15V DC: [MOTM version](http://www.jhaible.com/triple_chorus/jh_triple_chorus_overlay_motm.pdf),   [Synthesizers.com (.COM) version](http://www.jhaible.com/triple_chorus/jh_triple_chorus_overlay_dotcom.pdf).
By the way: The whole circuit only needs the -15V part of the MOTM and .COM system; the +15V pins of the connectors are unconnected.
The audio signals are centered to 0V nevertheless, of course, due to AC coupling of inputs and outputs.
Signals are weaker than your usual modular system. Input can be attenuated with a potentiometer. Output is roughly "Line level" and can go directly into a mixing desk or sound card.

[jh\_triple\_chorus\_overlay.pdf](assets/jh_triple_chorus_overlay.pdf)

[jh\_triple\_chorus\_overlay.pdf](assets/jh_triple_chorus_overlay.pdf)

[jh\_triple\_chorus\_connections\_1p2t\_switches.pdf](assets/jh_triple_chorus_connections_1p2t_switches.pdf)

[jh\_triple\_chorus\_connections\_1p2t\_switches.pdf](assets/jh_triple_chorus_connections_1p2t_switches.pdf)

[jh\_triple\_chorus\_sch\_page1.pdf](assets/jh_triple_chorus_sch_page1.pdf)

[jh\_triple\_chorus\_sch\_page1.pdf](assets/jh_triple_chorus_sch_page1.pdf)

[jh\_triple\_chorus\_sch\_page2.pdf](assets/jh_triple_chorus_sch_page2.pdf)

[jh\_triple\_chorus\_sch\_page2.pdf](assets/jh_triple_chorus_sch_page2.pdf)

## Background from J.Haible website

 The lush Sound of the Solina (TM) Ensemble is created by 3 BBD delay lines that are modulated in a unique way:
There are two 3-phase modulation generators, one running at slow speed ("Chorus"), and one running at high speed ("Vibrato").

We'll focus on one of the modulation generators first, "Chorus": the slow one.
"3-Phase" means that the modulation generator has 3 outputs, each of which's phase is roughly 120 deg apart from the previous output.
Let's call them "0 deg", "120 deg" and 240 deg" - it's easy to see that, with 360 deg describing a full circle, the three modulation outputs a modulation generator are equally distributed around a circle. They are routed to the CV inputs of the 3 BBD's clock VCOs. Modulation of a BBD line causes a pitch shift similar to the Doppler effect of  a moving sound source, so with the 3 BBD lines modulated by the 3-phase control signals, a sonic image of  3 sound sources that are moving along the same circle, with equal distance to one another along the outline of the circle, is created.

Actually, each BBD clock VCO is controlled not by a single modulation generator, but by a combination of the slow and the fast generator.
BBD1 sees a CV that is combined from the Chorus generator's "0 deg" output and the Vibrato generator's "0 deg" output.
BBD2 sees Chorus "120 deg" and Vibrato "120 deg".
BBD3 sees Chorus "240deg" and Vibrato "240 deg".

This method creates the famous "Solina" sound, which was so sucessfull that it has been emulated by other manufacturers.
Of these, I have studied two very closely: The Crumar Performer, and the Dr. Boehm Phasing Rotor 78. I've also taken a look at the Korg Polysix's Ensemble mode.

Classic Implementation  

The original Solina did not use a 3-phase oscillator at all. Not even a sine wave oscillator, for that matter.
There's a Square Wave oscillator which is then turned into an approximated sine wave by heavy filtering, creating the "0 deg" signal of the "Chorus" part.
This is then fed into a 1-pole low pass filter with a gain 1.83 for very low frequencies. The brilliant idea behind this: For one specific input frequency, you get unity gain and the desired 120 degree phase shift. You can adjust the frequency of the square wave generator for the "0 deg " and "120 deg" signals to have the same amplitude, and you'll have the right frequency and the right phase shift automatically.
The "240 deg"  signal  is not created with another filter: It's derived from the "0 deg" and "120 deg" signal with a simple inverting adder stage. (The wonders of vector maths: The vector sum of a balanced 3-phase system is always zero.)
The "Vibrato" path even needs one stage less: There's the square wave oscillator with filtering for the "0 deg" signal, a LPF for the "120 deg signal".
These two signals are added to the "Chorus" signal chain at the respective stages, so the inverting adder of the "Chorus" takes care of the vector maths to create the "240 deg" signal of the "Vibrato" as well. (Even though there is no point in the circuit where you could measure the individual "240 deg" signals separately!)

This was pretty brilliant at a time when saving an opamp stage in a circuit made a difference. :)
From today's point of view, it's the tiny flaws of the original method that may make it interesing: Whatever adjustment of the Vibrato and Chorus speed potentiometers, it is not possible to create a perfect level balance and equal phase distribution for both, the fast and the slow part of the modulation.
My conclusion is that if there is a perceivable difference in the sound of a Solina, compared to a Boehm or the Polysix (other than EQ-ing and SNR), this may have to do with these special  modulation waveforms.
The Boehm, for instance, has a very direct and precise method of directly creating 3-phase signals.

My Emulation  

When emulating the behaviour of some Vintage instrument, my design goal is always to be as precise as possible. But don't get fooled: If part of that vintage sound is due to certain imperfections, all the precision of the emulation must be directed to re-create that specific - once "non-perfect", but now your reference! - solution.
This doesn't mean to just copy the original and to use the same components. While this certainly works in most cases, it's rarely an option if you want to give others the oportunity to to build your circuit as well. I have a set of TCA 350's in my drawer, but I'd rather go for BBDs that are still available (even when production has long stopped), the TDA1022. And I've omitted a lot of the more bulky components in the Solina's modulation generators, but I've painstakingly taken care to get the same waveforms, with all their "flaws", as in the original. (A circuit simulator is a gift from heaven for that kind of work.)

I've also noticed that a diode in the Solina's BBD Clock VCOs is slightly bending the combined modulation waveform, before it really hits the VCO core. As my VCO implementation is different - CMOS gates like the Boehm, instead of  transistors - that kind of  waveform bending  is also implemented in a different way, to get the same result without introducing en extra 21V supply rail. I've made it adjustable with a trimmer, so you can set that effect to your taste, Solina Way or Dr. Boehm Way.

Filtering in general, and the Crumar Performer in particular 
 In the Solina, the signal as it comes from the tone generation and string sound shaping, runs thru a second order 12kHz filter before it goes into the BBDs. This acts as an anti-aliasing filter, as well as adding to the sound shaping a bit.
With longer BBD lines (TDA1022 instead of TCA350), the clock frequency can be higher, this allowing for a wider bandwidth without increased aliasing.
So I've implemented a 16kHz anti-aliasing filter, plus a 12kHz filter, to be able to choose a broadband sound vs. a slightly darker sound.
A third option was inspired by the Crumar Performer: It has a very specialized 3-Band EQ that is very effective on string sounds. With my Performer, I get very convincing, yet very different, string sounds with a 0-10-0 setting and with a 10-0-10 setting (low-mid-high).
I've included this wonderful EQ in my emulation.

First Step- sockets.. for 3 triple Chorus.

## Build tips:

**calibration:**

U6: Pin 1 6hz

U6 PIN 7 0,6HZ  (YOU NEED A DSO to measure this slow value with 1s/ and 100mV, typically analog scopes only offer 200mS)

use CD4011UBE or try different vendors

![triple_chorus.jpg](assets/triple_chorus.jpg)

![20140802_231421.jpg](assets/20140802_231421.jpg)

![20140809_231913.jpg](assets/20140809_231913.jpg)

![20140809_231920.jpg](assets/20140809_231920.jpg)

![20140809_231928.jpg](assets/20140809_231928.jpg)

![20140809_231938.jpg](assets/20140809_231938.jpg)

![20140809_231950.jpg](assets/20140809_231950.jpg)

![20140809_231958.jpg](assets/20140809_231958.jpg)

![20140809_232016.jpg](assets/20140809_232016.jpg)

![20140809_232026.jpg](assets/20140809_232026.jpg)

![20140813_220054.jpg](assets/20140813_220054.jpg)

![20140813_234218.jpg](assets/20140813_234218.jpg)

![20140813_234224.jpg](assets/20140813_234224.jpg)

![20140902_234342.jpg](assets/20140902_234342.jpg)

![IMG_20140903_222447.jpg](assets/IMG_20140903_222447.jpg)

![20140726_233830.jpg](assets/20140726_233830.jpg)
