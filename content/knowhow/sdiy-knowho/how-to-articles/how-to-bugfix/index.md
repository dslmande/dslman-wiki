---
title: "How to bugfix"
space: "KNOWHOW"
space_key: "KNOWHOW"
type: page
created: "2025-02-03T13:00:00"
updated: "2025-03-17T08:59:22"
confluence_id: "336101402"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/KNOWHOW/pages/336101402"
---

# How to bugfix

# Identifying Failures in a Circuit

Identifying failures in a circuit is crucial for troubleshooting and maintaining electrical systems. Here are some steps and methods to help you diagnose circuit failures effectively.

please respect: [The electricity safety rules](../../the-electricity-safety-rules/index.md)

## **0. Write a Documentation**

- **take  paper and make notes about everything you changed**and **check** the following steps,  this prevent wrong measurements, useless parts changes

## 1. Visual Inspection

- **Check for Obvious Damage**: Look for burnt components, broken wires, or signs of overheating, broken or bend IC pins
- **Inspect Connections**: Ensure all connections are secure and free from corrosion.
- **Inspect Traces** - sometimes people cut accidentally traces, by cutting resistor pins
- **for new builds: look under all IC sockets** for pieces from cutter  resistor legs for example
- **Make sure your cables are really connected**- I have seen few times wrong pressed Molex pins for example

## 2. Use of Multimeter

- **Measure Voltage**: Check the voltage at various points in the circuit to ensure it matches expected values.
- **Check Resistance**: Measure resistance across components to identify shorts or open circuits.
- **Continuity Testing**: Use the continuity setting to check if current can flow through the circuit.
- **Check your Voltmeter**in a other circuit to avoid measurement failures

## 3. Signal Testing

- **Oscilloscope**: Use an oscilloscope to visualize waveforms and check for irregularities in signal patterns.
- **Frequency Counter**: Verify that the frequency of signals is within expected ranges.
- **Build building blocks**- disconnect the signal flow to identify the section, for example PSU → VCO, remove the signal flow to the VCF and Ringmod . measure just the VCO out for example
- **Check your Scope** in a other circuit to avoid measurement failures

## 4. Component Testing

- **Test Individual Components**: Remove and test components like resistors, capacitors, and diodes individually to ensure they are functioning correctly.
- **Substitution Method**: Replace suspected faulty components with known good ones to see if the issue resolves.

## 5. Circuit Simulation

- **Compare the Schematics to the circuit**- please be aware that some Service Manuals have different versions and some schematics have failures
- **Frequency Generator:**in case you have experience - insert a signal in the VCF, VCA, Mixer for example - **in circuit**.
- **Use Simulation Software**: Simulate the circuit using software to identify potential failure points and analyze circuit behavior under different conditions.

## 6. Thermal Imaging

- **Infrared Camera**: Use thermal imaging to detect hot spots in the circuit that may indicate a failure.

## 7. Documentation Review

- **Check Schematics**: Review circuit diagrams and schematics to understand the expected operation and identify discrepancies.
- **DIY Builds: check the change log**, Known issue pages, bug tracker, look and ask in given support pages
- **Refer to Maintenance Logs**: Look at past maintenance records for recurring issues or patterns in service manuals

## 8. How to report a issue

1. to receive a fast response without thousands questions you should report this:
2. Device Manufacturer ? who build the machine (in case of diy)
3. Device Modell and Version from the PCBs ?
4. failure description in long version ?
5. changelog - what did you changed exactly?
6. was the machine working before ?
7. in which cases can the failure reproduced ?
8. what did you tested and the results ? - but please aware:  respect my above infos about measurement failures
9. how urgent is a repair - how does it affect your daily business or financial results ?

## Conclusion

Identifying failures in a circuit requires a systematic approach combining visual inspection, testing, and analysis. By following these steps, you can effectively diagnose and resolve circuit issues, ensuring reliable operation of electrical systems.
