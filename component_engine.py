# component_engine.py
import math  # TIER 6: RENTING HEAVY MACHINERY (For exponentials and square roots)


def calculate_first_order_transients():
    print("\n--- FIRST-ORDER TRANSIENT RESPONSE ---")
    print("1. RC Circuit (Resistor-Capacitor)")
    print("2. RL Circuit (Resistor-Inductor)")

    mode = input("Select circuit type (1 or 2): ")

    # TIER 5: THE SAFETY NET
    try:
        if mode == '1':
            print("\n>>> TRACK 1: RC Circuit (Capacitor Charging)")
            r = float(input("Enter Resistance (Ohms): "))
            c = float(input("Enter Capacitance (Farads): "))
            v_s = float(input("Enter Source Voltage (Volts): "))
            t = float(input("Enter time elapsed (seconds): "))

            # WHITEBOARD: Time Constant (Tau)
            tau = r * c

            # THE HEAVY MACHINERY: math.exp() calculates e^(-t/tau)
            v_t = v_s * (1 - math.exp(-t / tau))

            print("\n[SUCCESS] TRANSIENT STATE CALCULATED:")
            print(f"Time Constant (τ): {tau:.4f} seconds")
            print(f"Voltage across Capacitor at {t}s: {v_t:.4f} V")

        elif mode == '2':
            print("\n>>> TRACK 2: RL Circuit (Inductor Energizing)")
            r = float(input("Enter Resistance (Ohms): "))
            l = float(input("Enter Inductance (Henries): "))
            v_s = float(input("Enter Source Voltage (Volts): "))
            t = float(input("Enter time elapsed (seconds): "))

            # WHITEBOARD: Time Constant (Tau)
            tau = l / r

            # WHITEBOARD: Max current is V/R
            i_max = v_s / r

            # THE HEAVY MACHINERY: math.exp() calculates e^(-t/tau)
            i_t = i_max * (1 - math.exp(-t / tau))

            print("\n[SUCCESS] TRANSIENT STATE CALCULATED:")
            print(f"Time Constant (τ): {tau:.4f} seconds")
            print(f"Current through Inductor at {t}s: {i_t:.4f} A")

        else:
            print("\n[!] Invalid track selection.")

    except ValueError:
        print("\n[!] INPUT ERROR: The factory only accepts heavy numbers.")
    except ZeroDivisionError:
        print("\n[!] FATAL ERROR: Resistance cannot be zero in these circuits.")
    # ... (V1.0 Code remains identical, utilizing Tier 5 Safety Nets and Tier 1 Tupperware) ...
    pass


def calculate_second_order_rlc():
    print("\n--- 🌊 SECOND-ORDER RLC TRANSIENT ENGINE ---")
    print("1. Series RLC Circuit")
    print("2. Parallel RLC Circuit")

    # TIER 1: THE TRAIN TRACK DISPATCHER (if/elif/else)
    mode = input("Select circuit topology (1 or 2): ")

    # TIER 5: THE SAFETY NET
    try:
        if mode in ['1', '2']:
            r = float(input("\nEnter Resistance (Ohms): "))
            l = float(input("Enter Inductance (Henries): "))
            c = float(input("Enter Capacitance (Farads): "))

            # TIER 6: Heavy Machinery calculating the Resonant Frequency
            omega = 1 / math.sqrt(l * c)

            if mode == '1':
                print("\n>>> TRACK 1: SERIES RLC TOPOLOGY LOADED")
                alpha = r / (2 * l)
            else:
                print("\n>>> TRACK 2: PARALLEL RLC TOPOLOGY LOADED")
                alpha = 1 / (2 * r * c)

            # Calculate Damping Ratio
            zeta = alpha / omega

            print("\n[SUCCESS] RLC PARAMETERS EXTRACTED:")
            print(f"Attenuation (\u03B1): {alpha:.4f} Np/s")
            print(f"Resonant Frequency (\u03C9): {omega:.4f} rad/s")
            print(f"Damping Ratio (\u03B6): {zeta:.4f}")

            # Determine Damping Type based on roots
            if alpha > omega:
                print(">>> SYSTEM STATUS: OVERDAMPED (Roots are real and not equal)")
            elif alpha < omega:
                print(">>> SYSTEM STATUS: UNDER-DAMPED (Roots are complex. Oscillation detected!)")
            else:
                print(">>> SYSTEM STATUS: CRITICALLY DAMPED (Roots are real and equal)")
        else:
            print("\n[!] Invalid track selection.")

    except ValueError:
        print("\n[!] INPUT ERROR: The factory only accepts heavy numbers.")
    except ZeroDivisionError:
        print("\n[!] FATAL ERROR: Resistance/Inductance/Capacitance cannot be zero in this topology.")


def calculate_op_amp():
    print("\n--- 🎛️ OP-AMP GAIN CALCULATOR ---")

    try:
        r_in = float(input("Enter Input Resistance R_in (Ohms): "))
        r_f = float(input("Enter Feedback Resistance R_f (Ohms): "))
        v_in = float(input("Enter Input Voltage V_in (Volts): "))

        print("\nSelect Op-Amp Configuration:")
        print("1. Inverting Amplifier")
        print("2. Non-Inverting Amplifier")
        mode = input("Selection (1 or 2): ")

        # TIER 2: THE VENDING MACHINE (Dictionary)
        # Loading the exact gain formulas into slots "1" and "2"
        gains = {
            "1": -(r_f / r_in),
            "2": 1 + (r_f / r_in)
        }

        # THE KEYPAD: If the user types a valid slot...
        if mode in gains:
            # Drop the specific gain calculation from the vending machine
            gain = gains[mode]
            v_out = gain * v_in

            print("\n[SUCCESS] OP-AMP BEHAVIOR CALCULATED:")
            print(f"Gain (Av): {gain:.4f}")
            print(f"Output Voltage (V_out): {v_out:.4f} V")
        else:
            print("\n[!] Invalid keypad selection.")

    except ValueError:
        print("\n[!] INPUT ERROR: The factory only accepts heavy numbers.")
    except ZeroDivisionError:
        print("\n[!] FATAL ERROR: Input Resistance (R_in) cannot be zero.")


# --- THE DEPARTMENT MANAGER (Sub-Contractor) ---
def component_menu():
    while True:
        print("\n" + "-" * 50)
        print("⚙️ MODULE 4: COMPONENT BEHAVIOR (V2.0) ⚙️")
        print("-" * 50)
        print("1. First-Order Transient Response (RC / RL)")
        print("2. Second-Order Transient Response (RLC)")
        print("3. Op-Amp Gain Calculator")
        print("0. RETURN TO MAIN FACTORY LOBBY")
        print("-" * 50)

        choice = input("Select a Component tool (0-3): ")

        if choice == '1':
            calculate_first_order_transients()
        elif choice == '2':
            calculate_second_order_rlc()
        elif choice == '3':
            calculate_op_amp()
        elif choice == '0':
            print("\nReturning to Main Factory Lobby...")
            break
        else:
            print("\n[!] Invalid selection. Enter 0-3.")
