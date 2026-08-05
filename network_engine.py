# network_engine.py

# TIER 6: OFFSHORE IMPORTS
# We are renting a foreign, heavy-duty Hydraulic Press and nicknaming it 'np'.
# This press will crush our complex Pallet Racks (Matrices) into solved currents/voltages.
import numpy as np


# TIER 1: THE SUB-CONTRACTOR
# Hiring a specialist for Nodal Analysis. We put them in a room and wait for the result.
def automated_nodal_analysis():
    print("\n--- 🌊 V2.0 AUTOMATED NODAL ANALYSIS (ADMITTANCE MATRIX) ---")
    print(">>> Sub-Contractor 'Nodal' hired. Welcome to the Factory Floor.")
    print(">>> We are assembling the [Y]V = I Pallet Rack from scratch.")

    # TIER 5: THE SAFETY NET
    # Placing a net under the factory. If math explodes (e.g., dividing by 0), the net catches it.
    try:
        # TIER 1: TUPPERWARE & HEAVY WEIGHTS
        # input() hands us a Sticky Note with ink. int() casts it into a heavy iron weight.
        # We store this weight in the 'n' Tupperware container.
        n = int(input("\nEnter the number of UNKNOWN nodes (exclude the reference/ground node): "))
        if n <= 0:
            return  # Dead end. Fire the sub-contractor.

        # TIER 3: THE EMPTY PALLET RACKS
        # np.zeros creates a massive 2D warehouse rack completely filled with 0.0 weights.
        Y_matrix = np.zeros((n, n))
        I_vector = np.zeros(n)

        # TIER 1: THE CONVEYOR BELT
        # This belt runs through every single node, one by one.
        for i in range(n):
            print(f"\n--- 📦 ASSEMBLING NODE {i + 1} ---")

            # Storing the current source into the I_vector Tupperware rack
            i_src = float(
                input(f"Total current entering Node {i + 1} from sources (Amps) [leave negative if leaving]: "))
            I_vector[i] = i_src

            print("Load all resistors connected directly to this node onto the belt.")

            # TIER 1: INFINITE CONVEYOR BELT
            # Runs continuously until the operator pulls the 'break' lever.
            while True:
                r_val = float(input("Enter resistor weight in Ohms (or '0' to pull the break lever): "))

                # TIER 1: THE TRAIN TRACK DISPATCHER
                if r_val == 0:
                    break  # Operator pulled the lever. Stop the belt for this node.

                # Loading automated conductance (1/R) into the diagonal slot of our Pallet Rack
                Y_matrix[i, i] += (1.0 / r_val)

        print("\n--- 🔗 LOADING SHARED RESISTORS ---")
        # Double Conveyor Belt: One runs the rows, the other runs the columns.
        for i in range(n):
            for j in range(i + 1, n):
                r_shared = float(
                    input(f"Enter resistor shared between Node {i + 1} and Node {j + 1} (or '0' if none): "))

                # The Dispatcher checks if a resistor actually exists here
                if r_shared != 0:
                    conductance = 1.0 / r_shared
                    # Subtracting the heavy weight symmetrically across the Pallet Rack
                    Y_matrix[i, j] -= conductance
                    Y_matrix[j, i] -= conductance

        print("\n[ASSEMBLY COMPLETE] Sending Admittance Pallet Rack to the Hydraulic Press...")

        # TIER 6: THE HYDRAULIC PRESS IN ACTION
        results = np.linalg.solve(Y_matrix, I_vector)

        print("\n[SUCCESS] HYDRAULIC PRESS FINISHED. NODE VOLTAGES EXTRACTED:")
        # Final Conveyor belt to print out all the Tupperware results
        for i in range(n):
            print(f"Voltage at Node {i + 1} = {results[i]:.4f} V")

    except np.linalg.LinAlgError:
        print("\n[!] FATAL ERROR: Singular Matrix. The Pallet Rack collapsed in the press.")
    except ValueError:
        print("\n[!] INPUT ERROR: Safety Net triggered. The factory only accepts heavy numbers, not ink.")
    except ZeroDivisionError:
        print("\n[!] FATAL ERROR: Safety Net triggered. A 0 Ohm resistor creates a short circuit explosion.")


# TIER 1: THE SUB-CONTRACTOR
def automated_mesh_analysis():
    print("\n--- 🌪️ V2.0 AUTOMATED MESH ANALYSIS (IMPEDANCE MATRIX) ---")
    print(">>> Sub-Contractor 'Mesh' hired. Building the [Z]I = V Pallet Rack.")

    # TIER 5: THE SAFETY NET
    try:
        # Casting ink into a heavy iron weight, putting it in Tupperware 'n'
        n = int(input("\nEnter the number of Loops/Meshes: "))
        if n <= 0:
            return

        # TIER 3: THE EMPTY PALLET RACKS
        Z_matrix = np.zeros((n, n))
        V_vector = np.zeros(n)

        # TIER 1: THE CONVEYOR BELT
        for i in range(n):
            print(f"\n--- 🔄 ASSEMBLING LOOP {i + 1} ---")

            v_src = float(input(f"Sum of voltage sources driving CLOCKWISE in Loop {i + 1} (Volts): "))
            V_vector[i] = v_src

            r_total = float(input(f"Sum of ALL resistor weights in Loop {i + 1} (Ohms): "))
            # Loading total resistance into the diagonal slot of the Pallet Rack
            Z_matrix[i, i] = r_total

        print("\n--- 🔗 LOADING SHARED RESISTORS ---")
        for i in range(n):
            for j in range(i + 1, n):
                r_shared = float(
                    input(f"Enter resistor shared between Loop {i + 1} and Loop {j + 1} (or '0' if none): "))

                # TIER 1: THE DISPATCHER
                if r_shared != 0:
                    # Subtracting the shared weight symmetrically
                    Z_matrix[i, j] -= r_shared
                    Z_matrix[j, i] -= r_shared

        print("\n[ASSEMBLY COMPLETE] Sending Impedance Pallet Rack to the Hydraulic Press...")

        # TIER 6: THE HYDRAULIC PRESS IN ACTION
        results = np.linalg.solve(Z_matrix, V_vector)

        print("\n[SUCCESS] HYDRAULIC PRESS FINISHED. MESH CURRENTS EXTRACTED:")
        for i in range(n):
            print(f"Current for Loop {i + 1} = {results[i]:.4f} A")

    except np.linalg.LinAlgError:
        print("\n[!] FATAL ERROR: Singular Matrix. The Pallet Rack collapsed in the press.")
    except ValueError:
        print("\n[!] INPUT ERROR: Safety Net triggered. The factory only accepts heavy numbers, not ink.")


# TIER 1: THE SUB-CONTRACTOR
def generate_thevenin_norton():
    print("\n--- ⚡ THEVENIN / NORTON EQUIVALENT GENERATOR ---")
    print("1. Generate from Open-Circuit Voltage (Voc) & Short-Circuit Current (Isc)")
    print("2. Generate from Standard Topology (Source Vs, Series R1, Parallel R2)")

    # Getting a Sticky Note (String) and placing it in Tupperware 'mode'
    mode = input("Select operation track (1 or 2): ")

    # TIER 5: THE SAFETY NET
    try:
        # TIER 1: THE TRAIN TRACK DISPATCHER
        if mode == '1':
            print("\n>>> DISPATCHER SELECTED TRACK 1: Voc / Isc Conversion")
            # Casting ink into heavy iron weights
            v_oc = float(input("Enter Open-Circuit Voltage (Voc) in Volts: "))
            i_sc = float(input("Enter Short-Circuit Current (Isc) in Amps: "))

            # Processing raw materials into finished products
            r_th = v_oc / i_sc
            v_th = v_oc
            i_n = i_sc

            print("\n[SUCCESS] EQUIVALENT CIRCUITS MANUFACTURED:")
            print(f"Thevenin Equivalent: V_th = {v_th:.4f} V, R_th = {r_th:.4f} Ohms")
            print(f"Norton Equivalent:   I_n = {i_n:.4f} A, R_th = {r_th:.4f} Ohms")

        elif mode == '2':
            print("\n>>> DISPATCHER SELECTED TRACK 2: Topology Reduction")
            v_s = float(input("Enter Source Voltage (Vs) in Volts: "))
            r_1 = float(input("Enter Series Resistor (R1) in Ohms: "))
            r_2 = float(input("Enter Parallel Resistor (R2) near load in Ohms: "))

            # Processing raw materials
            v_th = v_s * (r_2 / (r_1 + r_2))
            r_th = (r_1 * r_2) / (r_1 + r_2)
            i_n = v_th / r_th

            print("\n[SUCCESS] EQUIVALENT CIRCUITS MANUFACTURED:")
            print(f"Thevenin Equivalent: V_th = {v_th:.4f} V, R_th = {r_th:.4f} Ohms")
            print(f"Norton Equivalent:   I_n = {i_n:.4f} A, R_th = {r_th:.4f} Ohms")

        else:
            print("\n[!] DISPATCHER ERROR: Invalid track selection.")

    except ZeroDivisionError:
        print("\n[!] FATAL ERROR: Safety Net triggered. Short circuit detected (Current or Resistance cannot be 0).")
    except ValueError:
        print("\n[!] INPUT ERROR: Safety Net triggered. The factory only accepts heavy numbers, not ink.")


# --- THE DEPARTMENT MANAGER ---
# This is the master coordinator for Module 2.
def network_menu():
    # TIER 1: INFINITE CONVEYOR BELT (The Main Factory Loop)
    while True:
        print("\n" + "=" * 50)
        print("🕸️ MODULE 2: NETWORK THEOREMS (V2.0) 🕸️")
        print("=" * 50)
        print("1. Automated Nodal Analysis (Admittance Matrix)")
        print("2. Automated Mesh Analysis (Impedance Matrix)")
        print("3. Thevenin/Norton Equivalent Generator")
        print("0. PULL LEVER TO RETURN TO MAIN LOBBY")
        print("=" * 50)

        choice = input("Select a Network sub-contractor (0-3): ")

        # TIER 1: THE TRAIN TRACK DISPATCHER (Routing the user)
        if choice == '1':
            automated_nodal_analysis()
        elif choice == '2':
            automated_mesh_analysis()
        elif choice == '3':
            generate_thevenin_norton()
        elif choice == '0':
            print("\n>>> BREAK LEVER PULLED. Returning to Main Factory Lobby...")
            break  # Kills the infinite conveyor belt
        else:
            print("\n[!] DISPATCHER ERROR: Invalid selection. Enter 0-3.")
