---
title: "Behringer B2600 calibration and VCF Modification"
space: "DIY Synth other"
space_key: "DSO"
type: page
created: "2020-12-24T21:39:13"
updated: "2021-11-21T15:53:28"
confluence_id: "1147534"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147534"
attachments: 9
---

# Behringer B2600 calibration and VCF Modification

(the pictures are copyright by me - Patrick Joericke, ask me if you want a agreement)

Also read the [TTSH Calibration](../../../ttsh/ttsh-calibration-guide/index.md)guide or ask me for support.

**Triangle** , the original settings from the factory was totally wrong  - symmetry(Spike)

![IMG_0591.jpg](assets/IMG_0591.jpg)

**Solution:**

use a scope and check your waveform and correct this by turning the trimmer TRI Symmetry

![IMG_0588.jpeg](assets/IMG_0588.jpeg)

**Thats not a Sine wave !**- wrong settings from factory

![IMG_0594.jpg](assets/IMG_0594.jpg)

**Solution:**

Purity - bends the TRI to a Sine wave - after this check the voltage to 10VPP (adjust the gain)

![IMG_0586.jpeg](assets/IMG_0586.jpeg)

  

![IMG_0595.jpeg](assets/IMG_0595.jpeg)

![IMG_0587.jpeg](assets/IMG_0587.jpeg)

**Filter Frequency, the Filter closed at 100hz instead of less 10hz**

**Solution:**

Move 1 VCO to top in the VCF mixer and try to close the Filter, the signal must stop at 10-20hz Initial Frequency settings., not by 100hz or more, just turn the Trimmer as shown on bottom picture. (read the [TTSH](../../../ttsh/ttsh-calibration-guide/index.md)**[calibration guide](../../../ttsh/ttsh-calibration-guide/index.md)** too, to understand what you do)

![IMG_0593.jpeg](assets/IMG_0593.jpeg)

## VCF Modification

![IMG_8727.JPG](assets/IMG_8727.jpg)

Modded VCF with 1% premium LCR caps in the 4012 and matched 2.5% to 1% tolerance in the 4072 VCF.

I used sockets to make the LCR cap footprint compatible with the PCB RM5 footprint.

![IMG_8728.JPG](assets/IMG_8728.jpg)
