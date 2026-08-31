---
title: "TTSH Calibration guide"
space: "TTSH"
space_key: "TTSH"
type: page
created: "2016-07-11T18:45:37"
updated: "2020-07-10T18:44:09"
confluence_id: "1310771"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/TTSH/pages/1310771"
---

# TTSH Calibration guide

last update: June 2020 for 4072 Filtercard, big thanks to @Autor

> **Tipp**
>
> works best with Scope and good DMM (4,5digits with less than 1% tolerance)

> **Achtung**
>
> make sure your device works without smoke, smell, all LEDs are on, your VCO/VCF/VCA works.
>
> before you start, let the TTSH in a room with stable temperature, power on the TTSH for 30 min. before you start the calibration.
>
> make sure you have no jumper on kbd/cv pcb header (was used in TTSH rev.1 buildguide)

**Table of Content**

## Powersupply (for rev.3)

trim to excactly -15V/15V by usage of the Powersupply Multiturn trimmer, **measure between -V and 0  and +V and 0**

use a 12V - 24DC powersupply at the input.

## Ring modulator

before you start with the Ringmodulator calibrate the VCO2 Sinewave and check the function of VCO1

**Positive Null**
01) Put switch in DC position
02) Raise VCO 1 slider only
03) Monitor output with oscilloscope and adjust POS NULL for minimum output

**Negative Null**
01) Put switch in AC position
02) Raise VCO 1 slider only
03) Monitor output with oscilloscope and adjust NEG NULL for minimum output

**Gain**
01) Raise both sliders into Ring Modulator and set switch to DC
02) Adjust GAIN trimmer for 20Vpp maximum

---

## VCO 1 to 3

**V/oct adjustments**  (own Info: start with VCO1 - use the Mixer to doublecheck the same initial frequency and lowest/highest frequency to get the same values on all VCOs)
01) Monitor output with frequency counter or tuning standard
02) Depress low C and adjust frequency for 100Hz using coarse or fine tune slider
03) Depress high C and adjust 1V/OCT trimmer for 1600Hz
04) repeat 2 and 3 until C are correct

**Frequency calibrate**
01) Monitor output with oscilloscope or frequency counter
02) All FM sliders down
03) Remove keyboard CV from selected VCO
04) Put frequency slider far right (maximum)
05) Put fine tune slider – mid range
06) Adjust FREQ CAL for 8.33kHz

---

**VCO-1**
Pulse width
01) Monitor square wave output with oscilloscope and adjust SYMMETRY trimmer for 50% duty cycle.

---

**VCO-2 Wave shape adjustments****Symmetry**
01) Monitor triangle output with oscilloscope
02) Adjust the "Symmetry" trimmer for best triangle waveform (you move the waveform to an triangle - you find at the waveform a spike which must be moved to get a sharp peak/top notch

**DC offset adjust  for the Sine Wave**

01) Monitor sine wave output with oscilloscope

02) Adjust "OFFSET" trimmer so the peaks of the triangle waveform is not flat or either end - (the waveform voltage for -/+ Volt must be balanced to get the best waveform balance)

**Gain adjust**
01) Monitor sine wave output with oscilloscope
02) Adjust GAIN for 10Vpp output

Mostly this step is combined with Purity - sometimes you have to give more than 10VPP to start the bending of an triangle to an Sine Wave

**Purity adjust**
01) Adjust PURITY for best sine waveform
*It might b e necessary to readjust calibrations after performed in the order listed.*

*note: if you don\`t get a SINE wave ,  but often its just an failure from the calibration method - if you have trouble change the gain to 12-15VPP, then turn the purity trimmer)*

*but sometimes is a faulty 2N3958 the problem, mostly cheap Chinese fakes*

---

## VCF with 4012 VCF (original TTSH)

**Frequency calibration**
01) Monitor VCF output with an oscilloscope or frequency couter
02) Initial frequency slider – left
03) Fine tune slider – mid range
04) Resonance slider – right
05) All VCF inputs sliders – down
06) Disconnect or use dummy plug for KYBD CV in
07) Adjust FREQ CALIBRATE for 10Hz output

**V/oct adjust**
01) Repeat steps for frequency calibration but reconnect the CV keyboard
02) Depress low C (0 volts)
03) Adjust initial frequency slider and fine tune slider for 200Hz
04) Depress C three octaves higher and adjust 1V OCT trimmer for 1600Hz
05) Repeat step 2-4 until low C remains at 200Hz and C3 remains at 1600Hz

**Output offset**
01) Monitor VCF output with oscilloscope
02) Initial frequency, fine tune, and resonance slider – left
03) All input sliders down
04) Adjust OUTPUT OFFSET for minimum DC output. Movement of the initial frequency slider should not cause more than 1V deflection

**Gain adjust**
01) Open VCF initial frequency slider – right
02) Resonance slider – left
03) Raise VCO1 input slider and adjust GAIN for same amplitude as measure at VCO1 output

## VCF 4072

The only calibration adjustment that seems to make any difference with the 4072 filter module is Initial Frequency. When you remove the 4012 filter and install the 4072 filter, the Initial Frequency is shifted way down, so that the cutoff frequency is at sub audio range somewhere around 75% on the Coarse Frequency control. This one calibration needs to be repeated when changing between filter modules. The 1V/Oct panel trimmer is efficacious with the 4012 filter module, so should be adjusted for that unit, and should be undisturbed when swapping. The Offset and Gain trims work the same for both filters, and should also be undisturbed when changing filters.

The following procedure is written for end-user, and is simplified. Obviously a builder may have a more precise means of measurement.

This is based on the following standards:
a. Note C1 (MIDI note 24) = 32.70Hz
b. 0.00VDC on KBD CV bus produces note C1 at VCO1-3 and VCF cutoff frequency

If you have a different standard, adjust the target frequency you adjust to in step 8 accordingly.

1. Disconnect power and open the case, or unmount the panel if using the standard steel case.
2. Remove the in-use filter module, and install the alternate one.
3. Re-assemble, and power up the instrument. Let it warm up for 20 minutes.
4. Using a midi keyboard and midi to CV device, drive C5 (midi note 72), to produce +4.00V on the KBD CV bus.
5. Adjust the filter’s Coarse Frequency control to minimized, the Fine Frequency control is in the middle, and the Resonance control to maximum.
6. Disconnect any audio and CV inputs, and minimize their controls to the filter.
7. Connect the output of the filter into a guitar tuner. It may help to use the mixer section to attenuate the signal down to guitar level, which is something like .5V p-p (-20dB from the VCF output of 10V p-p).
8. Adjust the Freq. Calibrate trimmer from the front panel in the VCF to get C5/523hZ on the tuner. Getting close is probably good enough here.

---

## VCA

**Linear gain**
01) Monitor VCA output with oscilloscope
02) Patch VCO3 saw to VCA ‘VCF Input’ jack and raise audio slider fully
03) Put initial gain slider – left (minimum)
04) Raise VCA AR control slider all way
05) Depress and hold the manual start button and adjust LINEAR GAIN for 10Vpp maximum signal output

**Control rejection**
01) Repeat steps 1-3 for linear gain adjustment
02) Patch VCO2 LF sine wave (2Hz) into VCA AR control input
03) Close VCA VCF input slider
04) Adjust CONTROL REJ for minimum output

**High frequency reject**
01) No adjustment necessary

**Exponential gain**
01) Set EXP’L GAIN trimmer fully clockwise
*Experiment with exponential setting…*

---

## Internal Clock

**Init. frequency**
01) Monitor the internal clock output with an oscilloscope
02) Put rate slider at max
03) Adjust INIT trimmer so the square wave doesn’t disappear at max rate setting

**Pulse width**
01) Monitor Internal clock output with an oscilloscope
02) Put RATE slider at max
03) Adjust WIDTH trimmer for 50% duty cycle

---
