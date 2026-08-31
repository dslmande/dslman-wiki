---
title: "TTSH rev.2 Build notices"
space: "TTSH"
space_key: "TTSH"
type: page
created: "2015-02-06T17:02:12"
updated: "2020-02-25T08:14:05"
confluence_id: "1310800"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/TTSH/pages/1310800"
---

# TTSH rev.2 Build notices

here is the new \[b\]Build thread rev.2\[/b\]
(backup here:\[url\] http://electro-music.com/forum\[/url\]/viewtopic.php?p=407150#407150   and on my website)

General TTSH postings like Availability and more here:
\[url\][https://www.muffwiggler.com/forum/viewtopic.php?t=82997](https://www.muffwiggler.com/forum/viewtopic.php?t=82997) \[/url\]

\[b\]TTSH Ver.2\[/b\]  (7.1 on pcb)
Released:  5.January 2015

Release Info:
Changes between first Version and rev.2:
- Powersection, two 1 inch voltage converter, embedded powerregulator like nordcores v1 addon pcb, 3x SMD inductors/chokes and more
- Amplifier : new design without cooling, other Amplifier Transistors and some other parts in this section
- LED Driver redesign
- multiples on pcb
- speaker holes
- switches: you get with the pcb kit few small pcbs with - this are used like a washer for the switches, in result switch mounting is easier as in TTSH rev.1 (pics on my website)
- some minor fixes
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\[b\]Schematic v2  (7.1):\[/b\]
\[url\]http://thehumancomparator.net/wordpress/wp-content/uploads/2014/05/ttshv2schematics.pdf\[/url\]
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\[b\]Jon /Zthees Buidling guide (26.Jan.2015 uncomplete)\[/b\]
\[url\]http://build.thehumancomparator.net/\[/url\]
\[b\]
my own Building guide for Users with good experiences in DIY:\[/b\]
\[url\]https://www.dsl-man.de/display/DSO/TTSH+rev2+Buidling+Guide\[/url\]
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\[b\]Mainboard BOM\[/b\]

\[url\]http://thehumancomparator.net/wordpress/wp-content/uploads/2015/01/ttshv2BOM.pdf\[/url\]
dont worry if you miss 2x 100K resisitors and 1x 1M , TL071 -  thats only needed when you complete the TL071 section on frontpanel pcb side
1x 10K resistor left

add 4x 4n7 c0g instead of 4x 4n7 from BOM - (wrong partnumber)
(correct nr. partnumber 810-FK28C0G1H472J )

add 2x 12k resistor  instead of one
add 32x 1uF electrolyte cap  instead of 31

\[b\]VCO Sub pcbs BOM\[/b\]

\[url\]http://thehumancomparator.net/wordpress/wp-content/uploads/2015/01/4027v2BOM.pdf\[/url\]

please add: 6x 100nF SMT c0g caps in size 805
mouser part 100nF 77-VJ0805Y104JXXPBC  instead of the 6x normal caps.
10nF works fine too (its only a decoupling cap)

3x  Timing cap 680pF needs a polypropylene, polystyrene or silva mica (7.5mm footprint)
mouser:  80-PHE450HK3680JR05

\[b\]notice: \[/b\]  the usage of 1k87  3300ppm instead of 3500ppm works fine too.

you can try the usage instead of SMT inductors/chokes this:
\[url\]http://www.reichelt.de/index.html?ACTION=3;ARTICLE=86466;SEARCH=L-HBCC%20100\[/url\]
(add enough soldercore to the pcb pads, bent the leads and solder this to the pads)

\[b\]
DIFF from Version 1to version2\[/b\]    (first TTSH from early2014 to second from early 2015)
\[url\]http://thehumancomparator.net/wordpress/wp-content/uploads/2014/05/v1-v2-diffferences.pdf\[/url\]

rare partkit: [http://www.thonk.co.uk/?s=ttsh&submit.x=0&submit.y=0&post\_type=product](http://www.thonk.co.uk/?s=ttsh&submit.x=0&submit.y=0&post_type=product)
full partkits, cases: [http://www.synthcube.com/cart](http://www.synthcube.com/cart)

matched pairs and some other parts from my groupbuy left, ask me.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\[b\]Studio/Roadcase Cases opt. Tolex \[/b\]  [https://dsl-man.atlassian.net/wiki/display/DSO/TTSH+Case](../../../ttsh-case/index.md)
synthcube.com plans to offer cases too
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\[b\]known Issues and more\[/b\]

1.
You dont need TTSHv1. Bugfixes in rev.2 to get a working TTSH
all known Issues are fixed in rev.2, except the Noise gain/distorted - for my usage its the default good  \[url\]https://www.dsl-man.de/display/DSO/TTSH+known+issues#TTSHknownissues-3fix\[/url\]

2.
Measurement of DC Regulator output:
use  for measurement  the TP 15V to ground and TP -15V to ground \[b\](not TP1 or TP3 )\[/b\]
THATS very important to measure -15/+15V
otherwise you risk expensive damages or blown caps. (safe your eyes)

3.
if you plan to add the VCO Sync option, dont cut the legs from all VCO subboards too short (see VCO sync option here)
please pm me, if you want to add/correct here some Infos

4.
mount the mje172/mje182 with letters in position to pcb inside not to the outside. (pics later)

5. picture of matched pairs here:
\[img\]https://www.dsl-man.de/download/thumbnails/10420421/matched\_pairs.jpg\[/img\]
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\[b\]Modifications (no bugfixes) \[/b\]

AR Envelope:
\[url\]https://www.dsl-man.de/display/DSO/TTSH+Mod+AR+Envelope\[/url\]

VCO Sync:
\[url\][https://dsl-man.atlassian.net/wiki/display/DSO/TTSH+Mod+Sync+Option](#)
\[/url\]
Reverb Op-amp:
\[url\]https://www.dsl-man.de/display/DSO/TTSH+Reverb+Driver+Mod\[/url\]

Gatebooster:
\[url\]https://www.dsl-man.de/display/DSO/TTSH+Gatebooster\[/url\]
