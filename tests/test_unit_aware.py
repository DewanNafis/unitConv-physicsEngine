"""Unit tests for unit-aware physics calculations."""

import pytest
from converters.units import Distance, Mass, Velocity, parse_input
from physics import unit_aware


class TestDistanceConversion:
    """Test distance/length conversions."""
    
    def test_meters_to_meters(self):
        assert Distance.to_meters(5, 'm') == 5.0
        assert Distance.to_meters(5, 'meter') == 5.0
        assert Distance.to_meters(5, 'meters') == 5.0
    
    def test_cm_to_meters(self):
        assert Distance.to_meters(100, 'cm') == 1.0
        assert Distance.to_meters(50, 'centimeters') == 0.5
    
    def test_inches_to_meters(self):
        result = Distance.to_meters(1, 'inch')
        assert abs(result - 0.0254) < 0.0001
        
        result = Distance.to_meters(12, 'inches')
        assert abs(result - 0.3048) < 0.0001
    
    def test_feet_to_meters(self):
        result = Distance.to_meters(1, 'feet')
        assert abs(result - 0.3048) < 0.0001
        
        result = Distance.to_meters(10, 'ft')
        assert abs(result - 3.048) < 0.001
    
    def test_yards_to_meters(self):
        result = Distance.to_meters(1, 'yard')
        assert abs(result - 0.9144) < 0.0001
    
    def test_miles_to_meters(self):
        result = Distance.to_meters(1, 'mile')
        assert abs(result - 1609.34) < 0.01
    
    def test_km_to_meters(self):
        assert Distance.to_meters(1, 'km') == 1000.0
        assert Distance.to_meters(2.5, 'kilometers') == 2500.0
    
    def test_parse_distance(self):
        assert Distance.parse("5 m") == 5.0
        assert Distance.parse("100 cm") == 1.0
        
        result = Distance.parse("10 feet")
        assert abs(result - 3.048) < 0.001
    
    def test_invalid_unit(self):
        with pytest.raises(ValueError, match="Unknown unit"):
            Distance.to_meters(5, 'invalid')
    
    def test_invalid_parse_format(self):
        with pytest.raises(ValueError, match="Invalid format"):
            Distance.parse("5")
        
        with pytest.raises(ValueError, match="Invalid format"):
            Distance.parse("5 m 10")
    
    def test_invalid_number(self):
        with pytest.raises(ValueError, match="Invalid number"):
            Distance.parse("abc m")


class TestMassConversion:
    """Test mass conversions."""
    
    def test_kg_to_kg(self):
        assert Mass.to_kg(5, 'kg') == 5.0
        assert Mass.to_kg(5, 'kilogram') == 5.0
    
    def test_grams_to_kg(self):
        assert Mass.to_kg(1000, 'g') == 1.0
        assert Mass.to_kg(500, 'grams') == 0.5
    
    def test_pounds_to_kg(self):
        result = Mass.to_kg(1, 'lb')
        assert abs(result - 0.453592) < 0.00001
        
        result = Mass.to_kg(10, 'pounds')
        assert abs(result - 4.53592) < 0.0001
    
    def test_ounces_to_kg(self):
        result = Mass.to_kg(1, 'oz')
        assert abs(result - 0.0283495) < 0.000001
    
    def test_parse_mass(self):
        assert Mass.parse("5 kg") == 5.0
        assert Mass.parse("1000 g") == 1.0
        
        result = Mass.parse("10 lb")
        assert abs(result - 4.53592) < 0.0001
    
    def test_invalid_mass_unit(self):
        with pytest.raises(ValueError, match="Unknown unit"):
            Mass.to_kg(5, 'invalid')


class TestVelocityConversion:
    """Test velocity conversions."""
    
    def test_mps_to_mps(self):
        assert Velocity.to_mps(10, 'm/s') == 10.0
        assert Velocity.to_mps(10, 'mps') == 10.0
    
    def test_kmh_to_mps(self):
        result = Velocity.to_mps(36, 'km/h')
        assert abs(result - 10.0) < 0.01
        
        result = Velocity.to_mps(100, 'kph')
        assert abs(result - 27.7778) < 0.001
    
    def test_mph_to_mps(self):
        result = Velocity.to_mps(10, 'mph')
        assert abs(result - 4.4704) < 0.001
    
    def test_fps_to_mps(self):
        result = Velocity.to_mps(10, 'ft/s')
        assert abs(result - 3.048) < 0.001
    
    def test_parse_velocity(self):
        assert Velocity.parse("10 m/s") == 10.0
        
        result = Velocity.parse("50 km/h")
        assert abs(result - 13.8889) < 0.001


class TestParseInput:
    """Test general parse_input function."""
    
    def test_parse_distance(self):
        assert parse_input("5 m", "distance") == 5.0
        assert parse_input("100 cm", "length") == 1.0
    
    def test_parse_mass(self):
        assert parse_input("5 kg", "mass") == 5.0
    
    def test_parse_velocity(self):
        assert parse_input("10 m/s", "velocity") == 10.0
        assert parse_input("10 m/s", "speed") == 10.0
    
    def test_invalid_quantity_type(self):
        with pytest.raises(ValueError, match="Unknown quantity type"):
            parse_input("5 m", "invalid")


class TestUnitAwarePhysics:
    """Test unit-aware physics calculations."""
    
    def test_calculate_speed_meters(self):
        result = unit_aware.calculate_speed("100 m", 10)
        assert result == 10.0
    
    def test_calculate_speed_cm(self):
        result = unit_aware.calculate_speed("100 cm", 2)
        assert result == 0.5
    
    def test_calculate_speed_feet(self):
        result = unit_aware.calculate_speed("10 feet", 1)
        assert abs(result - 3.048) < 0.001
    
    def test_calculate_momentum(self):
        result = unit_aware.calculate_momentum("5 kg", "10 m/s")
        assert result == 50.0
        
        result = unit_aware.calculate_momentum("1000 g", "10 m/s")
        assert result == 10.0
    
    def test_calculate_kinetic_energy(self):
        result = unit_aware.calculate_kinetic_energy("2 kg", "10 m/s")
        assert result == 100.0
    
    def test_calculate_potential_energy(self):
        result = unit_aware.calculate_potential_energy("10 kg", "5 m")
        assert abs(result - 490.5) < 0.1
        
        result = unit_aware.calculate_potential_energy("10 kg", "500 cm")
        assert abs(result - 490.5) < 0.1
    
    def test_calculate_force(self):
        result = unit_aware.calculate_force("10 kg", 5)
        assert result == 50.0
        
        result = unit_aware.calculate_force("1000 g", 5)
        assert result == 5.0
    
    def test_calculate_work(self):
        result = unit_aware.calculate_work(50, "10 m")
        assert result == 500.0
        
        result = unit_aware.calculate_work(50, "1000 cm")
        assert result == 500.0
    
    def test_calculate_centripetal_force(self):
        result = unit_aware.calculate_centripetal_force("2 kg", "10 m/s", "5 m")
        assert result == 40.0
    
    def test_calculate_gravitational_force(self):
        result = unit_aware.calculate_gravitational_force("1000 kg", "2000 kg", "10 m")
        assert result > 0
        assert result < 0.001  # Very small force
    
    def test_simulate_falling_body(self):
        result = unit_aware.simulate_falling_body(1)
        assert result > 0
        assert abs(result - 4.905) < 0.01  # 0.5 * 9.81 * 1^2
        
        result = unit_aware.simulate_falling_body(2)
        assert abs(result - 19.62) < 0.01  # 0.5 * 9.81 * 2^2
    
    def test_simulate_projectile_range(self):
        result = unit_aware.simulate_projectile_range("20 m/s", 45)
        assert result > 0
        
        result = unit_aware.simulate_projectile_range("70 km/h", 45)
        assert result > 0


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def test_empty_string(self):
        with pytest.raises(ValueError):
            Distance.parse("")
    
    def test_whitespace_handling(self):
        assert Distance.parse("  5   m  ") == 5.0
        assert Mass.parse("  10  kg  ") == 10.0
    
    def test_case_insensitive_units(self):
        assert Distance.to_meters(5, 'M') == 5.0
        assert Distance.to_meters(5, 'CM') == 0.05
        assert Mass.to_kg(5, 'KG') == 5.0
        assert Mass.to_kg(5, 'G') == 0.005
    
    def test_zero_values(self):
        assert unit_aware.calculate_speed("0 m", 1) == 0.0
        assert unit_aware.calculate_force("0 kg", 10) == 0.0
    
    def test_negative_values(self):
        # Distance parsing should accept negative values (e.g., displacement)
        assert Distance.parse("-5 m") == -5.0
