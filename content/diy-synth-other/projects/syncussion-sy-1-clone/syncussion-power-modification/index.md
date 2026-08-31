---
title: "Syncussion Power Modification"
space: "DIY Synth other"
space_key: "DSO"
type: page
created: "2018-11-03T21:14:29"
updated: "2024-09-16T05:24:25"
confluence_id: "1147404"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147404"
attachments: 19
---

# Syncussion Power Modification

## I offer a pcb on diysynth.de to change the onboard -8V power to a hum free solution for the **THC SY-1 (all Versions)**

## The pcb was designed with the help of Simon Cox (SY-1M psycox CEO).

BOM: (or order an assembled Version from diysynth.de)

| **Amount** | **Part** | **Source** | **Mouser** | **tme.eu** |
|---|---|---|---|---|
| 1 | pcb | diysynth.de |   |   |
| 1 | LT1054 SOIC 8 |   | check the datasheets for voltage operation !<br>the input voltage is from your wandwart powersupply like 9-12V DC<br>[https://www.mouser.de/ProductDetail/Analog-Devices-Linear-Technology/LT1054CS8PBF?qs=sGAEpiMZZMtUqDgmOWBjgEMyKnxEDNWS0swAkuNbdYQ%3d](https://www.mouser.de/ProductDetail/Analog-Devices-Linear-Technology/LT1054CS8PBF?qs=sGAEpiMZZMtUqDgmOWBjgEMyKnxEDNWS0swAkuNbdYQ%3d) | LT1054CS8-SMD ✅ |
| 1 | LM7908 |   | [https://www.mouser.de/ProductDetail/ON-Semiconductor-Fairchild/LM7908CT?qs=%2fha2pyFadujt3%2f9kcI1ojRvjBqETND0G1EFAI2FtFq8%3d](https://www.mouser.de/ProductDetail/ON-Semiconductor-Fairchild/LM7908CT?qs=%2fha2pyFadujt3%2f9kcI1ojRvjBqETND0G1EFAI2FtFq8%3d) | [https://www.tme.eu/de/details/lm7908ct/ungeregelte-spannungsstabilisatoren/on-semiconductor-fairchild/](https://www.tme.eu/de/details/lm7908ct/ungeregelte-spannungsstabilisatoren/on-semiconductor-fairchild/) ✅ |
| 2 | 10uF tantal capacitor |   | [https://www.mouser.co.uk/ProductDetail/Vishay-Sprague/293D106X9025D2TE3?qs=sGAEpiMZZMuEN2agSAc2ppeu9zLjpAvsaEU2jkMDoCM%3d](https://www.mouser.co.uk/ProductDetail/Vishay-Sprague/293D106X9025D2TE3?qs=sGAEpiMZZMuEN2agSAc2ppeu9zLjpAvsaEU2jkMDoCM%3d) | 293D106X9025D2TE3 ✅ |
| 1 | 10pf capacitor<br>SMT 0805 0603 |   | [https://www.mouser.co.uk/ProductDetail/Wurth-Electronics/885012008019?qs=sGAEpiMZZMs0AnBnWHyRQEGbLOF2VP1iqcmVcmnwX7UxaJ2jp2TLLg%3d%3d](https://www.mouser.co.uk/ProductDetail/Wurth-Electronics/885012008019?qs=sGAEpiMZZMs0AnBnWHyRQEGbLOF2VP1iqcmVcmnwX7UxaJ2jp2TLLg%3d%3d) | CL21C100JBANNNC ✅ |
| 1 | 5mm metal spacer or a long M3 screw with washer and 2-3 M3 nuts |   |   | TFM-M3/5 plus 3mm washer and nut ✅ |

## **Build guide**

**INFO: I´m not responsible for your work or result, you need SMT soldering skills**

**PCB Assembly:**

> **Achtung**
>
> make sure your LT1054 is this version (LT1054CS):
>
> [https://www.mouser.de/ProductDetail/Analog-Devices-Linear-Technology/LT1054CS8PBF?qs=sGAEpiMZZMtUqDgmOWBjgEMyKnxEDNWS0swAkuNbdYQ](https://www.mouser.de/ProductDetail/Analog-Devices-Linear-Technology/LT1054CS8PBF?qs=sGAEpiMZZMtUqDgmOWBjgEMyKnxEDNWS0swAkuNbdYQ%3d)
>
> and not the "LT1054L" version.

1. **solder the LT1054 on the pcb**, double check the pinout !! for my LT1054 (from TME.eu) is the pinout as shown on bottom pictures, i haven´t checked the mouser version pinout.
   i prefer to add a bit of soldercore on one pad, this gives you a easier placement of the IC.
  for the other pads use a kester flux pen for a better and easier soldering.
  ![IMG_3579.JPG](assets/IMG_3579.jpg)
  ![IMG_3580.JPG](assets/IMG_3580.jpg)
  ![IMG_3581.JPG](assets/IMG_3581.jpg)
  ![IMG_3582.JPG](assets/IMG_3582.jpg)
2. solder the tantal capacitors
  apply on one pad on each tantal capacitor pad, solder core.
  place the part on in correct orientation on the pads (see bottom picture in case you dont know which polarity is used)
  ![IMG_3584.JPG](assets/IMG_3584.jpg)
  ![IMG_3585.JPG](assets/IMG_3585.jpg)
  ![IMG_3586.JPG](assets/IMG_3586.jpg)
3. solder the non polarity 10 pf capactitor on the pcb, start with one pad as described above
4. turn the pcb
5. bend the LM7908 pins to place it the shown orientation
  ![IMG_3587.JPG](assets/IMG_3587.jpg)
6. solder all pins and check with a magnifier all pins
7. clean the pcb with isoprop
  ![IMG_3588.JPG](assets/IMG_3588.jpg)

## Prepare your THC SY-1

1. **disconnect power and wait few minutes too uncharge the capacitors. (or move the powerswitch to on without powercord connected to the device, this unload the capacitor too)**
2. **remove the screws and knob, slidercaps from the case**
3. **open the device**
4. **remove the metal distance bolts/spacer**
5. **remove the controlboard pcb**
6. **remove all parts as shown on my picture:**
  ![IMG_3590.JPG](assets/IMG_3590.jpg)
7. **prepare  3 short cables, each 7cm is fine - you can shorten it later**
  ![IMG_3595.JPG](assets/IMG_3595.jpg)
8. **solder the "yellow cable" to the 1R resistor pad hole as shown:**
9. ![IMG_3597.JPG](assets/IMG_3597.jpg)
  ![IMG_3599.JPG](assets/IMG_3599.jpg)
  ![IMG_3600.JPG](assets/IMG_3600.jpg)
  ![IMG_3602.JPG](assets/IMG_3602.jpg)
  ![IMG_3601.JPG](assets/IMG_3601.jpg)
10. Solder the white cable to the IC pad as shown:
11. Solder the black cable as shown on the IC pad
12. ![IMG_3598.JPG](assets/IMG_3598.jpg)
13. mount the 5mm "metalspacer" or use a long screw with nuts between the pcbs to mount it as shown:
14. ![IMG_3601.JPG](assets/IMG_3601.jpg)
  ![IMG_3603.JPG](assets/IMG_3603.jpg)
  ![IMG_3602.JPG](assets/IMG_3602.jpg)
  ![IMG_3604.JPG](assets/IMG_3604.jpg)
15. Technical description: (yellow is connected on left side when shown from component side, black is ground and connected to pad (IC-PIN)2 or 5 when shown from component side, white ic connected to pin 7 (when shown from componet side)
  white is the new -8Volt output
  yellow is the 12V output from the syncussion which is connected to our new pcb LT1054 input.
