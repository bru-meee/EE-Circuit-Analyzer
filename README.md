# ⚡ EE Circuit Analyzer V2.0 (Active Development)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Linear_Algebra-013243?style=for-the-badge&logo=numpy)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)

## 📌 Overview
A comprehensive, terminal-based Python engine engineered to automate complex Electrical Engineering computations. Designed to handle steady-state AC/DC analysis, transient circuit dynamics, and digital logic, this suite accelerates engineering workflows by replacing manual computation with automated, physics-based algorithms.

## 🗄️ Repository Architecture
The engine operates on a modular, object-oriented structure, allowing discrete physics calculations to run independently before routing back to the main terminal lobby.

```text
├── main.py                 # Central Dispatch & UI Lobby
├── dc_engine.py            # DC Physics & Divider Rules
├── ac_engine.py            # Phasors, AC Power & 3D Impedance
├── network_engine.py       # NumPy Matrix Solvers & Thevenin Models
├── component_engine.py     # Transients & Op-Amp Behaviors
├── digital_engine.py       # Logic Gates & Base-2 Conversions
├── plan.py                 # Development Roadmap
└── README.md               # Documentation
