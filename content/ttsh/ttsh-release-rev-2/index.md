---
title: "TTSH Release rev.2"
space: "TTSH"
space_key: "TTSH"
type: page
created: "2017-03-08T14:28:02"
updated: "2024-02-19T22:05:57"
confluence_id: "1311103"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/TTSH/pages/1311103"
attachments: 2
---

# TTSH Release rev.2

**TTSH rev.2 Release**

→ siehe

**BOM**

**only for REV."2"  (v7.1 on pcb top right corner)**

Mainboard BOM

[http://thehumancomparator.net/wordpress/wp-content/uploads/2015/01/ttshv2BOM.pdf](http://thehumancomparator.net/wordpress/wp-content/uploads/2015/01/ttshv2BOM.pdf)

[ttshv2BOM.pdf](assets/ttshv2BOM.pdf)

VCO Sub pcbs BOM

[4027v2BOM.pdf](assets/4027v2BOM.pdf)

[http://thehumancomparator.net/wordpress/wp-content/uploads/2015/01/4027v2BOM.pdf](http://thehumancomparator.net/wordpress/wp-content/uploads/2015/01/4027v2BOM.pdf)

please add: 6x 100nF SMT c0g caps in size 805
mouser part 100nF 77-VJ0805Y104JXXPBC
10nF works fine too (its only a decoupling cap)

3x Timing cap **680pF needs** a polypropylene, polystyrene or silva mica cap(7.5mm footprint)
mouser: 80-PHE450HK3680JR05

you can try the usage **instead** of **SMT inductors/chokes** this:
[http://www.reichelt.de/index.html?ACTION=3;ARTICLE=86466;SEARCH=L-HBCC %20100](http://www.reichelt.de/index.html?ACTION=3;ARTICLE=86466;SEARCH=L-HBCC%20100)
(add enough soldercore to the pcb pads, bent the leads and solder this to the pads)

notice:  the usage of 1k87 tempco 3300ppm instead of 3500ppm works fine too.

DIFF from Version 1to version2    (first TTSH from early2014 to second from early 2015)

[http://thehumancomparator.net/wordpress/wp-content/uploads/2014/05/v1-v2-diffferences.pdf](http://thehumancomparator.net/wordpress/wp-content/uploads/2014/05/v1-v2-diffferences.pdf)

**TTSH Rev.2 known Issues**

**Minor Bug/improvement:** use a BC337-16 instead 2N5172 in the noise section [more Details here](#) (you don't need further mods)

**![](http://www.dsl-man.de/download/attachments/6324282/ttsh-bc337.jpg?version=1&modificationDate=1400677696000&api=v2)**

**Major Bug**

**Description:**the onboard DC-DC adapter (Murata) bleeds in the VCF (EMV - high frequency)

**Solution:**use a external 110/230V powersupply or a other powersupply with 15V/-15V outputs and connect it on the 3pole MTA156 header (dont assemble the onboard power section)

**check the [110V/230V powersupply page](../old-documentation/ttsh-rev2-build-guide/ttsh-230v-110v-powersupply/index.md)**

**TTSH Rev.1 Hardcore builders guide**

works for most parts too..

→ siehe

**Mod: 110V/230V Powersupply**

→ siehe
