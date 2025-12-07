#!/usr/bin/env python3
"""Quick demonstration of unit-aware physics calculations."""

from physics.unit_aware import (
    calculate_speed, calculate_momentum, calculate_kinetic_energy,
    calculate_potential_energy, calculate_force, calculate_work,
    calculate_centripetal_force, simulate_projectile_range
)

print("=" * 70)
print("  🌍 UNIT-AWARE PHYSICS DEMONSTRATION")
print("=" * 70)

print("\n📏 SPEED CALCULATION")
print("   Example 1: 100 cm in 2 seconds")
result = calculate_speed("100 cm", 2.0)
print(f"   Result: {result} m/s")

print("   Example 2: 10 feet in 1 second")
result = calculate_speed("10 feet", 1.0)
print(f"   Result: {result:.3f} m/s")

print("\n🚀 MOMENTUM CALCULATION")
print("   Example 1: 5 kg at 20 m/s")
result = calculate_momentum("5 kg", "20 m/s")
print(f"   Result: {result} kg⋅m/s")

print("   Example 2: 10 pounds at 50 km/h")
result = calculate_momentum("10 lb", "50 km/h")
print(f"   Result: {result:.2f} kg⋅m/s")

print("\n⚡ KINETIC ENERGY")
print("   Example: 2 kg at 30 km/h")
result = calculate_kinetic_energy("2 kg", "30 km/h")
print(f"   Result: {result:.2f} J")

print("\n🏔️  POTENTIAL ENERGY")
print("   Example 1: 10 kg at 5 meters height")
result = calculate_potential_energy("10 kg", "5 m")
print(f"   Result: {result:.2f} J")

print("   Example 2: 20 pounds at 30 feet height")
result = calculate_potential_energy("20 lb", "30 feet")
print(f"   Result: {result:.2f} J")

print("\n💪 FORCE CALCULATION")
print("   Example: 5 pounds accelerating at 10 m/s²")
result = calculate_force("5 lb", 10)
print(f"   Result: {result:.2f} N")

print("\n🔧 WORK CALCULATION")
print("   Example: 50 N force over 10 feet")
result = calculate_work(50, "10 feet")
print(f"   Result: {result:.2f} J")

print("\n🌀 CENTRIPETAL FORCE")
print("   Example: 3 kg at 25 km/h in 2 meter radius")
result = calculate_centripetal_force("3 kg", "25 km/h", "2 m")
print(f"   Result: {result:.2f} N")

print("\n🎯 PROJECTILE RANGE")
print("   Example: Launched at 100 km/h at 45° angle")
result = simulate_projectile_range("100 km/h", 45)
print(f"   Result: {result:.2f} m")

print("\n" + "=" * 70)
print("  ✅ All calculations completed successfully!")
print("  📝 Units automatically converted to SI before calculation")
print("=" * 70)
