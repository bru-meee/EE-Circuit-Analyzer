# visual_engine.py

# TIER 6: OFFSHORE IMPORTS
import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as log


# ==========================================
# [ MODULE 1 ] DC TOPOLOGIES
# ==========================================
def draw_dc_topologies():
    print("\n--- 🖨️ HOLOGRAM PRINTER: DC CIRCUITS ---")
    print("1. Series Resistor Circuit (Voltage Divider)")
    print("2. Parallel Resistor Circuit (Current Divider)")
    mode = input("Select track (1-2): ")

    try:
        if mode == '1':
            v_s = input("Enter Source Voltage (e.g., 12V): ")
            r1 = input("Enter R1 (e.g., 10Ω): ")
            r2 = input("Enter R2 (e.g., 20Ω): ")

            with schemdraw.Drawing(show=True) as d:
                d += elm.SourceV().up().label(v_s)
                d += elm.Resistor().right().label(r1)
                d += elm.Resistor().down().label(r2)
                d += elm.Line().left()
                d += elm.Ground()
                d.save('DC_Series_Hologram.png')
                print("\n[SUCCESS] Saved as 'DC_Series_Hologram.png'")

        elif mode == '2':
            i_s = input("Enter Source Current (e.g., 5A): ")
            r1 = input("Enter R1 (e.g., 10Ω): ")
            r2 = input("Enter R2 (e.g., 20Ω): ")

            with schemdraw.Drawing(show=True) as d:
                d += elm.SourceI().up().label(i_s)
                d += elm.Line().right().length(2)
                d.push()  # Save this node
                d += elm.Resistor().down().label(r1)
                d += elm.Line().left().length(2)
                d += elm.Ground()
                d.pop()  # Return to saved node
                d += elm.Line().right().length(2)
                d += elm.Resistor().down().label(r2)
                d += elm.Line().left().length(2)
                d.save('DC_Parallel_Hologram.png')
                print("\n[SUCCESS] Saved as 'DC_Parallel_Hologram.png'")
        else:
            print("\n[!] Invalid track.")
    except Exception as e:
        print(f"\n[!] PRINTER JAM: {e}")


# ==========================================
# [ MODULE 2 ] NETWORK THEOREMS
# ==========================================
def draw_equivalent_circuits():
    print("\n--- 🖨️ HOLOGRAM PRINTER: EQUIVALENT CIRCUITS ---")
    print("1. Thevenin Equivalent")
    print("2. Norton Equivalent")
    mode = input("Select track (1-2): ")

    try:
        if mode == '1':
            v_th = input("Enter V_th: ")
            r_th = input("Enter R_th: ")

            with schemdraw.Drawing(show=True) as d:
                d += elm.SourceV().up().label(v_th)
                d += elm.Resistor().right().label(r_th)
                d += elm.Dot().label('A')
                d += elm.Resistor().down().label('R_Load').idot()
                d += elm.Line().left()
                d += elm.Ground()
                d.save('Thevenin_Hologram.png')
                print("\n[SUCCESS] Saved as 'Thevenin_Hologram.png'")

        elif mode == '2':
            i_n = input("Enter I_n: ")
            r_th = input("Enter R_th: ")

            with schemdraw.Drawing(show=True) as d:
                d += elm.SourceI().up().label(i_n)
                d += elm.Line().right().length(2)
                d.push()
                d += elm.Resistor().down().label(r_th)
                d += elm.Line().left().length(2)
                d += elm.Ground()
                d.pop()
                d += elm.Line().right().length(2)
                d += elm.Dot().label('A', 'top')
                d += elm.Resistor().down().label('R_Load')
                d += elm.Dot().label('B', 'bottom')
                d += elm.Line().left().length(2)
                d.save('Norton_Hologram.png')
                print("\n[SUCCESS] Saved as 'Norton_Hologram.png'")
    except Exception as e:
        print(f"\n[!] PRINTER JAM: {e}")


# ==========================================
# [ MODULE 3 & 4 ] AC & TRANSIENT CIRCUITS
# ==========================================
def draw_transient_ac_circuits():
    print("\n--- 🖨️ HOLOGRAM PRINTER: TRANSIENT & AC CIRCUITS ---")
    print("1. First-Order RC Circuit")
    print("2. First-Order RL Circuit")
    print("3. Second-Order RLC Circuit (Series)")
    mode = input("Select track (1-3): ")

    try:
        with schemdraw.Drawing(show=True) as d:
            if mode == '1':
                d += elm.SourceV().up().label('Vs')
                d += elm.Switch().right().label('t=0')
                d += elm.Resistor().right().label('R')
                d += elm.Capacitor().down().label('C')
                d += elm.Line().left().tox(d.elements[0].start)
                d += elm.Ground()
                d.save('RC_Transient_Hologram.png')
                print("\n[SUCCESS] Saved as 'RC_Transient_Hologram.png'")

            elif mode == '2':
                d += elm.SourceV().up().label('Vs')
                d += elm.Switch().right().label('t=0')
                d += elm.Resistor().right().label('R')
                d += elm.Inductor().down().label('L')
                d += elm.Line().left().tox(d.elements[0].start)
                d += elm.Ground()
                d.save('RL_Transient_Hologram.png')
                print("\n[SUCCESS] Saved as 'RL_Transient_Hologram.png'")

            elif mode == '3':
                d += elm.SourceSin().up().label('Vs (AC)')
                d += elm.Resistor().right().label('R')
                d += elm.Inductor().right().label('L')
                d += elm.Capacitor().down().label('C')
                d += elm.Line().left().tox(d.elements[0].start)
                d += elm.Ground()
                d.save('RLC_AC_Hologram.png')
                print("\n[SUCCESS] Saved as 'RLC_AC_Hologram.png'")
    except Exception as e:
        print(f"\n[!] PRINTER JAM: {e}")


# ==========================================
# [ MODULE 4 ] OP-AMPS
# ==========================================
def draw_op_amps():
    print("\n--- 🖨️ HOLOGRAM PRINTER: OPERATIONAL AMPLIFIERS ---")
    print("1. Inverting Amplifier")
    print("2. Non-Inverting Amplifier")
    mode = input("Select track (1-2): ")

    try:
        with schemdraw.Drawing(show=True) as d:
            op = d.add(elm.Opamp(sign=True))

            if mode == '1':  # Inverting
                d += elm.Resistor().left().at(op.in1).label('R_in').idot()
                d += elm.SourceV().down().label('Vin')
                d += elm.Ground()
                d += elm.Line().down().at(op.in2).length(1)
                d += elm.Ground()
                d += elm.Line().up().at(op.in1).length(1.5)
                d += elm.Resistor().right().label('R_f')
                d += elm.Line().down().toy(op.out)
                d += elm.Line().left().tox(op.out).dot()
                d += elm.Line().right().at(op.out).length(1).label('Vout', 'right')
                d.save('OpAmp_Inverting_Hologram.png')
                print("\n[SUCCESS] Saved as 'OpAmp_Inverting_Hologram.png'")

            elif mode == '2':  # Non-Inverting
                d += elm.Line().left().at(op.in2).length(1).idot()
                d += elm.SourceV().down().label('Vin')
                d += elm.Ground()
                d += elm.Resistor().down().at(op.in1).label('R_in')
                d += elm.Ground()
                d += elm.Line().up().at(op.in1).length(1.5)
                d += elm.Resistor().right().label('R_f')
                d += elm.Line().down().toy(op.out)
                d += elm.Line().left().tox(op.out).dot()
                d += elm.Line().right().at(op.out).length(1).label('Vout', 'right')
                d.save('OpAmp_NonInverting_Hologram.png')
                print("\n[SUCCESS] Saved as 'OpAmp_NonInverting_Hologram.png'")
    except Exception as e:
        print(f"\n[!] PRINTER JAM: {e}")


# ==========================================
# [ MODULE 5 ] DIGITAL LOGIC
# ==========================================
def draw_logic_gates():
    print("\n--- 🖨️ HOLOGRAM PRINTER: DIGITAL LOGIC GATES ---")
    print("Generates all standard 2-input logic gates.")

    try:
        with schemdraw.Drawing(show=True) as d:
            d.config(fontsize=12)
            # Spacing them out on a grid
            d += log.And().at((0, 0)).label('AND', 'center')
            d += log.Nand().at((4, 0)).label('NAND', 'center')
            d += log.Or().at((0, -3)).label('OR', 'center')
            d += log.Nor().at((4, -3)).label('NOR', 'center')
            d += log.Xor().at((0, -6)).label('XOR', 'center')
            d += log.Not().at((4, -6)).label('NOT', 'center')

            d.save('Logic_Gates_Hologram.png')
            print("\n[SUCCESS] Logic Gates Matrix saved as 'Logic_Gates_Hologram.png'")
    except Exception as e:
        print(f"\n[!] PRINTER JAM: {e}")


# ==========================================
# THE DEPARTMENT MANAGER
# ==========================================
def visual_menu():
    while True:
        print("\n" + "=" * 50)
        print("🖨️ MODULE 6: VISUAL ARCHITECTURE ENGINE 🖨️")
        print("=" * 50)
        print("1. DC Circuit Topologies (Module 1 mapped)")
        print("2. Equivalent Circuits (Module 2 mapped)")
        print("3. AC & Transient Circuits (Modules 3 & 4 mapped)")
        print("4. Operational Amplifiers (Module 4 mapped)")
        print("5. Digital Logic Gates (Module 5 mapped)")
        print("0. PULL LEVER TO RETURN TO MAIN LOBBY")
        print("=" * 50)

        choice = input("Select a Hologram Protocol (0-5): ")

        if choice == '1':
            draw_dc_topologies()
        elif choice == '2':
            draw_equivalent_circuits()
        elif choice == '3':
            draw_transient_ac_circuits()
        elif choice == '4':
            draw_op_amps()
        elif choice == '5':
            draw_logic_gates()
        elif choice == '0':
            print("\n>>> BREAK LEVER PULLED. Returning to Main Factory Lobby...")
            break
        else:
            print("\n[!] DISPATCHER ERROR: Invalid selection. Enter 0-5.")
