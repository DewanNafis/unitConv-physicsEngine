"""Interactive Menu-Based Physics & Unit Conversion System.

This module provides an interactive menu for:
- Basic unit conversions
- Derived physics formulas
- Advanced physics calculations
- Motion simulations
"""

from converters.basic import m_to_cm, cm_to_m, kg_to_g, g_to_kg, c_to_f, f_to_c, s_to_min, min_to_s
from physics.derived import (
    speed, acceleration, density,
    momentum, kinetic_energy, potential_energy,
    impulse, frequency, period
)
from physics.advanced import (
    force, work, power, pressure,
    torque, angular_velocity, centripetal_force,
    gravitational_force, elastic_potential_energy,
    efficiency, electric_power
)
from simulation.motion import falling_body, projectile_range
from physics import unit_aware
from converters.units import Distance, Mass, Velocity
import math
import sys


def print_section(title: str):
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print('=' * 60)


def demo_basic_conversions():
    """Demonstrate basic unit conversions."""
    print_section("LEVEL 1: Basic Unit Conversions")
    
    print("\n📏 Length Conversions:")
    print(f"  5 meters = {m_to_cm(5)} centimeters")
    print(f"  250 centimeters = {cm_to_m(250)} meters")
    
    print("\n⚖️  Mass Conversions:")
    print(f"  2.5 kilograms = {kg_to_g(2.5)} grams")
    print(f"  1500 grams = {g_to_kg(1500)} kilograms")
    
    print("\n🌡️  Temperature Conversions:")
    print(f"  0°C = {c_to_f(0):.1f}°F")
    print(f"  100°C = {c_to_f(100):.1f}°F")
    print(f"  32°F = {f_to_c(32):.1f}°C")
    print(f"  212°F = {f_to_c(212):.1f}°C")
    
    print("\n⏱️  Time Conversions:")
    print(f"  120 seconds = {s_to_min(120)} minutes")
    print(f"  3 minutes = {min_to_s(3)} seconds")


def demo_derived_physics():
    """Demonstrate derived physics formulas."""
    print_section("LEVEL 2: Derived Physics Formulas")
    
    print("\n🏃 Speed Calculation:")
    dist = 100
    time = 10
    v = speed(dist, time)
    print(f"  Distance: {dist}m, Time: {time}s")
    print(f"  Speed: {v} m/s")
    
    print("\n🚗 Acceleration Calculation:")
    v_i = 0
    v_f = 30
    time = 5
    a = acceleration(v_f, v_i, time)
    print(f"  Initial velocity: {v_i} m/s, Final velocity: {v_f} m/s, Time: {time}s")
    print(f"  Acceleration: {a} m/s²")
    
    print("\n📦 Density Calculation:")
    mass = 7.8
    volume = 0.001
    rho = density(mass, volume)
    print(f"  Mass: {mass} kg, Volume: {volume} m³")
    print(f"  Density: {rho} kg/m³")
    
    print("\n💨 Momentum Calculation:")
    mass = 10
    velocity = 15
    p = momentum(mass, velocity)
    print(f"  Mass: {mass} kg, Velocity: {velocity} m/s")
    print(f"  Momentum: {p} kg·m/s")
    
    print("\n⚡ Kinetic Energy Calculation:")
    mass = 5
    velocity = 10
    ke = kinetic_energy(mass, velocity)
    print(f"  Mass: {mass} kg, Velocity: {velocity} m/s")
    print(f"  Kinetic Energy: {ke} J")
    
    print("\n⛰️  Potential Energy Calculation:")
    mass = 10
    height = 20
    pe = potential_energy(mass, height)
    print(f"  Mass: {mass} kg, Height: {height} m")
    print(f"  Potential Energy: {pe:.1f} J")
    
    print("\n🥊 Impulse Calculation:")
    force_val = 100
    time = 0.5
    j = impulse(force_val, time)
    print(f"  Force: {force_val} N, Time: {time} s")
    print(f"  Impulse: {j} N·s")
    
    print("\n🔄 Frequency & Period:")
    freq = 5
    per = period(freq)
    print(f"  Frequency: {freq} Hz → Period: {per} s")
    per = 0.2
    freq = frequency(per)
    print(f"  Period: {per} s → Frequency: {freq} Hz")


def demo_advanced_physics():
    """Demonstrate advanced physics calculations."""
    print_section("LEVEL 3: Advanced Physics")
    
    print("\n💪 Force Calculation (Newton's 2nd Law):")
    mass = 10
    accel = 5
    f = force(mass, accel)
    print(f"  Mass: {mass} kg, Acceleration: {accel} m/s²")
    print(f"  Force: {f} N")
    
    print("\n⚡ Work Calculation:")
    force_val = 50
    distance = 10
    w = work(force_val, distance)
    print(f"  Force: {force_val} N, Distance: {distance} m")
    print(f"  Work: {w} J")
    
    print("\n🔋 Power Calculation:")
    work_val = 500
    time = 10
    p = power(work_val, time)
    print(f"  Work: {work_val} J, Time: {time} s")
    print(f"  Power: {p} W")
    
    print("\n🌊 Pressure Calculation:")
    force_val = 1000
    area = 2
    press = pressure(force_val, area)
    print(f"  Force: {force_val} N, Area: {area} m²")
    print(f"  Pressure: {press} Pa")
    
    print("\n🔧 Torque Calculation:")
    force_val = 50
    radius = 0.5
    tau = torque(force_val, radius)
    print(f"  Force: {force_val} N, Radius: {radius} m")
    print(f"  Torque: {tau} N·m")
    
    print("\n🌀 Angular Velocity Calculation:")
    angle = math.pi
    time = 2
    omega = angular_velocity(angle, time)
    print(f"  Angle: π radians, Time: {time} s")
    print(f"  Angular Velocity: {omega:.3f} rad/s")
    
    print("\n🎢 Centripetal Force Calculation:")
    mass = 50
    velocity = 10
    radius = 5
    fc = centripetal_force(mass, velocity, radius)
    print(f"  Mass: {mass} kg, Velocity: {velocity} m/s, Radius: {radius} m")
    print(f"  Centripetal Force: {fc} N")
    
    print("\n🌍 Gravitational Force Calculation:")
    m1 = 1000
    m2 = 2000
    dist = 10
    fg = gravitational_force(m1, m2, dist)
    print(f"  Mass 1: {m1} kg, Mass 2: {m2} kg, Distance: {dist} m")
    print(f"  Gravitational Force: {fg:.2e} N")
    
    print("\n🏹 Elastic Potential Energy (Spring):")
    spring_k = 200
    displacement = 0.5
    epe = elastic_potential_energy(spring_k, displacement)
    print(f"  Spring constant: {spring_k} N/m, Displacement: {displacement} m")
    print(f"  Elastic PE: {epe} J")
    
    print("\n⚙️  Efficiency Calculation:")
    output = 800
    input_val = 1000
    eff = efficiency(output, input_val)
    print(f"  Output energy: {output} J, Input energy: {input_val} J")
    print(f"  Efficiency: {eff}%")
    
    print("\n⚡ Electric Power Calculation:")
    voltage = 120
    current = 5
    ep = electric_power(voltage, current)
    print(f"  Voltage: {voltage} V, Current: {current} A")
    print(f"  Electric Power: {ep} W")


def demo_simulations():
    """Demonstrate motion simulations."""
    print_section("LEVEL 4: Motion Simulations")
    
    print("\n🪂 Falling Body:")
    for t in [1, 2, 3]:
        dist = falling_body(t)
        print(f"  After {t}s: {dist:.2f} meters fallen")
    
    print("\n🎯 Projectile Range:")
    initial_velocity = 20
    for angle in [30, 45, 60]:
        range_val = projectile_range(initial_velocity, angle)
        print(f"  Launch angle {angle}° at {initial_velocity} m/s: Range = {range_val:.2f} m")


def get_float_input(prompt: str) -> float:
    """Get and validate float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def clear_screen():
    """Clear the screen (works on most terminals)."""
    print("\n" * 2)


def pause():
    """Pause and wait for user input."""
    input("\n📝 Press Enter to continue...")


def menu_unit_conversions():
    """Interactive menu for unit conversions."""
    while True:
        clear_screen()
        print_section("LEVEL 1: Unit Conversions")
        print("\n1. Length (meters ↔ centimeters)")
        print("2. Mass (kilograms ↔ grams)")
        print("3. Temperature (Celsius ↔ Fahrenheit)")
        print("4. Time (seconds ↔ minutes)")
        print("0. Back to Main Menu")
        
        choice = input("\n🎯 Select conversion type: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            print("\n📏 Length Conversion")
            print("1. Meters to Centimeters")
            print("2. Centimeters to Meters")
            sub_choice = input("Select: ").strip()
            if sub_choice == "1":
                value = get_float_input("Enter meters: ")
                result = m_to_cm(value)
                print(f"✅ {value} m = {result} cm")
            elif sub_choice == "2":
                value = get_float_input("Enter centimeters: ")
                result = cm_to_m(value)
                print(f"✅ {value} cm = {result} m")
            pause()
        elif choice == "2":
            print("\n⚖️  Mass Conversion")
            print("1. Kilograms to Grams")
            print("2. Grams to Kilograms")
            sub_choice = input("Select: ").strip()
            if sub_choice == "1":
                value = get_float_input("Enter kilograms: ")
                result = kg_to_g(value)
                print(f"✅ {value} kg = {result} g")
            elif sub_choice == "2":
                value = get_float_input("Enter grams: ")
                result = g_to_kg(value)
                print(f"✅ {value} g = {result} kg")
            pause()
        elif choice == "3":
            print("\n🌡️  Temperature Conversion")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            sub_choice = input("Select: ").strip()
            if sub_choice == "1":
                value = get_float_input("Enter Celsius: ")
                result = c_to_f(value)
                print(f"✅ {value}°C = {result:.2f}°F")
            elif sub_choice == "2":
                value = get_float_input("Enter Fahrenheit: ")
                result = f_to_c(value)
                print(f"✅ {value}°F = {result:.2f}°C")
            pause()
        elif choice == "4":
            print("\n⏱️  Time Conversion")
            print("1. Seconds to Minutes")
            print("2. Minutes to Seconds")
            sub_choice = input("Select: ").strip()
            if sub_choice == "1":
                value = get_float_input("Enter seconds: ")
                result = s_to_min(value)
                print(f"✅ {value} s = {result} min")
            elif sub_choice == "2":
                value = get_float_input("Enter minutes: ")
                result = min_to_s(value)
                print(f"✅ {value} min = {result} s")
            pause()


def menu_derived_physics():
    """Interactive menu for derived physics formulas."""
    while True:
        clear_screen()
        print_section("LEVEL 2: Derived Physics Formulas")
        print("\n1. Speed (v = d / t)")
        print("2. Acceleration (a = (v_f - v_i) / t)")
        print("3. Density (ρ = m / V)")
        print("4. Momentum (p = m × v)")
        print("5. Kinetic Energy (KE = 0.5 × m × v²)")
        print("6. Potential Energy (PE = m × g × h)")
        print("7. Impulse (J = F × Δt)")
        print("8. Frequency (f = 1 / T)")
        print("9. Period (T = 1 / f)")
        print("0. Back to Main Menu")
        
        choice = input("\n🎯 Select formula: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            print("\n🏃 Speed Calculation")
            distance = get_float_input("Enter distance (m): ")
            time = get_float_input("Enter time (s): ")
            try:
                result = speed(distance, time)
                print(f"✅ Speed = {result:.2f} m/s")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "2":
            print("\n🚗 Acceleration Calculation")
            v_i = get_float_input("Enter initial velocity (m/s): ")
            v_f = get_float_input("Enter final velocity (m/s): ")
            time = get_float_input("Enter time (s): ")
            try:
                result = acceleration(v_f, v_i, time)
                print(f"✅ Acceleration = {result:.2f} m/s²")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "3":
            print("\n📦 Density Calculation")
            mass = get_float_input("Enter mass (kg): ")
            volume = get_float_input("Enter volume (m³): ")
            try:
                result = density(mass, volume)
                print(f"✅ Density = {result:.2f} kg/m³")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "4":
            print("\n💨 Momentum Calculation")
            mass = get_float_input("Enter mass (kg): ")
            velocity = get_float_input("Enter velocity (m/s): ")
            result = momentum(mass, velocity)
            print(f"✅ Momentum = {result:.2f} kg·m/s")
            pause()
        elif choice == "5":
            print("\n⚡ Kinetic Energy Calculation")
            mass = get_float_input("Enter mass (kg): ")
            velocity = get_float_input("Enter velocity (m/s): ")
            result = kinetic_energy(mass, velocity)
            print(f"✅ Kinetic Energy = {result:.2f} J")
            pause()
        elif choice == "6":
            print("\n⛰️  Potential Energy Calculation")
            mass = get_float_input("Enter mass (kg): ")
            height = get_float_input("Enter height (m): ")
            result = potential_energy(mass, height)
            print(f"✅ Potential Energy = {result:.2f} J")
            pause()
        elif choice == "7":
            print("\n🥊 Impulse Calculation")
            force_val = get_float_input("Enter force (N): ")
            time = get_float_input("Enter time (s): ")
            result = impulse(force_val, time)
            print(f"✅ Impulse = {result:.2f} N·s")
            pause()
        elif choice == "8":
            print("\n🔄 Frequency Calculation")
            period_val = get_float_input("Enter period (s): ")
            try:
                result = frequency(period_val)
                print(f"✅ Frequency = {result:.2f} Hz")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "9":
            print("\n� Period Calculation")
            freq_val = get_float_input("Enter frequency (Hz): ")
            try:
                result = period(freq_val)
                print(f"✅ Period = {result:.2f} s")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()


def menu_advanced_physics():
    """Interactive menu for advanced physics calculations."""
    while True:
        clear_screen()
        print_section("LEVEL 3: Advanced Physics")
        print("\n1. Force (F = m × a)")
        print("2. Work (W = F × d)")
        print("3. Power (P = W / t)")
        print("4. Pressure (P = F / A)")
        print("5. Torque (τ = F × r)")
        print("6. Angular Velocity (ω = θ / t)")
        print("7. Centripetal Force (F_c = (m × v²) / r)")
        print("8. Gravitational Force (F = G × (m₁ × m₂) / r²)")
        print("9. Elastic PE (PE = 0.5 × k × x²)")
        print("10. Efficiency (η = (E_out / E_in) × 100%)")
        print("11. Electric Power (P = V × I)")
        print("0. Back to Main Menu")
        
        choice = input("\n🎯 Select formula: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            print("\n💪 Force Calculation")
            mass = get_float_input("Enter mass (kg): ")
            accel = get_float_input("Enter acceleration (m/s²): ")
            result = force(mass, accel)
            print(f"✅ Force = {result:.2f} N")
            pause()
        elif choice == "2":
            print("\n⚡ Work Calculation")
            force_val = get_float_input("Enter force (N): ")
            distance = get_float_input("Enter distance (m): ")
            result = work(force_val, distance)
            print(f"✅ Work = {result:.2f} J")
            pause()
        elif choice == "3":
            print("\n🔋 Power Calculation")
            work_val = get_float_input("Enter work (J): ")
            time = get_float_input("Enter time (s): ")
            try:
                result = power(work_val, time)
                print(f"✅ Power = {result:.2f} W")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "4":
            print("\n🌊 Pressure Calculation")
            force_val = get_float_input("Enter force (N): ")
            area = get_float_input("Enter area (m²): ")
            try:
                result = pressure(force_val, area)
                print(f"✅ Pressure = {result:.2f} Pa")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "5":
            print("\n🔧 Torque Calculation")
            force_val = get_float_input("Enter force (N): ")
            radius = get_float_input("Enter radius (m): ")
            result = torque(force_val, radius)
            print(f"✅ Torque = {result:.2f} N·m")
            pause()
        elif choice == "6":
            print("\n🌀 Angular Velocity Calculation")
            angle = get_float_input("Enter angle (radians): ")
            time = get_float_input("Enter time (s): ")
            try:
                result = angular_velocity(angle, time)
                print(f"✅ Angular Velocity = {result:.3f} rad/s")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "7":
            print("\n🎢 Centripetal Force Calculation")
            mass = get_float_input("Enter mass (kg): ")
            velocity = get_float_input("Enter velocity (m/s): ")
            radius = get_float_input("Enter radius (m): ")
            try:
                result = centripetal_force(mass, velocity, radius)
                print(f"✅ Centripetal Force = {result:.2f} N")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "8":
            print("\n🌍 Gravitational Force Calculation")
            m1 = get_float_input("Enter mass 1 (kg): ")
            m2 = get_float_input("Enter mass 2 (kg): ")
            dist = get_float_input("Enter distance (m): ")
            try:
                result = gravitational_force(m1, m2, dist)
                print(f"✅ Gravitational Force = {result:.2e} N")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "9":
            print("\n🏹 Elastic Potential Energy")
            spring_k = get_float_input("Enter spring constant (N/m): ")
            displacement = get_float_input("Enter displacement (m): ")
            result = elastic_potential_energy(spring_k, displacement)
            print(f"✅ Elastic PE = {result:.2f} J")
            pause()
        elif choice == "10":
            print("\n⚙️  Efficiency Calculation")
            output = get_float_input("Enter output energy (J): ")
            input_val = get_float_input("Enter input energy (J): ")
            try:
                result = efficiency(output, input_val)
                print(f"✅ Efficiency = {result:.2f}%")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "11":
            print("\n⚡ Electric Power Calculation")
            voltage = get_float_input("Enter voltage (V): ")
            current = get_float_input("Enter current (A): ")
            result = electric_power(voltage, current)
            print(f"✅ Electric Power = {result:.2f} W")
            pause()


def menu_simulations():
    """Interactive menu for motion simulations."""
    while True:
        clear_screen()
        print_section("LEVEL 4: Motion Simulations")
        print("\n1. Falling Body (d = 0.5 × g × t²)")
        print("2. Projectile Range (R = (u² × sin(2θ)) / g)")
        print("0. Back to Main Menu")
        
        choice = input("\n🎯 Select simulation: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            print("\n🪂 Falling Body Simulation")
            time = get_float_input("Enter time (s): ")
            try:
                result = falling_body(time)
                print(f"✅ Distance fallen = {result:.2f} meters")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()
        elif choice == "2":
            print("\n🎯 Projectile Range Simulation")
            velocity = get_float_input("Enter initial velocity (m/s): ")
            angle = get_float_input("Enter launch angle (degrees): ")
            try:
                result = projectile_range(velocity, angle)
                print(f"✅ Projectile Range = {result:.2f} meters")
            except ValueError as e:
                print(f"❌ Error: {e}")
            pause()


def run_all_demos():
    """Run all demonstrations (original functionality)."""
    clear_screen()
    print("\n" + "🔬" * 30)
    print("  Running All Demonstrations")
    print("🔬" * 30)
    
    demo_basic_conversions()
    demo_derived_physics()
    demo_advanced_physics()
    demo_simulations()
    
    print("\n" + "=" * 60)
    print("  ✅ All demonstrations completed successfully!")
    print("=" * 60)
    pause()


def auto_demonstration():
    """Run automatic demonstration with sample calculations."""
    clear_screen()
    print("\n" + "🎬" * 30)
    print("  Automatic Demonstration Mode")
    print("🎬" * 30)
    print("\nThis will showcase each level with example calculations.\n")
    
    import time
    
    def demo_pause(seconds=1.5):
        """Short pause for auto demo."""
        time.sleep(seconds)
    
    # Level 1: Unit Conversions
    print_section("LEVEL 1: Unit Conversions Demo")
    print("\n📏 Length Conversion:")
    print("   Converting 5 meters to centimeters...")
    demo_pause()
    print(f"   ✅ Result: {m_to_cm(5)} cm")
    demo_pause()
    
    print("\n⚖️  Mass Conversion:")
    print("   Converting 2.5 kilograms to grams...")
    demo_pause()
    print(f"   ✅ Result: {kg_to_g(2.5)} g")
    demo_pause()
    
    print("\n🌡️  Temperature Conversion:")
    print("   Converting 100°C to Fahrenheit...")
    demo_pause()
    print(f"   ✅ Result: {c_to_f(100):.1f}°F")
    demo_pause()
    
    print("\n⏱️  Time Conversion:")
    print("   Converting 120 seconds to minutes...")
    demo_pause()
    print(f"   ✅ Result: {s_to_min(120)} min")
    demo_pause(2)
    
    # Level 2: Derived Physics
    print_section("LEVEL 2: Derived Physics Demo")
    print("\n🏃 Speed Calculation:")
    print("   Distance: 100m, Time: 10s")
    demo_pause()
    v = speed(100, 10)
    print(f"   ✅ Speed: {v} m/s")
    demo_pause()
    
    print("\n💨 Momentum Calculation:")
    print("   Mass: 10kg, Velocity: 15m/s")
    demo_pause()
    p = momentum(10, 15)
    print(f"   ✅ Momentum: {p} kg·m/s")
    demo_pause()
    
    print("\n⚡ Kinetic Energy Calculation:")
    print("   Mass: 5kg, Velocity: 10m/s")
    demo_pause()
    ke = kinetic_energy(5, 10)
    print(f"   ✅ Kinetic Energy: {ke} J")
    demo_pause()
    
    print("\n⛰️  Potential Energy Calculation:")
    print("   Mass: 10kg, Height: 20m")
    demo_pause()
    pe = potential_energy(10, 20)
    print(f"   ✅ Potential Energy: {pe:.1f} J")
    demo_pause(2)
    
    # Level 3: Advanced Physics
    print_section("LEVEL 3: Advanced Physics Demo")
    print("\n💪 Force Calculation (Newton's 2nd Law):")
    print("   Mass: 10kg, Acceleration: 5m/s²")
    demo_pause()
    f = force(10, 5)
    print(f"   ✅ Force: {f} N")
    demo_pause()
    
    print("\n⚡ Work Calculation:")
    print("   Force: 50N, Distance: 10m")
    demo_pause()
    w = work(50, 10)
    print(f"   ✅ Work: {w} J")
    demo_pause()
    
    print("\n🔋 Power Calculation:")
    print("   Work: 500J, Time: 10s")
    demo_pause()
    pw = power(500, 10)
    print(f"   ✅ Power: {pw} W")
    demo_pause()
    
    print("\n🔧 Torque Calculation:")
    print("   Force: 50N, Radius: 0.5m")
    demo_pause()
    tau = torque(50, 0.5)
    print(f"   ✅ Torque: {tau} N·m")
    demo_pause()
    
    print("\n⚙️  Efficiency Calculation:")
    print("   Output: 800J, Input: 1000J")
    demo_pause()
    eff = efficiency(800, 1000)
    print(f"   ✅ Efficiency: {eff}%")
    demo_pause(2)
    
    # Level 4: Motion Simulations
    print_section("LEVEL 4: Motion Simulations Demo")
    print("\n🪂 Falling Body Simulation:")
    print("   Calculating distance fallen after 1s, 2s, and 3s...")
    demo_pause()
    for t in [1, 2, 3]:
        dist = falling_body(t)
        print(f"   ✅ After {t}s: {dist:.2f} meters")
        demo_pause(0.8)
    
    print("\n🎯 Projectile Range Simulation:")
    print("   Initial velocity: 20 m/s")
    demo_pause()
    print("   Calculating range at different angles...")
    demo_pause()
    for angle in [30, 45, 60]:
        range_val = projectile_range(20, angle)
        print(f"   ✅ Angle {angle}°: Range = {range_val:.2f} m")
        demo_pause(0.8)
    
    print("\n" + "=" * 60)
    print("  🎉 Automatic demonstration completed!")
    print("  All physics calculations executed successfully!")
    print("=" * 60)
    pause()


def menu_unit_aware_physics():
    """Interactive menu for unit-aware physics calculations."""
    while True:
        clear_screen()
        print_section("🌍 Unit-Aware Physics Calculations")
        print("\n✨ Enter values with units (e.g., '5 cm', '10 feet', '50 km/h')")
        print("\n1. Speed Calculation")
        print("2. Momentum Calculation")
        print("3. Kinetic Energy Calculation")
        print("4. Potential Energy Calculation")
        print("5. Force Calculation")
        print("6. Work Calculation")
        print("7. Centripetal Force Calculation")
        print("8. Gravitational Force Calculation")
        print("9. Falling Body Simulation")
        print("10. Projectile Range Simulation")
        print("0. Back to Main Menu")
        
        choice = input("\n🎯 Select calculation: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            print("\n📐 Speed Calculation (Speed = Distance / Time)")
            print("Supported distance units: m, cm, inch, feet, yard, km, mile")
            distance = input("Enter distance (e.g., '100 cm', '10 feet'): ").strip()
            time = get_float_input("Enter time (seconds): ")
            try:
                result = unit_aware.calculate_speed(distance, time)
                print(f"\n✅ Speed: {result:.2f} m/s")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        elif choice == "2":
            print("\n🚀 Momentum Calculation (p = m × v)")
            print("Supported mass units: kg, g, lb, oz")
            print("Supported velocity units: m/s, km/h, mph")
            mass = input("Enter mass (e.g., '5 kg', '10 lb'): ").strip()
            velocity = input("Enter velocity (e.g., '20 m/s', '50 km/h'): ").strip()
            try:
                result = unit_aware.calculate_momentum(mass, velocity)
                print(f"\n✅ Momentum: {result:.2f} kg⋅m/s")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        elif choice == "3":
            print("\n⚡ Kinetic Energy Calculation (KE = ½mv²)")
            print("Supported mass units: kg, g, lb, oz")
            print("Supported velocity units: m/s, km/h, mph")
            mass = input("Enter mass (e.g., '2 kg', '5 lb'): ").strip()
            velocity = input("Enter velocity (e.g., '10 m/s', '30 km/h'): ").strip()
            try:
                result = unit_aware.calculate_kinetic_energy(mass, velocity)
                print(f"\n✅ Kinetic Energy: {result:.2f} J")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        elif choice == "4":
            print("\n🏔️  Potential Energy Calculation (PE = mgh)")
            print("Supported mass units: kg, g, lb, oz")
            print("Supported height units: m, cm, inch, feet, yard")
            mass = input("Enter mass (e.g., '5 kg', '10 lb'): ").strip()
            height = input("Enter height (e.g., '10 m', '30 feet'): ").strip()
            try:
                result = unit_aware.calculate_potential_energy(mass, height)
                print(f"\n✅ Potential Energy: {result:.2f} J")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        elif choice == "5":
            print("\n💪 Force Calculation (F = ma)")
            print("Supported mass units: kg, g, lb, oz")
            mass = input("Enter mass (e.g., '10 kg', '20 lb'): ").strip()
            acceleration = get_float_input("Enter acceleration (m/s²): ")
            try:
                result = unit_aware.calculate_force(mass, acceleration)
                print(f"\n✅ Force: {result:.2f} N")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        elif choice == "6":
            print("\n🔧 Work Calculation (W = F × d)")
            force = get_float_input("Enter force (Newtons): ")
            print("Supported distance units: m, cm, inch, feet, yard")
            distance = input("Enter distance (e.g., '5 m', '10 feet'): ").strip()
            try:
                result = unit_aware.calculate_work(force, distance)
                print(f"\n✅ Work: {result:.2f} J")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        elif choice == "7":
            print("\n🌀 Centripetal Force (F = mv²/r)")
            print("Supported mass units: kg, g, lb, oz")
            print("Supported velocity units: m/s, km/h, mph")
            print("Supported radius units: m, cm, inch, feet")
            mass = input("Enter mass (e.g., '2 kg', '5 lb'): ").strip()
            velocity = input("Enter velocity (e.g., '15 m/s', '50 km/h'): ").strip()
            radius = input("Enter radius (e.g., '3 m', '10 feet'): ").strip()
            try:
                result = unit_aware.calculate_centripetal_force(mass, velocity, radius)
                print(f"\n✅ Centripetal Force: {result:.2f} N")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        elif choice == "8":
            print("\n🌍 Gravitational Force (F = G × m₁m₂/r²)")
            print("Supported mass units: kg, g, lb")
            print("Supported distance units: m, cm, km")
            mass1 = input("Enter first mass (e.g., '1000 kg'): ").strip()
            mass2 = input("Enter second mass (e.g., '2000 kg'): ").strip()
            distance = input("Enter distance (e.g., '10 m', '1000 cm'): ").strip()
            try:
                result = unit_aware.calculate_gravitational_force(mass1, mass2, distance)
                print(f"\n✅ Gravitational Force: {result:.2e} N")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        elif choice == "9":
            print("\n🪂 Falling Body Simulation")
            print("Calculate distance fallen under gravity")
            time = get_float_input("Enter time (seconds): ")
            try:
                result = unit_aware.simulate_falling_body(time)
                print(f"\n✅ Distance fallen: {result:.2f} m")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        elif choice == "10":
            print("\n🎯 Projectile Range Simulation")
            print("Supported velocity units: m/s, km/h, mph")
            velocity = input("Enter initial velocity (e.g., '20 m/s', '70 km/h'): ").strip()
            angle = get_float_input("Enter launch angle (degrees): ")
            try:
                result = unit_aware.simulate_projectile_range(velocity, angle)
                print(f"\n✅ Range: {result:.2f} m")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            pause()
        
        else:
            print("\n❌ Invalid choice! Please try again.")
            pause()


def main_menu():
    """Display and handle the main menu."""
    while True:
        clear_screen()
        print("\n" + "🔬" * 30)
        print("  Multi-Level Physics & Unit Conversion System")
        print("🔬" * 30)
        print("\n╔════════════════════════════════════════════════╗")
        print("║            MAIN MENU                           ║")
        print("╚════════════════════════════════════════════════╝")
        print("\n1. 📏 Level 1: Unit Conversions")
        print("2. ⚡ Level 2: Derived Physics Formulas")
        print("3. 🚀 Level 3: Advanced Physics")
        print("4. 🎯 Level 4: Motion Simulations")
        print("5. 🌍 Unit-Aware Physics")
        print("6. 🎬 Auto Demonstration (with examples)")
        print("7. 📊 Run All Demonstrations (detailed)")
        print("0. 🚪 Exit")
        
        choice = input("\n🎯 Select an option: ").strip()
        
        if choice == "0":
            print("\n👋 Thank you for using the Physics System!")
            print("   Goodbye! 🔬\n")
            sys.exit(0)
        elif choice == "1":
            menu_unit_conversions()
        elif choice == "2":
            menu_derived_physics()
        elif choice == "3":
            menu_advanced_physics()
        elif choice == "4":
            menu_simulations()
        elif choice == "5":
            menu_unit_aware_physics()
        elif choice == "6":
            auto_demonstration()
        elif choice == "7":
            run_all_demos()
        else:
            print("\n❌ Invalid choice! Please try again.")
            pause()


def main():
    """Run the interactive menu system."""
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye! 🔬\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
