# ac_engine.py
import cmath  # RENTING HEAVY MACHINERY: Complex Math library
import math  # RENTING HEAVY MACHINERY: Standard Math library


def convert_phasors():
    print("\n--- PHASOR CONVERTER (RECTANGULAR <-> POLAR) ---")
    print("1. Polar to Rectangular ( r∠θ --> x + jy )")
    print("2. Rectangular to Polar ( x + jy --> r∠θ )")

    # TUPPERWARE: Storing user's track choice
    mode = input("Select conversion track (1 or 2): ")

    # TIER 5: THE SAFETY NET
    try:
        if mode == '1':
            print("\n>>> TRACK 1: Polar to Rectangular")
            magnitude = float(input("Enter Magnitude (r): "))
            angle_deg = float(input("Enter Angle in degrees (θ): "))

            # WHITEBOARD: Python's cmath uses radians, so we must convert the angle first
            angle_rad = math.radians(angle_deg)

            # THE 3D HOLOGRAM: cmath.rect builds the x + jy complex number
            rectangular_val = cmath.rect(magnitude, angle_rad)

            print("\n[SUCCESS] 3D HOLOGRAM GENERATED:")
            print(f"Rectangular Form: {rectangular_val.real:.4f} + {rectangular_val.imag:.4f}j")

        elif mode == '2':
            print("\n>>> TRACK 2: Rectangular to Polar")
            real_x = float(input("Enter Real part (x): "))
            imag_y = float(input("Enter Imaginary part (y): "))

            # THE 3D HOLOGRAM: Building the z = x + jy variable
            z = complex(real_x, imag_y)

            # WHITEBOARD: cmath.polar returns (magnitude, angle_in_radians)
            magnitude, angle_rad = cmath.polar(z)
            angle_deg = math.degrees(angle_rad)

            print("\n[SUCCESS] PHASOR GENERATED:")
            print(f"Polar Form: {magnitude:.4f} ∠ {angle_deg:.4f}°")

        else:
            print("\n[!] Invalid track selection.")

    except ValueError:
        print("\n[!] INPUT ERROR: The factory only accepts heavy numbers.")


def calculate_impedance():
    print("\n--- IMPEDANCE (Z) CALCULATOR ---")
    print("Calculates Z = R + j(X_L - X_C)")

    try:
        # TUPPERWARE: Loading raw materials
        r = float(input("Enter Resistance (R) in Ohms: "))
        x_l = float(input("Enter Inductive Reactance (X_L) in Ohms (0 if none): "))
        x_c = float(input("Enter Capacitive Reactance (X_C) in Ohms (0 if none): "))

        # WHITEBOARD: Calculating total reactance
        x_total = x_l - x_c

        # TIER 4: 3D HOLOGRAM GENERATION
        # We combine the flat resistance with the 90-degree projection
        z = complex(r, x_total)

        # We also want to ship it with a Polar label (Magnitude and Phase)
        mag, phase_rad = cmath.polar(z)
        phase_deg = math.degrees(phase_rad)

        print("\n[SUCCESS] IMPEDANCE CALCULATED:")
        print(f"Rectangular (Z): {z.real} + {z.imag}j Ohms")
        print(f"Polar (Z):       {mag:.4f} ∠ {phase_deg:.4f}° Ohms")

    except ValueError:
        print("\n[!] INPUT ERROR: The factory only accepts heavy numbers.")


def calculate_ac_power():
    print("\n--- AC POWER CALCULATOR ---")
    print("Calculates Real (P), Reactive (Q), and Apparent (S) Power.")

    try:
        v_rms = float(input("Enter V_rms (Volts): "))
        i_rms = float(input("Enter I_rms (Amps): "))
        phase_angle_deg = float(input("Enter Phase Angle difference between V and I (degrees): "))

        # Convert degrees to radians for the math functions
        phase_rad = math.radians(phase_angle_deg)

        # WHITEBOARD: The Power Triangle math
        apparent_s = v_rms * i_rms
        real_p = apparent_s * math.cos(phase_rad)
        reactive_q = apparent_s * math.sin(phase_rad)
        power_factor = math.cos(phase_rad)

        print("\n[SUCCESS] AC POWER TRIANGLE GENERATED:")
        print(f"Apparent Power (S): {apparent_s:.4f} VA")
        print(f"Real Power (P):     {real_p:.4f} W")
        print(f"Reactive Power (Q): {reactive_q:.4f} VAR")
        print(f"Power Factor (pf):  {power_factor:.4f}")

    except ValueError:
        print("\n[!] INPUT ERROR: The factory only accepts heavy numbers.")


# --- THE DEPARTMENT MANAGER ---
def ac_menu():
    while True:
        print("\n" + "-" * 40)
        print("🌊 MODULE 3: AC & COMPLEX NUMBERS 🌊")
        print("-" * 40)
        print("1. Phasor Converter (Polar/Rectangular)")
        print("2. Impedance Calculator (Z = R + jX)")
        print("3. AC Power Triangle Calculator")
        print("0. RETURN TO MAIN LOBBY")
        print("-" * 40)

        choice = input("Select an AC tool (0-3): ")

        if choice == '1':
            convert_phasors()
        elif choice == '2':
            calculate_impedance()
        elif choice == '3':
            calculate_ac_power()
        elif choice == '0':
            print("\nReturning to Main Factory Lobby...")
            break
        else:
            print("\n[!] Invalid selection. Enter 0-3.")