---
title: "TR-909 Firmware"
space: "DIY Synth other"
space_key: "DSO"
type: page
created: "2020-05-11T14:05:29"
updated: "2026-01-15T10:00:33"
confluence_id: "1147690"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147690"
attachments: 4
---

# TR-909 Firmware

> **Project**
>
> ### Projecttitel: TR-909
>
> ### Status: `done`
>
> ### page **updated 01/2026**

There´s a massive firmware update in V5.0 from addictive Instruments : [https://revolution909.fr/](https://revolution909.fr/)

I have an TR-909 with Firmware Version v.1 and tried to upadte the firmware byself.

In my labor i have the TL866 Pro 2 programmer and the 2764 er series Eproms on stock.

It was hard to find the hex or bin image file.

so i converted it byself:

**you can download here the Firmware:**

TR-909 v4 Firmware for the origional eprom type (27C64)  (64K)

[TR909-V4\_for64k\_eprom.hex](assets/TR909-V4_for64k_eprom.hex)

here´s the EPR FILE (same content and can be used in the Tool Prony Prog)

[TR909-V4.EPR](assets/TR909-V4.epr)

and for the **27C256**(256K) eprom which is different - please note: you have to ground pin26

[TR909-V4-for-27C256-4000-to-5FFF.hex](assets/TR909-V4-for-27C256-4000-to-5FFF.hex)

here´s the EPR FILE (same content and can be used in the Tool Prony Prog)

[TR909-V4-for-27C256-4000-to-5FFF.EPR](assets/TR909-V4-for-27C256-4000-to-5FFF.epr)

**Here´s a technical description from Robin Whittle:** ([http://www.firstpr.com.au/rwi/tr-909/](http://www.firstpr.com.au/rwi/tr-909/))
"I use a 27C256, with the firmware programmed into the 4000 to 5FFF locations, because  27C256s are more modern, faster and easier to obtain than 27C64s.  **This requires that pin 26 be grounded**.  That said, in 2018, no conventional supplier such as element14, RS Components, Mouser or Digikey supplies 27C256s, since they went out of production around the turn of century.  Furthermore, the great majority of 27C256 EPROMs for sale on eBay are fakes, in that they are modern chips made by some unknown company and falsely marked as being ST or some other brand.  I use EPROMs which I have had since the 1980s or which I have purchased more recently and whose the chip, package and markings exactly resemble the original devices I have had from those days"
