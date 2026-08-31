---
title: "choosing capacitors for DIY Synths"
space: "KNOWHOW"
space_key: "KNOWHOW"
type: page
created: "2018-05-17T08:18:06"
updated: "2025-02-03T14:19:49"
confluence_id: "1704959"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/KNOWHOW/pages/1704959"
---

# choosing capacitors for DIY Synths

here are my BEST PRACTICE tipps of

## Step-by-step guide

1. read the [capacitor types page](../capacitor-types/index.md) at first, to know the difference between polar, bi/unpolar capacitors
2. read this best practice page
3. find a reseller for capacitors  Shopping Tipps Home
4. design and build your synth

we have around 50 different capacitor types and each with are different in casetype, footprint, dielectric

i describe here for now only the THT (Thruhole) Versions what we use for Synths, Effects, Drumcomputer, Eurorack and 4U/5U Formats like Serge, MU, MOTM..

| **Numer** | **Type** | **Dielectricum** | **picture** | **benefit** | **use-case** | **BEST Practice** | **negative** | **identify** | **Footprint** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | MLCC<br>(Multilayer Ceramic Disc Capacitor) | C0G or NP0 |   | temperature stable, timing stable<br>longterm capacitor | VCO timing,<br>VCF Core<br>"Clock timer" | for small pcbs/designs,<br>cheaper than | expensive for bigger capactiy values<br>(above 100pf) | for values less 1nF mostly dark yellow colour, TDK use normally light or dark blue colours for the body | normally only in RM2, RM2.5 and RM5 avaible |
| 2 | MLCC | X5R X7R |   | cheap,<br>longterm capacitor | bypass capacitor |   | microphonic effect possible<br>[read more here](https://e2e.ti.com/blogs_/archives/b/precisionhub/archive/2014/12/19/stress-induced-outbursts-microphonics-in-ceramic-capacitors-part-1) | normally only avaible in yellow colours from 470pF - 2uF | normally only in RM2, RM2.5 and RM5 avaible |
| 3 | Polypropylene (PP) Filmcap | (PP) |   | temperature stable, timing stable<br>longterm capacitor | VCO timing,<br>VCF Core<br>"Clock timer" | avaible in 1% tolerance, perfect for high precision application | bis size |   | avaiable in RM2 - RM20 |
| 4 | Styroflex (Styrene) |   |   | temperature stable, timing stable<br>longterm capacitor | VCO timing,<br>VCF Core<br>"Clock timer" | very popular for VCF /Filtercore<br>the sound is different to C0G or polypropylene<br>avaible in 2% tolerance.<br>ideal for Ladder VCF (moog, arp) | big size |   | avaible in RM2 when mounting upwards |
| 5 | Silver Mica |   |   | temperature stable, timing stable<br>longterm capacitor |   | 1% tolerance,<br>good for VCF because the values are matched within 1% tolerance,<br>good sound in VCF | rare, expensive,<br>not avaible in every size, please note there are some country restrictions for import |   | avaible in RM5 - RM ? |
| 6 | Polyester (PET) (MKP) |   |   | cheap |   |   | 5-20% tolerance |   | avaiable in RM2 - RM20 |
| 7 |   |   |   |   |   |   |   |   |   |
| 8 |   |   |   |   |   |   |   |   |   |
| 9 |   |   |   |   |   |   |   |   |   |
| 10 |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |

> **Info**
>
> **Lessons learned:**
>
> for timing/thermal criticial applications like VCO, VCF, clock use   C0G/NP0 or Polypropylene, Styroflex or Silver Mica.
>
> for VCF try polypropylene or styroflex (depends on the footprint)

## Related articles
