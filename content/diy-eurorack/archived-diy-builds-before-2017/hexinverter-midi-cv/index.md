---
title: "Hexinverter MIDI-CV"
space: "DIY Eurorack"
space_key: "CHECKMATE"
type: page
created: "2017-11-21T08:43:50"
updated: "2017-11-21T08:45:52"
confluence_id: "688636"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/CHECKMATE/pages/688636"
attachments: 1
---

# Hexinverter MIDI-CV

> **Project**
>
> ### Projecttitel:Hexinverter MIDI-CV
>
> ### Status: `hier ändern`
>
> ### Startdate: 21 Nov. 2017
>
> ### Duedate:
>
> ### Manufacture link: [http://www.hexinverter.net/midi2cv](http://www.hexinverter.net/midi2cv)

**BOM:**

[MIDI2CV\_v1.0\_BOM.xlsx](assets/MIDI2CV_v1.0_BOM.xlsx)

|   |   |   |   |
|---|---|---|---|
| **Part** | **Qty** | **Designators** | **Note/s** |
|   |   |   |   |
| **Base Parts (all formats need these parts)** |   |   |   |
|   |   |   |   |
| CA3140 Precision Operational Amplifier | 4 | IC1, IC2, IC3, IC4 | Mouser: 968-CA3140EZ -- DO NOT GET CA3140A! |
| 6N137 Optocoupler | 1 | IC9 | Mouser: 757-6N137F |
| PIC16F88 Microcontroller w/ MIDI2CV firmware | 1 | IC6 | Included pre-programmed with PCB/kit from [hexinverter.net](http://hexinverter.net) |
| MCP4822 dual 12b DAC | 2 | IC7, IC8 | Mouser: 579-MCP4822-E/P |
| 78L05 5V regulator | 1 | IC5 | Mouser: 512-LM78L05ACZXA |
| The use of IC sockets for all integrated circuits is HIGHLY recommended. |   |   |   |
|   |   |   |   |
| 2N3904 NPN Transistor | 4 | Q1, Q2, Q3, Q4 |   |
|   |   |   |   |
| 1N4148 small signal diode | 5 | D1, D2, D3, D4, D5 | 1N914 or any other small signal diode should work fine as well |
| 5mm LED | 5 | LED.S, LED1, LED2, LED3, LED4 | I recommend diffused LEDs. |
|   |   |   |   |
| .1uF capacitor | 6 | C3, C4, C5, C6, C7, C8 | 5mm lead spacing |
| 47uF electrolytic capacitor | 2 | C1, C2 | 2.5mm lead spacing, 6.3mm diameter |
|   |   |   |   |
| 220R resistor | 5 | R1, R22, R26, R31, R36 | 1/4W, 1% metal film |
| 470R resistor | 6 | R5, R8, R11, R14, R16, R17 | 1/4W, 1% metal film |
| 1k resistor | 5 | R2, R6, R9, R12, R15 | 1/4W, 1% metal film |
| 4.7k resistor | 8 | R20, R21, R25, R29, R30, R34, R35, R39 | 1/4W, 1% metal film |
| 10k resistor | 3 | R3, R18, R19 | 1/4W, 1% metal film |
| 33k resistor | 4 | R4, R7, R10, R13 | 1/4W, 1% metal film |
| 130k resistor | 4 | R24, R28, R33, R38 | 1/4W, 1% metal film |
| 200k resistor | 4 | R23, R27, R32, R37 | 1/4W, 1% metal film |
|   |   |   |   |
| 10k cermet 12 turn trim pot (straight lead pattern) | 4 | P1, P3, P5, P7 | Mouser: 858-67WR10KLF |
| 22k (or 20k) cermet 12 turn trim pot (straight lead pattern) | 4 | P2, P4, P6, P8 | Mouser: 858-67WR20KLF |
|   |   |   |   |
| Panel mount MIDI connector (5 pin DIN) | 1 |   | Mouser: 568-NYS325 |
| M3 machine screw and nut for MIDI connector | 2 |   |   |
|   |   |   |   |
| M3 machine screws (M3x35mm) | 4 |   | For connecting the boards together |
| 12mm PCB spacers | 8 |   | For connecting the boards together |
|   |   |   |   |
| 40pin male .1" breakaway header | 2 |   | For connecting the PCBs together -- broken into appropriate sections |
| 40pin female .1" breakaway header | 2 |   | NOTE: not in Mouser cart. Find these somewhere else! |
|   |   |   |   |
| MIDI2CV PCB Set | 1 | N/A | [http://www.hexinverter.net](http://www.hexinverter.net/) |
|   |   |   |   |
| **Eurorack Specific Control Board Parts (included in full eurorack kits)** |   |   |   |
|   |   |   |   |
|   |   |   |   |
| PCB Mount ON-OFF-ON toggle switch | 1 | SW.MODE | Mouser: 108-0044-EVX |
| LED PCB spacer \[OPTIONAL!\] | 5 |   | Mouser: 593-STD240B |
| 3.5mm vertical mount jacks | 9 | CV1, CV2, CV3, CV4, GATE1, GATE2, GATE3, GATE4, SYNC | [http://erthenvar.com/store/eurodiy/35hardware/jack35mmv](http://erthenvar.com/store/eurodiy/35hardware/jack35mmv) |
| Eurorack power cable | 1 |   | [http://erthenvar.com/store/eurodiy/power/cable1016](http://erthenvar.com/store/eurodiy/power/cable1016) |
| Eurorack power connector | 1 | Power |   |
|   |   |   |   |
| **Stuff you will need ONLY if not building eurorack:** |   |   |   |
|   |   |   |   |
| Assorted Panel Wire (only needed if not building eurorack) | N/A | N/A |   |
| Power connector | 1 | Power | MTA-156 |
| PCB Mount ON-OFF-ON toggle switch (panel mount) | 1 | SW.MODE |   |
| Jacks | 9 | CV1, CV2, CV3, CV4, GATE1, GATE2, GATE3, GATE4, SYNC | To match your format |
