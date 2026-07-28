# component_engine.py
import math  # RENTING HEAVY MACHINERY: For exponential decay (e^-t/tau)


def calculate_transients():
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


def calculate_op_amp():
    print("\n--- OP-AMP GAIN CALCULATOR ---")

    try:
        r_in = float(input("Enter Input Resistance R_in (Ohms): "))
        r_f = float(input("Enter Feedback Resistance R_f (Ohms): "))
        v_in = float(input("Enter Input Voltage V_in (Volts): "))

        print("\nSelect Op-Amp Configuration:")
        print("1. Inverting Amplifier")
        print("2. Non-Inverting Amplifier")
        mode = input("Selection (1 or 2): ")

        # TIER 2: THE VENDING MACHINE (Dictionary)
        # We load the exact gain calculations into slots "1" and "2"
        gains = {
            "1": -(r_f / r_in),  # Slot 1: Inverting Formula
            "2": 1 + (r_f / r_in)  # Slot 2: Non-Inverting Formula
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
            print("\n[!] Invalid selection.")

    except ValueError:
        print("\n[!] INPUT ERROR: The factory only accepts heavy numbers.")
    except ZeroDivisionError:
        print("\n[!] FATAL ERROR: Input Resistance (R_in) cannot be zero.")


# --- THE DEPARTMENT MANAGER ---
def component_menu():
    while True:
        print("\n" + "-" * 40)
        print("⚙️ MODULE 4: COMPONENT BEHAVIOR ⚙️")
        print("-" * 40)
        print("1. Transient Response (RC / RL)")
        print("2. Op-Amp Gain Calculator")
        print("0. RETURN TO MAIN LOBBY")
        print("-" * 40)

        choice = input("Select a Component tool (0-2): ")

        if choice == '1':
            calculate_transients()
        elif choice == '2':
            calculate_op_amp()
        elif choice == '0':
            print("\nReturning to Main Factory Lobby...")
            break
        else:
            print("\n[!] Invalid selection. Enter 0-2.")