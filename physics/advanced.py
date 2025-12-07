"""Advanced physics calculations."""


def force(mass_kg: float, acceleration_m_s2: float) -> float:
    """Calculate force using Newton's second law.
    
    Formula: F = m * a
    
    Args:
        mass_kg: Mass in kilograms
        acceleration_m_s2: Acceleration in m/s²
        
    Returns:
        Force in Newtons (N)
    """
    return mass_kg * acceleration_m_s2


def work(force_n: float, distance_m: float) -> float:
    """Calculate work done by a force over a distance.
    
    Formula: W = F * d
    
    Args:
        force_n: Force in Newtons
        distance_m: Distance in meters
        
    Returns:
        Work in Joules (J)
    """
    return force_n * distance_m


def power(work_j: float, time_s: float) -> float:
    """Calculate power from work and time.
    
    Formula: P = W / t
    
    Args:
        work_j: Work in Joules
        time_s: Time in seconds
        
    Returns:
        Power in Watts (W)
        
    Raises:
        ValueError: If time is zero or negative
    """
    if time_s <= 0:
        raise ValueError("Time must be positive")
    return work_j / time_s


def pressure(force_n: float, area_m2: float) -> float:
    """Calculate pressure from force and area.
    
    Formula: P = F / A
    
    Args:
        force_n: Force in Newtons
        area_m2: Area in square meters
        
    Returns:
        Pressure in Pascals (Pa)
        
    Raises:
        ValueError: If area is zero or negative
    """
    if area_m2 <= 0:
        raise ValueError("Area must be positive")
    return force_n / area_m2


def torque(force_n: float, radius_m: float) -> float:
    """Calculate torque from force and lever arm distance.
    
    Formula: τ = F × r
    
    Args:
        force_n: Force in Newtons
        radius_m: Perpendicular distance from axis of rotation in meters
        
    Returns:
        Torque in Newton-meters (N·m)
    """
    return force_n * radius_m


def angular_velocity(angle_rad: float, time_s: float) -> float:
    """Calculate angular velocity from angle and time.
    
    Formula: ω = θ / t
    
    Args:
        angle_rad: Angle in radians
        time_s: Time in seconds
        
    Returns:
        Angular velocity in radians per second (rad/s)
        
    Raises:
        ValueError: If time is zero or negative
    """
    if time_s <= 0:
        raise ValueError("Time must be positive")
    return angle_rad / time_s


def centripetal_force(mass_kg: float, velocity_m_s: float, radius_m: float) -> float:
    """Calculate centripetal force for circular motion.
    
    Formula: F_c = (m × v²) / r
    
    Args:
        mass_kg: Mass in kilograms
        velocity_m_s: Tangential velocity in m/s
        radius_m: Radius of circular path in meters
        
    Returns:
        Centripetal force in Newtons (N)
        
    Raises:
        ValueError: If radius is zero or negative
    """
    if radius_m <= 0:
        raise ValueError("Radius must be positive")
    return (mass_kg * velocity_m_s ** 2) / radius_m


def gravitational_force(mass1_kg: float, mass2_kg: float, distance_m: float) -> float:
    """Calculate gravitational force between two masses.
    
    Formula: F = G × (m₁ × m₂) / r²
    Where G = 6.674 × 10⁻¹¹ N·m²/kg²
    
    Args:
        mass1_kg: First mass in kilograms
        mass2_kg: Second mass in kilograms
        distance_m: Distance between centers of mass in meters
        
    Returns:
        Gravitational force in Newtons (N)
        
    Raises:
        ValueError: If distance is zero or negative
    """
    G = 6.674e-11  # Gravitational constant
    if distance_m <= 0:
        raise ValueError("Distance must be positive")
    return G * (mass1_kg * mass2_kg) / (distance_m ** 2)


def elastic_potential_energy(spring_constant: float, displacement_m: float) -> float:
    """Calculate elastic potential energy in a spring.
    
    Formula: PE_elastic = 0.5 × k × x²
    
    Args:
        spring_constant: Spring constant in N/m
        displacement_m: Displacement from equilibrium in meters
        
    Returns:
        Elastic potential energy in Joules (J)
    """
    return 0.5 * spring_constant * displacement_m ** 2


def efficiency(output_energy: float, input_energy: float) -> float:
    """Calculate efficiency as a percentage.
    
    Formula: η = (E_out / E_in) × 100%
    
    Args:
        output_energy: Useful output energy in Joules
        input_energy: Total input energy in Joules
        
    Returns:
        Efficiency as a percentage (0-100)
        
    Raises:
        ValueError: If input energy is zero or negative
    """
    if input_energy <= 0:
        raise ValueError("Input energy must be positive")
    return (output_energy / input_energy) * 100


def electric_power(voltage_v: float, current_a: float) -> float:
    """Calculate electrical power.
    
    Formula: P = V × I
    
    Args:
        voltage_v: Voltage in Volts
        current_a: Current in Amperes
        
    Returns:
        Electrical power in Watts (W)
    """
    return voltage_v * current_a
