# EE Circuit Analyzer V2.0

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Linear_Algebra-013243?style=flat-square&logo=numpy)
![Schemdraw](https://img.shields.io/badge/Schemdraw-Schematics-orange?style=flat-square)

Terminal-based Python tool for core electrical and electronic engineering calculations.  
Built to cover the main topics from a first-year EE circuits module and extended with network theorems, transients, digital logic, and schematic generation.

## Features

| Module | What it does |
|--------|--------------|
| **1. DC Circuits** | Ohm’s Law, series/parallel resistance, voltage & current dividers |
| **2. Network Theorems** | Automated Nodal Analysis (N×N admittance matrix) and Mesh Analysis (N×N impedance matrix) using NumPy, plus Thevenin/Norton equivalents |
| **3. AC & Complex Numbers** | Phasor conversion (polar ↔ rectangular), impedance \(Z = R + jX\), AC power triangle (P, Q, S, power factor) |
| **4. Component Behaviour** | First-order RC/RL transients, second-order RLC (damping type), op-amp gain (inverting / non-inverting) |
| **5. Digital Logic** | Truth tables for common gates, binary ↔ decimal conversion |
| **6. Visual Output** | Generates 2D circuit schematics with `schemdraw` and saves them as PNG files |

## Project Structure

```text
├── main.py                 # Main menu / entry point
├── dc_engine.py            # DC calculations
├── network_engine.py       # Nodal, Mesh, Thevenin/Norton
├── ac_engine.py            # Phasors, impedance, AC power
├── component_engine.py     # Transients & op-amps
├── digital_engine.py       # Logic gates & number conversion
├── visual_engine.py        # Schemdraw schematic generation
├── plan.py                 # Development notes
└── README.md
