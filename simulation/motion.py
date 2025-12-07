"""Motion simulation functions."""

import math

# Acceleration due to gravity (m/s²)
GRAVITY = 9.81


def falling_body(time_s: float) -> float:
    """Calculate distance fallen by a body under gravity.
    
    Formula: d = 0.5 * g * t²
    
    Args:
        time_s: Time in seconds
        
    Returns:
        Distance fallen in meters
        
    Raises:
        ValueError: If time is negative
    """
    if time_s < 0:
        raise ValueError("Time cannot be negative")
    return 0.5 * GRAVITY * time_s ** 2


def projectile_range(u: float, angle_deg: float) -> float:
    """Calculate the range of a projectile.
    
    Formula: R = (u² * sin(2θ)) / g
    
    Args:
        u: Initial velocity in m/s
        angle_deg: Launch angle in degrees
        
    Returns:
        Horizontal range in meters
        
    Raises:
        ValueError: If initial velocity is negative
    """
    if u < 0:
        raise ValueError("Initial velocity cannot be negative")
    
    # Convert angle to radians
    angle_rad = math.radians(angle_deg)
    
    # Calculate range
    return (u ** 2 * math.sin(2 * angle_rad)) / GRAVITY
