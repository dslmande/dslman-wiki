---
title: "Troubleshooting"
space: "ISENIN"
space_key: "ISENIN"
type: page
created: "2022-11-07T09:34:25"
updated: "2022-11-07T09:42:00"
confluence_id: "1312939"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/ISENIN/pages/1312939"
---

# Troubleshooting

Here are some Infos about Troubleshooting

Schematic JP8 - didn't match for all functions

[https://manuals.fdiskc.com/flat/Roland%20Jupiter-8%20Service%20Maunal.pdf](https://manuals.fdiskc.com/flat/Roland%20Jupiter-8%20Service%20Maunal.pdf)

**VCF**

[https://www.ericasynths.lv/media/AS662D.pdf](https://www.ericasynths.lv/media/AS662D.pdf)

[https://alfarzpp.lv/eng/sc/AS3109.pdf](https://alfarzpp.lv/eng/sc/AS3109.pdf)

**Resonance failures:**

**works the resonance or only NOT the Self Oscillation ?**

**when the resonance is completely not working - the Controlboard can be involved in Troubleshooting - (connect****scope on pin16 of as662 as described few lines on bottom)**

at first check the 68K and 560R in the VCF Core around the AS3109, only when all resistors are correct works the Self Oscilallation.

involved are too: q4, R79 (12K next to the Reso Trimmer), as662D close to the q4, Trimmer 10K

you can connect a scope on pin16 of as662 (which is also connected to q4) - when you move the resonance slider, the voltage change between -14v range, the difference is 100mV by moving the Reso slider. 

swap the AS3109 from a working card is an option too for testing.
