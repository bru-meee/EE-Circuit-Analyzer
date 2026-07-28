# ⚡ EE Circuit Analyzer V1.0

## Overview
A comprehensive, terminal-based Python engine engineered to automate complex Electrical Engineering computations. Designed to handle both steady-state and transient circuit physics, this suite accelerates circuit analysis by replacing manual computation with automated, physics-based algorithms.

## Core Architecture
* **Module 1: DC Circuit Engine** - Ohm's Law matrices, Series/Parallel Equivalence, and Voltage/Current Divider rules.
* **Module 2: Network Theorems** - 2x2 Mesh/Nodal Matrix Solvers utilizing NumPy linear algebra, alongside Thevenin/Norton Equivalent generation.
* **Module 3: AC & Complex Numbers** - Phasor translations (Polar/Rectangular), 3D Impedance tracking, and AC Power Triangle generation.
* **Module 4: Component Behavior** - First-Order Transient response modeling (RC/RL circuits) and active Op-Amp Gain processing.
* **Module 5: Digital Logic** - Automated Truth Table generation, bitwise Logic Gate simulation, and Base-2/Base-10 translation matrices.

## Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** `numpy` (Linear Algebra / Matrix solvers), `math`, `cmath` (Complex AC Phasors).

## Execution
Run `main.py` in your terminal to initialize the central dashboard and access the modular subsystems.
