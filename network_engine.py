# network_engine.py
import numpy as np  # RENTING THE HYDRAULIC PRESS


def solve_2x2_matrix():
    print("\n--- 2x2 MESH / NODAL MATRIX SOLVER ---")
    print("This machine solves simultaneous equations of the form:")
    print("[A]x + [B]y = [C]")
    print("[D]x + [E]y = [F]")

    # TIER 5: FAILSAFE PROTOCOL - The Safety Net[cite: 1]
    try:
        print("\nEnter the values for Equation 1 (Loop 1 / Node 1):")
        a = float(input("Enter A: "))
        b = float(input("Enter B: "))
        c = float(input("Enter C (Constant): "))

        print("\nEnter the values for Equation 2 (Loop 2 / Node 2):")
        d = float(input("Enter D: "))
        e = float(input("Enter E: "))
        f = float(input("Enter F (Constant): "))

        # TIER 3: THE PALLET RACK (2D List)[cite: 1]
        # Building the resistance/conductance matrix
        coefficients = np.array([
            [a, b],
            [d, e]
        ])

        # Building the voltage/current constant matrix
        constants = np.array([c, f])

        # THE HYDRAULIC PRESS: Solving the matrix instantly[cite: 1]
        results = np.linalg.solve(coefficients, constants)

        print("\n[SUCCESS] MATRIX SOLVED:")
        print(f"Variable 1 (I1 / V1) = {results[0]:.4f}")
        print(f"Variable 2 (I2 / V2) = {results[1]:.4f}")

    except np.linalg.LinAlgError:
        print("\n[!] FATAL ERROR: Singular Matrix. These equations cannot be solved (Parallel lines).")
    except ValueError:
        print("\n[!] INPUT ERROR: The factory only accepts heavy numbers, not letters.")


def generate_thevenin_norton():
    print("\n--- THEVENIN / NORTON EQUIVALENT GENERATOR ---")
    print("1. Generate from Open-Circuit Voltage (Voc) & Short-Circuit Current (Isc)")
    print("2. Generate from Standard Topology (Source Vs, Series R1, Parallel R2)")

    # TUPPERWARE: Storing the user's selected track
    mode = input("Select operation track (1 or 2): ")

    # TIER 5: FAILSAFE PROTOCOL - The Safety Net
    try:
        # THE TRAIN TRACK DISPATCHER
        if mode == '1':
            print("\n>>> TRACK 1: Voc / Isc Conversion")
            # TUPPERWARE: Loading raw materials
            v_oc = float(input("Enter Open-Circuit Voltage (Voc) in Volts: "))
            i_sc = float(input("Enter Short-Circuit Current (Isc) in Amps: "))

            # WHITEBOARD: Performing the Ohm's Law translation
            r_th = v_oc / i_sc
            v_th = v_oc
            i_n = i_sc

            # THE SHIPPING LABEL: Printing the final equivalents
            print("\n[SUCCESS] EQUIVALENT CIRCUITS GENERATED:")
            print(f"Thevenin Equivalent: V_th = {v_th:.4f} V, R_th = {r_th:.4f} Ohms")
            print(f"Norton Equivalent:   I_n = {i_n:.4f} A, R_th = {r_th:.4f} Ohms")

        elif mode == '2':
            print("\n>>> TRACK 2: Topology Reduction")
            # TUPPERWARE: Loading raw materials
            v_s = float(input("Enter Source Voltage (Vs) in Volts: "))
            r_1 = float(input("Enter Series Resistor (R1) in Ohms: "))
            r_2 = float(input("Enter Parallel Resistor (R2) near load in Ohms: "))

            # WHITEBOARD: Killing the source and calculating equivalents
            v_th = v_s * (r_2 / (r_1 + r_2))  # Voltage Divider for V_th
            r_th = (r_1 * r_2) / (r_1 + r_2)  # Parallel equivalence for R_th
            i_n = v_th / r_th  # Source Transformation for Norton

            # THE SHIPPING LABEL
            print("\n[SUCCESS] EQUIVALENT CIRCUITS GENERATED:")
            print(f"Thevenin Equivalent: V_th = {v_th:.4f} V, R_th = {r_th:.4f} Ohms")
            print(f"Norton Equivalent:   I_n = {i_n:.4f} A, R_th = {r_th:.4f} Ohms")

        else:
            print("\n[!] Invalid track selection.")

    except ZeroDivisionError:
        print("\n[!] FATAL ERROR: Short circuit detected (Current or Resistance cannot be 0).")
    except ValueError:
        print("\n[!] INPUT ERROR: The factory only accepts heavy numbers, not letters.")

# --- THE DEPARTMENT MANAGER ---
def network_menu():
    while True:
        print("\n" + "-" * 40)
        print("🕸️ MODULE 2: NETWORK THEOREMS 🕸️")
        print("-" * 40)
        print("1. 2x2 Matrix Solver (Mesh/Nodal)")
        print("2. Thevenin/Norton Generator (Under Construction)")
        print("0. RETURN TO MAIN LOBBY")
        print("-" * 40)

        choice = input("Select a Network tool (0-2): ")

        if choice == '1':
            solve_2x2_matrix()
        elif choice == '2':
            generate_thevenin_norton()
        elif choice == '0':
            print("\nReturning to Main Factory Lobby...")
            break
        else:
            print("\n[!] Invalid selection. Enter 0-2.")