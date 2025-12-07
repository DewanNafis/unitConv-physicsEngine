"""Unit conversion helper for physics calculations.

This module provides a unified interface to parse user input with units
and convert to SI units (meters, kilograms, etc.) for physics calculations.
"""

from converters.basic import (
    m_to_cm, cm_to_m, inch_to_m, feet_to_m, yard_to_m, mile_to_km,
    kg_to_g, g_to_kg
)


class Distance:
    """Handle distance/length with automatic unit conversion."""
    
    UNITS = {
        'm': 1.0,
        'meter': 1.0,
        'meters': 1.0,
        'cm': 0.01,
        'centimeter': 0.01,
        'centimeters': 0.01,
        'inch': 0.0254,
        'inches': 0.0254,
        'in': 0.0254,
        'ft': 0.3048,
        'foot': 0.3048,
        'feet': 0.3048,
        'yard': 0.9144,
        'yards': 0.9144,
        'yd': 0.9144,
        'km': 1000.0,
        'kilometer': 1000.0,
        'kilometers': 1000.0,
        'mile': 1609.34,
        'miles': 1609.34,
        'mi': 1609.34,
    }
    
    @classmethod
    def to_meters(cls, value: float, unit: str) -> float:
        """Convert any length unit to meters.
        
        Args:
            value: Numeric value
            unit: Unit string (e.g., 'cm', 'inch', 'feet')
            
        Returns:
            Value in meters
            
        Raises:
            ValueError: If unit is not recognized
        """
        unit_lower = unit.lower().strip()
        if unit_lower not in cls.UNITS:
            raise ValueError(f"Unknown unit: {unit}. Supported: {', '.join(sorted(set(cls.UNITS.keys())))}")
        return value * cls.UNITS[unit_lower]
    
    @classmethod
    def parse(cls, input_str: str) -> float:
        """Parse a string like '5 cm' or '10 inches' and return meters.
        
        Args:
            input_str: String containing value and unit (e.g., "5 cm", "10 feet")
            
        Returns:
            Value in meters
            
        Example:
            >>> Distance.parse("5 cm")
            0.05
            >>> Distance.parse("10 feet")
            3.048
        """
        parts = input_str.strip().split()
        if len(parts) != 2:
            raise ValueError(f"Invalid format: '{input_str}'. Expected format: 'VALUE UNIT' (e.g., '5 cm')")
        
        try:
            value = float(parts[0])
        except ValueError:
            raise ValueError(f"Invalid number: '{parts[0]}'")
        
        unit = parts[1]
        return cls.to_meters(value, unit)


class Mass:
    """Handle mass with automatic unit conversion."""
    
    UNITS = {
        'kg': 1.0,
        'kilogram': 1.0,
        'kilograms': 1.0,
        'g': 0.001,
        'gram': 0.001,
        'grams': 0.001,
        'lb': 0.453592,
        'lbs': 0.453592,
        'pound': 0.453592,
        'pounds': 0.453592,
        'oz': 0.0283495,
        'ounce': 0.0283495,
        'ounces': 0.0283495,
    }
    
    @classmethod
    def to_kg(cls, value: float, unit: str) -> float:
        """Convert any mass unit to kilograms.
        
        Args:
            value: Numeric value
            unit: Unit string (e.g., 'g', 'lb', 'oz')
            
        Returns:
            Value in kilograms
            
        Raises:
            ValueError: If unit is not recognized
        """
        unit_lower = unit.lower().strip()
        if unit_lower not in cls.UNITS:
            raise ValueError(f"Unknown unit: {unit}. Supported: {', '.join(sorted(set(cls.UNITS.keys())))}")
        return value * cls.UNITS[unit_lower]
    
    @classmethod
    def parse(cls, input_str: str) -> float:
        """Parse a string like '5 kg' or '10 pounds' and return kilograms.
        
        Args:
            input_str: String containing value and unit
            
        Returns:
            Value in kilograms
        """
        parts = input_str.strip().split()
        if len(parts) != 2:
            raise ValueError(f"Invalid format: '{input_str}'. Expected format: 'VALUE UNIT' (e.g., '5 kg')")
        
        try:
            value = float(parts[0])
        except ValueError:
            raise ValueError(f"Invalid number: '{parts[0]}'")
        
        unit = parts[1]
        return cls.to_kg(value, unit)


class Velocity:
    """Handle velocity with automatic unit conversion."""
    
    UNITS = {
        'm/s': 1.0,
        'mps': 1.0,
        'km/h': 0.277778,
        'kmh': 0.277778,
        'kph': 0.277778,
        'mph': 0.44704,
        'ft/s': 0.3048,
        'fps': 0.3048,
    }
    
    @classmethod
    def to_mps(cls, value: float, unit: str) -> float:
        """Convert any velocity unit to meters per second.
        
        Args:
            value: Numeric value
            unit: Unit string (e.g., 'km/h', 'mph')
            
        Returns:
            Value in meters per second
        """
        unit_lower = unit.lower().strip()
        if unit_lower not in cls.UNITS:
            raise ValueError(f"Unknown unit: {unit}. Supported: {', '.join(sorted(set(cls.UNITS.keys())))}")
        return value * cls.UNITS[unit_lower]
    
    @classmethod
    def parse(cls, input_str: str) -> float:
        """Parse velocity string and return m/s."""
        parts = input_str.strip().split()
        if len(parts) != 2:
            raise ValueError(f"Invalid format: '{input_str}'. Expected format: 'VALUE UNIT' (e.g., '50 km/h')")
        
        try:
            value = float(parts[0])
        except ValueError:
            raise ValueError(f"Invalid number: '{parts[0]}'")
        
        unit = parts[1]
        return cls.to_mps(value, unit)


def parse_input(value_str: str, quantity_type: str = 'distance') -> float:
    """General parser for different physical quantities.
    
    Args:
        value_str: String with value and unit (e.g., "5 cm", "10 kg")
        quantity_type: Type of quantity ('distance', 'mass', 'velocity')
        
    Returns:
        Value in SI units (meters, kilograms, m/s)
        
    Example:
        >>> parse_input("5 cm", "distance")
        0.05
        >>> parse_input("10 lb", "mass")
        4.53592
    """
    parsers = {
        'distance': Distance,
        'length': Distance,
        'mass': Mass,
        'velocity': Velocity,
        'speed': Velocity,
    }
    
    if quantity_type not in parsers:
        raise ValueError(f"Unknown quantity type: {quantity_type}")
    
    return parsers[quantity_type].parse(value_str)
