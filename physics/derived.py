"""Derived physics formulas."""


def speed(distance_m: float, time_s: float) -> float:
    """Calculate speed from distance and time.
    
    Formula: v = d / t
    
    Args:
        distance_m: Distance in meters
        time_s: Time in seconds
        
    Returns:
        Speed in meters per second (m/s)
        
    Raises:
        ValueError: If time is zero or negative
    """
    if time_s <= 0:
        raise ValueError("Time must be positive")
    return distance_m / time_s


def acceleration(v_final: float, v_initial: float, time_s: float) -> float:
    """Calculate acceleration from velocity change and time.
    
    Formula: a = (v_f - v_i) / t
    
    Args:
        v_final: Final velocity in m/s
        v_initial: Initial velocity in m/s
        time_s: Time interval in seconds
        
    Returns:
        Acceleration in meters per second squared (m/s²)
        
    Raises:
        ValueError: If time is zero or negative
    """
    if time_s <= 0:
        raise ValueError("Time must be positive")
    return (v_final - v_initial) / time_s


def density(mass_kg: float, volume_m3: float) -> float:
    """Calculate density from mass and volume.
    
    Formula: ρ = m / V
    
    Args:
        mass_kg: Mass in kilograms
        volume_m3: Volume in cubic meters
        
    Returns:
        Density in kilograms per cubic meter (kg/m³)
        
    Raises:
        ValueError: If volume is zero or negative
    """
    if volume_m3 <= 0:
        raise ValueError("Volume must be positive")
    return mass_kg / volume_m3


def momentum(mass_kg: float, velocity_m_s: float) -> float:
    """Calculate momentum from mass and velocity.
    
    Formula: p = m × v
    
    Args:
        mass_kg: Mass in kilograms
        velocity_m_s: Velocity in m/s
        
    Returns:
        Momentum in kilogram-meters per second (kg·m/s)
    """
    return mass_kg * velocity_m_s


def kinetic_energy(mass_kg: float, velocity_m_s: float) -> float:
    """Calculate kinetic energy from mass and velocity.
    
    Formula: KE = 0.5 × m × v²
    
    Args:
        mass_kg: Mass in kilograms
        velocity_m_s: Velocity in m/s
        
    Returns:
        Kinetic energy in Joules (J)
    """
    return 0.5 * mass_kg * velocity_m_s ** 2


def potential_energy(mass_kg: float, height_m: float, g: float = 9.81) -> float:
    """Calculate gravitational potential energy.
    
    Formula: PE = m × g × h
    
    Args:
        mass_kg: Mass in kilograms
        height_m: Height in meters
        g: Gravitational acceleration in m/s² (default: 9.81)
        
    Returns:
        Potential energy in Joules (J)
    """
    return mass_kg * g * height_m


def impulse(force_n: float, time_s: float) -> float:
    """Calculate impulse from force and time.
    
    Formula: J = F × Δt
    
    Args:
        force_n: Force in Newtons
        time_s: Time interval in seconds
        
    Returns:
        Impulse in Newton-seconds (N·s)
    """
    return force_n * time_s


def frequency(period_s: float) -> float:
    """Calculate frequency from period.
    
    Formula: f = 1 / T
    
    Args:
        period_s: Period in seconds
        
    Returns:
        Frequency in Hertz (Hz)
        
    Raises:
        ValueError: If period is zero or negative
    """
    if period_s <= 0:
        raise ValueError("Period must be positive")
    return 1 / period_s


def period(frequency_hz: float) -> float:
    """Calculate period from frequency.
    
    Formula: T = 1 / f
    
    Args:
        frequency_hz: Frequency in Hertz
        
    Returns:
        Period in seconds (s)
        
    Raises:
        ValueError: If frequency is zero or negative
    """
    if frequency_hz <= 0:
        raise ValueError("Frequency must be positive")
    return 1 / frequency_hz
