# --- WELCOME TO THE EE CIRCUIT ANALYZER V1.0 ---

# HIRING THE MANAGER: We only need to import the 'dc_menu' manager now.
# The manager will handle calling the individual workers.
from dc_engine import dc_menu
from network_engine import network_menu
from ac_engine import ac_menu
from component_engine import component_menu
from digital_engine import digital_menu

def main_menu():
    # THE FACTORY SHIFT: Keeps the main lobby open
    while True:
        print("\n" + "=" * 40)
        print("⚡ WELCOME TO THE EE CIRCUIT ANALYZER ⚡")
        print("=" * 40)
        print("1. DC Circuit Basics (Module 1)")
        print("2. Advanced Network Theorems (Module 2)")
        print("3. AC & Complex Numbers (Module 3)")
        print("4. Component Behavior (Module 4)")
        print("5. Digital Logic (Module 5)")
        print("0. EXIT PROTOCOL")
        print("=" * 40)

        # TUPPERWARE: Grabbing the user's main module command
        choice = input("Select a module (0-5): ")

        # THE MASTER TRAIN DISPATCHER: Routing the user to the correct Department Room
        if choice == '1':
            print("\n>>> ENTERING DC CIRCUIT ROOM...")
            dc_menu()  # Calling the Module 1 Manager

        elif choice == '2':
            print("\n>>> ENTERING NETWORK THEOREMS ROOM...")
            network_menu()  # Calling the Module 2 Manager

        elif choice == '3':
            print("\n>>> ENTERING AC CIRCUITS ROOM...")
            ac_menu() # Calling the Module 3 Manager

        elif choice == '4':
            print("\n>>> ENTERING COMPONENT ROOM...")
            component_menu() # Calling the Module 4 Manager

        elif choice == '5':
            print("\n>>> ENTERING DIGITAL LOGIC ROOM...")
            digital_menu() # Calling the Module 5 Manager

        elif choice == '0':
            print("\nShutting down the factory. Goodbye.")
            break  # EMERGENCY BRAKE: Turns off the whole factory

        else:
            print("\n[!] INVALID COMMAND. Please enter a number from 0 to 5.")


# IGNITION KEY: Starts the Front Desk
main_menu()