# dc_engine.py

def calculate_ohms_law():
    # THE FACTORY LOBBY: Greeting the user
    print("\n--- OHM'S LAW CALCULATOR INITIATED ---")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    print("4. Power (P)")

    # TUPPERWARE: Creating a box named 'target' to store the user's choice
    target = input("Select an option (1-4): ")

    # TRAIN TRACK SWITCH: Sending the program down the right path
    if target == '1':
        # TUPPERWARE: Storing raw materials as heavy decimals (float)
        i = float(input("Enter Current in Amps: "))
        r = float(input("Enter Resistance in Ohms: "))
        # WHITEBOARD: Doing the math
        v = i * r
        print(f"\nResult: Voltage = {v} V")

    elif target == '2':
        v = float(input("Enter Voltage in Volts: "))
        r = float(input("Enter Resistance in Ohms: "))
        i = v / r
        print(f"\nResult: Current = {i} A")

    elif target == '3':
        v = float(input("Enter Voltage in Volts: "))
        i = float(input("Enter Current in Amps: "))
        r = v / i
        print(f"\nResult: Resistance = {r} Ohms")

    elif target == '4':
        v = float(input("Enter Voltage in Volts: "))
        i = float(input("Enter Current in Amps: "))
        p = v * i
        print(f"\nResult: Power = {p} Watts")

    else:
        # DEAD END: The user typed something wrong
        print("\n[!] Invalid selection.")


def calculate_resistor_equivalence():
    print("\n--- EQUIVALENT RESISTANCE CALCULATOR ---")
    print("1. Series")
    print("2. Parallel")

    mode = input("Select configuration (1 or 2): ")

    if mode not in ['1', '2']:
        print("\n[!] Invalid selection. Train derailed.")
        return  # EMERGENCY STOP: Kills the function immediately

    # STICKY NOTE: Taking a single line of text from the user
    print("\nEnter all resistor values separated by spaces (e.g., 10 20 150.5)")
    raw_input = input("Values: ")

    # TOOLBOX: An empty list waiting for items
    resistors = []

    # CONVEYOR BELT (for loop) & SCISSORS (.split)
    # Cuts the sticky note, translates ink to weights, and drops them in the toolbox
    for val in raw_input.split():
        resistors.append(float(val))

    # TRAIN TRACK SWITCH
    if mode == '1':
        # THE SCALE: sum() automatically adds every heavy weight in the toolbox
        r_eq = sum(resistors)
        print(f"\nResult: R_eq (Series) = {r_eq} Ohms")

    elif mode == '2':
        # WHITEBOARD: Start the running total at 0
        inverse_sum = 0

        # CONVEYOR BELT: Pick up each weight in the toolbox one by one
        for r in resistors:
            inverse_sum += (1 / r)  # Add the fraction to the whiteboard

        # WHITEBOARD: Flip the final total upside down
        r_eq = 1 / inverse_sum

        # DISPLAY: The {:.4f} formats the final shipping label to 4 decimal places
        print(f"\nResult: R_eq (Parallel) = {r_eq:.4f} Ohms")

def calculate_dividers():
    print("\n--- DIVIDER RULE CALCULATOR ---")
    print("1. Voltage Divider (Series Circuit)")
    print("2. Current Divider (Parallel Circuit)")

    mode = input("Select rule (1 or 2): ")

    if mode not in ['1', '2']:
        print("\n[!] Invalid selection.")
        return

    # TUPPERWARE: Securing specific raw materials before the assembly line
    source_val = float(input("Enter total Source value (Volts or Amps): "))
    target_r = float(input("Enter the specific Resistor value you want to analyze (Ohms): "))

    # STICKY NOTE -> SCISSORS -> CONVEYOR BELT -> TOOLBOX
    print("Enter ALL resistor values in the circuit separated by spaces (e.g., 10 20 30)")
    raw_input = input("All Resistors: ")
    resistors = []
    for val in raw_input.split():
        resistors.append(float(val))

    # TRAIN TRACK SWITCH
    if mode == '1':
        # VOLTAGE DIVIDER TRACK
        r_total = sum(resistors)  # Dump toolbox on the scale
        v_drop = source_val * (target_r / r_total)  # Whiteboard math
        print(f"\nResult: Voltage drop across the {target_r} Ohm resistor is {v_drop:.4f} V")

    elif mode == '2':
        # CURRENT DIVIDER TRACK
        inverse_sum = 0
        for r in resistors:
            inverse_sum += (1 / r)
        r_eq = 1 / inverse_sum  # We need the parallel R_eq for the current divider

        i_branch = source_val * (r_eq / target_r)  # Whiteboard math
        print(f"\nResult: Current through the {target_r} Ohm branch is {i_branch:.4f} A")

# --- THE DEPARTMENT MANAGER ---
def dc_menu():
    # THE DEPARTMENT SHIFT: Keeps you in the DC room until you type 0
    while True:
        print("\n" + "-" * 40)
        print("🔋 MODULE 1: DC CIRCUIT ENGINE 🔋")
        print("-" * 40)
        print("1. Ohm's Law & Power")
        print("2. Resistor Equivalence")
        print("3. Voltage/Current Dividers")
        print("0. RETURN TO MAIN LOBBY")
        print("-" * 40)

        # TUPPERWARE: Grabbing the user's choice for this specific room
        dc_choice = input("Select a DC tool (0-3): ")

        # TRAIN DISPATCHER: Routing to the specific DC workers
        if dc_choice == '1':
            calculate_ohms_law()

        elif dc_choice == '2':
            calculate_resistor_equivalence()

        elif dc_choice == '3':
            calculate_dividers()

        elif dc_choice == '0':
            print("\nReturning to Main Factory Lobby...")
            break  # EMERGENCY BRAKE: Shatters the DC loop, sending you back to main.py

        else:
            print("\n[!] Invalid selection. Enter 0-3.")