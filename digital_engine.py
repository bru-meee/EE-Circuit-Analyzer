# digital_engine.py

def logic_gate_simulator():
    # THE SUBCONTRACTOR: Generates truth tables for 2-input gates
    print("\n--- TRUTH TABLE GENERATOR ---")
    print("Select a Gate:")
    print("1. AND   2. OR    3. XOR")
    print("4. NAND  5. NOR   6. NOT (1-Input)")

    # TUPPERWARE: Catching the sticky note input from the user
    gate_choice = input("Enter gate (1-6): ")

    # TIER 2: THE VENDING MACHINE (Dictionary)
    # We load the exact gate names into specific numbered slots.
    gates = {'1': 'AND', '2': 'OR', '3': 'XOR', '4': 'NAND', '5': 'NOR', '6': 'NOT'}

    # TRAIN TRACK DISPATCHER: Checking if the user's choice exists in the vending machine
    if gate_choice not in gates:
        print("\n[!] Invalid gate selection. Train derailed.")
        return

    # PUNCHING THE KEYPAD: Dropping the selected gate name from the machine
    gate = gates[gate_choice]
    print(f"\n[{gate} GATE TRUTH TABLE]")

    # TRAIN TRACK DISPATCHER: Splitting the path between 1-input (NOT) and 2-input gates
    if gate == 'NOT':
        print(" A | OUT")
        print("---|---")
        # TIER 1: THE CONVEYOR BELT (for loop)
        # Picks up light switches (0 and 1) one at a time.
        for a in [0, 1]:
            # WHITEBOARD: Inverting the light switch
            out = int(not a)
            print(f" {a} |  {out}")
    else:
        print(" A | B | OUT")
        print("---|---|---")

        # TIER 1: NESTED CONVEYOR BELTS
        # The main belt (A) picks up a switch, then the sub-belt (B) runs a full cycle.
        # This mathematically forces every combination: 00, 01, 10, 11.
        for a in [0, 1]:
            for b in [0, 1]:

                # TRAIN TRACK DISPATCHER: Routing to the correct bitwise math
                if gate == 'AND':
                    out = a & b
                elif gate == 'OR':
                    out = a | b
                elif gate == 'XOR':
                    out = a ^ b
                elif gate == 'NAND':
                    out = int(not (a & b))
                elif gate == 'NOR':
                    out = int(not (a | b))

                # SHIPPING LABEL: Printing the final row of the truth table
                print(f" {a} | {b} |  {out}")


def binary_decimal_converter():
    # THE SUBCONTRACTOR: Handles translation between base-2 and base-10
    print("\n--- TRANSLATION MATRIX ---")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")

    # TUPPERWARE
    conv_choice = input("Select conversion (1-2): ")

    # TRAIN TRACK DISPATCHER
    if conv_choice == '1':
        bin_str = input("Enter a binary number (e.g., 1011): ")

        # TIER 5: THE SAFETY NET (try/except block)
        # If the user types "2" in binary, the factory catches the error instead of exploding.
        try:
            # WHITEBOARD: int() translates base-2 ink into a base-10 iron weight
            dec_val = int(bin_str, 2)
            print(f"\n[SUCCESS] Binary {bin_str} = Decimal {dec_val}")
        except ValueError:
            print("\n[!] FATAL ERROR: Invalid binary input. Only 0s and 1s allowed.")

    elif conv_choice == '2':
        # TIER 5: THE SAFETY NET
        try:
            # TUPPERWARE: Securing a heavy iron weight (int)
            dec_int = int(input("Enter a decimal integer (e.g., 25): "))

            # WHITEBOARD: bin() converts to binary, [2:] slices off the '0b' prefix
            bin_val = bin(dec_int)[2:]
            print(f"\n[SUCCESS] Decimal {dec_int} = Binary {bin_val}")
        except ValueError:
            print("\n[!] INPUT ERROR: The factory only accepts whole numbers.")
    else:
        print("\n[!] Invalid selection.")


# --- THE DEPARTMENT MANAGER ---
def digital_menu():
    # THE DEPARTMENT SHIFT: Keeps the user in Module 5 until they clock out
    while True:
        print("\n" + "-" * 40)
        print("🖥️ MODULE 5: DIGITAL LOGIC ENGINE 🖥️")
        print("-" * 40)
        print("1. Logic Gate Simulator (Truth Tables)")
        print("2. Binary <-> Decimal Converter")
        print("0. RETURN TO MAIN LOBBY")
        print("-" * 40)

        # TUPPERWARE
        choice = input("Select a Digital Logic tool (0-2): ")

        # TRAIN DISPATCHER: Routing to the appropriate subcontractor
        if choice == '1':
            logic_gate_simulator()
        elif choice == '2':
            binary_decimal_converter()
        elif choice == '0':
            print("\nReturning to Main Factory Lobby...")
            break  # EMERGENCY BRAKE: Exits the loop
        else:
            print("\n[!] Invalid selection. Enter 0-2.")