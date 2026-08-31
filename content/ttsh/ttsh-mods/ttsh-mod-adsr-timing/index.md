---
title: "TTSH Mod ADSR Timing"
space: "TTSH"
space_key: "TTSH"
type: page
created: "2017-06-16T13:09:21"
updated: "2024-11-21T07:24:05"
confluence_id: "1310796"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/TTSH/pages/1310796"
attachments: 6
---

# TTSH Mod ADSR Timing

> **Info**
>
> this Mod was tested and works great

**ADSR:** ADSR C1, C2 are replaced with a single .22u cap, and its (+) terminal is tapped to a SPDT on-off-on switch that will connect to (+) terminals on either a 22uF or 2.2uF cap in parallel with the 0.22uF cap. These cap values provide a wide range, the range can be contracted by adjusting the value of the smallest and largest cap in the trio. The tricky part is building a little tree with the three caps, all their (-) terminals common, and putting that into the original cap location. A simplified (possibly more elegant) version of this might address only the specific deficiencies (AD being too long, ADSR being too short).

**original TTSH**

![image2017-6-16 15:4:53.png](assets/image2017-6-16-15-4-53.png)

**Modded TTSH ADSR** (C1 replaced with 0.22uF , C2 removed for a MTA100 header )

![ADSR.jpg](assets/ADSR.jpg)

(1,5UF, 15UF, in combination of 150nF works too)

**PRACTICE:**

1. **use for C1 or C2 a 0.22UF electrolyte cap instead of 1uF**

2. for a easy connection use a MTA100 header to connect later the capacitor switch, **mark/label the positive pin with a pen**

   (switch between 2.2UF and 22uF with a ON-On switch, it works with a ON-OFF-ON switch too (preffered) - then you only have the 0,22uF cap active when the switch is in OFF position)

![IMG_5080.JPG](assets/IMG_5080.jpg)

3. build the switch with caps like this, important: use cable shrink to isolate the cables.

![IMG_5215.JPG](assets/IMG_5215.jpg)

connect both positive capacitor ends together and connect this to the MTA100 header (positive), the middle pin is ground and connected to the MTA header ground.

![IMG_4955.JPG](assets/IMG_4955.jpg)

## optional AD- RANGE Switch (never used by me)

**AD**: C69 is replaced with a .1u cap, and its (+) terminal is tapped to a SPDT on-off-on switch that will connect to (+) terminals on either a 10u or 1u cap in parallel with the .1u cap.
