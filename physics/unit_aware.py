"""Unit-aware physics calculations.

This module provides wrapper functions that accept inputs with units
and automatically convert them before performing physics calculations.
"""

from converters.units import Distance, Mass, Velocity, parse_input
from physics import derived, advanced
from simulation import motion


def calculate_speed(distance: str, time: float) -> float:
    """Calculate speed with unit-aware distance input.
    
    Args:
        distance: Distance with unit (e.g., "100 cm", "5 feet", "10 m")
        time: Time in seconds
        
    Returns:
        Speed in m/s
        
    Example:
        >>> calculate_speed("100 cm", 2.0)
        0.5
        >>> calculate_speed("10 feet", 1.0)
        3.048
    """
    distance_m = Distance.parse(distance)
    return derived.speed(distance_m, time)


def calculate_acceleration(velocity_change: str, time: float) -> float:
    """Calculate acceleration with unit-aware velocity input.
    
    Args:
        velocity_change: Change in velocity with unit (e.g., "50 km/h", "10 m/s")
        time: Time in seconds
        
    Returns:
        Acceleration in m/s²
    """
    velocity_mps = Velocity.parse(velocity_change)
    return derived.acceleration(velocity_mps, time)


def calculate_density(mass: str, volume: str) -> float:
    """Calculate density with unit-aware inputs.
    
    Args:
        mass: Mass with unit (e.g., "500 g", "2 kg", "5 lb")
        volume: Volume in cubic meters (m³) - for now just a float
        
    Returns:
        Density in kg/m³
    """
    mass_kg = Mass.parse(mass)
    return derived.density(mass_kg, float(volume))


def calculate_momentum(mass: str, velocity: str) -> float:
    """Calculate momentum with unit-aware inputs.
    
    Args:
        mass: Mass with unit (e.g., "5 kg", "10 lb")
        velocity: Velocity with unit (e.g., "20 m/s", "50 km/h")
        
    Returns:
        Momentum in kg⋅m/s
    """
    mass_kg = Mass.parse(mass)
    velocity_mps = Velocity.parse(velocity)
    return derived.momentum(mass_kg, velocity_mps)


def calculate_kinetic_energy(mass: str, velocity: str) -> float:
    """Calculate kinetic energy with unit-aware inputs.
    
    Args:
        mass: Mass with unit
        velocity: Velocity with unit
        
    Returns:
        Kinetic energy in Joules
    """
    mass_kg = Mass.parse(mass)
    velocity_mps = Velocity.parse(velocity)
    return derived.kinetic_energy(mass_kg, velocity_mps)


def calculate_potential_energy(mass: str, height: str) -> float:
    """Calculate potential energy with unit-aware inputs.
    
    Args:
        mass: Mass with unit
        height: Height with unit
        
    Returns:
        Potential energy in Joules
    """
    mass_kg = Mass.parse(mass)
    height_m = Distance.parse(height)
    return derived.potential_energy(mass_kg, height_m)


def calculate_impulse(force: float, time: float) -> float:
    """Calculate impulse (force is already in Newtons).
    
    Args:
        force: Force in Newtons
        time: Time in seconds
        
    Returns:
        Impulse in N⋅s
    """
    return derived.impulse(force, time)


def calculate_force(mass: str, acceleration: float) -> float:
    """Calculate force with unit-aware mass.
    
    Args:
        mass: Mass with unit
        acceleration: Acceleration in m/s²
        
    Returns:
        Force in Newtons
    """
    mass_kg = Mass.parse(mass)
    return advanced.force(mass_kg, acceleration)


def calculate_work(force: float, distance: str) -> float:
    """Calculate work with unit-aware distance.
    
    Args:
        force: Force in Newtons
        distance: Distance with unit
        
    Returns:
        Work in Joules
    """
    distance_m = Distance.parse(distance)
    return advanced.work(force, distance_m)


def calculate_power(work: float, time: float) -> float:
    """Calculate power (work is in Joules, time in seconds).
    
    Args:
        work: Work in Joules
        time: Time in seconds
        
    Returns:
        Power in Watts
    """
    return advanced.power(work, time)


def calculate_pressure(force: float, area: str) -> float:
    """Calculate pressure with unit-aware area.
    
    Args:
        force: Force in Newtons
        area: Area as string with unit (e.g., "2 m" means 2 m²)
        
    Returns:
        Pressure in Pascals
    """
    # For now, we'll treat area input as square meters
    try:
        area_m2 = float(area)
    except ValueError:
        parts = area.strip().split()
        if len(parts) == 2:
            area_m2 = float(parts[0])
        else:
            raise ValueError("Area should be a number or 'VALUE m' format")
    return advanced.pressure(force, area_m2)


def calculate_torque(force: float, distance: str) -> float:
    """Calculate torque with unit-aware lever arm distance.
    
    Args:
        force: Force in Newtons
        distance: Lever arm distance with unit
        
    Returns:
        Torque in N⋅m
    """
    distance_m = Distance.parse(distance)
    return advanced.torque(force, distance_m)


def calculate_centripetal_force(mass: str, velocity: str, radius: str) -> float:
    """Calculate centripetal force with unit-aware inputs.
    
    Args:
        mass: Mass with unit
        velocity: Velocity with unit
        radius: Radius with unit
        
    Returns:
        Centripetal force in Newtons
    """
    mass_kg = Mass.parse(mass)
    velocity_mps = Velocity.parse(velocity)
    radius_m = Distance.parse(radius)
    return advanced.centripetal_force(mass_kg, velocity_mps, radius_m)


def calculate_gravitational_force(mass1: str, mass2: str, distance: str) -> float:
    """Calculate gravitational force with unit-aware inputs.
    
    Args:
        mass1: First mass with unit
        mass2: Second mass with unit
        distance: Distance between masses with unit
        
    Returns:
        Gravitational force in Newtons
    """
    mass1_kg = Mass.parse(mass1)
    mass2_kg = Mass.parse(mass2)
    distance_m = Distance.parse(distance)
    return advanced.gravitational_force(mass1_kg, mass2_kg, distance_m)


def calculate_elastic_potential_energy(spring_constant: float, displacement: str) -> float:
    """Calculate elastic potential energy with unit-aware displacement.
    
    Args:
        spring_constant: Spring constant in N/m
        displacement: Displacement with unit
        
    Returns:
        Elastic potential energy in Joules
    """
    displacement_m = Distance.parse(displacement)
    return advanced.elastic_potential_energy(spring_constant, displacement_m)


def simulate_falling_body(time: float) -> float:
    """Simulate falling body - distance fallen under gravity.
    
    Args:
        time: Time in seconds
        
    Returns:
        Distance fallen in meters
    """
    return motion.falling_body(time)


def simulate_projectile_range(velocity: str, angle: float) -> float:
    """Simulate projectile range with unit-aware velocity.
    
    Args:
        velocity: Initial velocity with unit
        angle: Launch angle in degrees
        
    Returns:
        Range in meters
    """
    velocity_mps = Velocity.parse(velocity)
    return motion.projectile_range(velocity_mps, angle)


# Helper function for interactive input
def get_input_with_unit(prompt: str, quantity_type: str = 'distance') -> float:
    """Get user input with unit and convert to SI units.
    
    Args:
        prompt: Prompt to show user
        quantity_type: Type of quantity ('distance', 'mass', 'velocity')
        
    Returns:
        Value in SI units
    """
    while True:
        try:
            user_input = input(prompt).strip()
            return parse_input(user_input, quantity_type)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
