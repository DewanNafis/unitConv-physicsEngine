"""Unit tests for basic unit conversions."""

import pytest
from converters.basic import (
    m_to_cm, cm_to_m,
    kg_to_g, g_to_kg,
    c_to_f, f_to_c,
    s_to_min, min_to_s
)


class TestLengthConversions:
    """Test length conversion functions."""
    
    def test_m_to_cm_positive(self):
        """Test meters to centimeters conversion with positive values."""
        assert m_to_cm(1) == 100
        assert m_to_cm(5) == 500
        assert m_to_cm(0.5) == 50
    
    def test_m_to_cm_zero(self):
        """Test meters to centimeters conversion with zero."""
        assert m_to_cm(0) == 0
    
    def test_cm_to_m_positive(self):
        """Test centimeters to meters conversion with positive values."""
        assert cm_to_m(100) == 1
        assert cm_to_m(250) == 2.5
        assert cm_to_m(50) == 0.5
    
    def test_cm_to_m_zero(self):
        """Test centimeters to meters conversion with zero."""
        assert cm_to_m(0) == 0


class TestMassConversions:
    """Test mass conversion functions."""
    
    def test_kg_to_g_positive(self):
        """Test kilograms to grams conversion with positive values."""
        assert kg_to_g(1) == 1000
        assert kg_to_g(2.5) == 2500
        assert kg_to_g(0.001) == 1
    
    def test_kg_to_g_zero(self):
        """Test kilograms to grams conversion with zero."""
        assert kg_to_g(0) == 0
    
    def test_g_to_kg_positive(self):
        """Test grams to kilograms conversion with positive values."""
        assert g_to_kg(1000) == 1
        assert g_to_kg(1500) == 1.5
        assert g_to_kg(1) == 0.001
    
    def test_g_to_kg_zero(self):
        """Test grams to kilograms conversion with zero."""
        assert g_to_kg(0) == 0


class TestTemperatureConversions:
    """Test temperature conversion functions."""
    
    def test_c_to_f_freezing(self):
        """Test Celsius to Fahrenheit at freezing point."""
        assert c_to_f(0) == 32
    
    def test_c_to_f_boiling(self):
        """Test Celsius to Fahrenheit at boiling point."""
        assert c_to_f(100) == 212
    
    def test_c_to_f_negative(self):
        """Test Celsius to Fahrenheit with negative temperature."""
        assert c_to_f(-40) == -40
    
    def test_c_to_f_room_temp(self):
        """Test Celsius to Fahrenheit at room temperature."""
        assert abs(c_to_f(20) - 68) < 0.01
    
    def test_f_to_c_freezing(self):
        """Test Fahrenheit to Celsius at freezing point."""
        assert f_to_c(32) == 0
    
    def test_f_to_c_boiling(self):
        """Test Fahrenheit to Celsius at boiling point."""
        assert f_to_c(212) == 100
    
    def test_f_to_c_negative(self):
        """Test Fahrenheit to Celsius with negative temperature."""
        assert f_to_c(-40) == -40
    
    def test_f_to_c_room_temp(self):
        """Test Fahrenheit to Celsius at room temperature."""
        assert abs(f_to_c(68) - 20) < 0.01


class TestTimeConversions:
    """Test time conversion functions."""
    
    def test_s_to_min_positive(self):
        """Test seconds to minutes conversion with positive values."""
        assert s_to_min(60) == 1
        assert s_to_min(120) == 2
        assert s_to_min(90) == 1.5
    
    def test_s_to_min_zero(self):
        """Test seconds to minutes conversion with zero."""
        assert s_to_min(0) == 0
    
    def test_min_to_s_positive(self):
        """Test minutes to seconds conversion with positive values."""
        assert min_to_s(1) == 60
        assert min_to_s(2) == 120
        assert min_to_s(0.5) == 30
    
    def test_min_to_s_zero(self):
        """Test minutes to seconds conversion with zero."""
        assert min_to_s(0) == 0


class TestConversionRoundTrips:
    """Test that conversions are reversible."""
    
    def test_length_round_trip(self):
        """Test that length conversions are reversible."""
        value = 5.5
        assert cm_to_m(m_to_cm(value)) == pytest.approx(value)
    
    def test_mass_round_trip(self):
        """Test that mass conversions are reversible."""
        value = 3.7
        assert g_to_kg(kg_to_g(value)) == pytest.approx(value)
    
    def test_temperature_round_trip(self):
        """Test that temperature conversions are reversible."""
        value = 25.5
        assert f_to_c(c_to_f(value)) == pytest.approx(value)
    
    def test_time_round_trip(self):
        """Test that time conversions are reversible."""
        value = 2.5
        assert s_to_min(min_to_s(value)) == pytest.approx(value)
