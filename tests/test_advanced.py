"""Unit tests for advanced physics calculations."""

import pytest
from physics.advanced import (
    force, work, power, pressure,
    torque, angular_velocity, centripetal_force,
    gravitational_force, elastic_potential_energy,
    efficiency, electric_power
)


class TestForce:
    """Test force calculation function."""
    
    def test_force_basic(self):
        """Test basic force calculation."""
        assert force(10, 5) == 50
        assert force(2, 10) == 20
    
    def test_force_zero_mass(self):
        """Test force with zero mass."""
        assert force(0, 10) == 0
    
    def test_force_zero_acceleration(self):
        """Test force with zero acceleration."""
        assert force(10, 0) == 0
    
    def test_force_decimal(self):
        """Test force with decimal values."""
        assert force(5.5, 2.0) == pytest.approx(11.0)
    
    def test_force_negative_acceleration(self):
        """Test force with negative acceleration (deceleration)."""
        assert force(10, -5) == -50


class TestWork:
    """Test work calculation function."""
    
    def test_work_basic(self):
        """Test basic work calculation."""
        assert work(50, 10) == 500
        assert work(100, 5) == 500
    
    def test_work_zero_force(self):
        """Test work with zero force."""
        assert work(0, 10) == 0
    
    def test_work_zero_distance(self):
        """Test work with zero distance."""
        assert work(50, 0) == 0
    
    def test_work_decimal(self):
        """Test work with decimal values."""
        assert work(25.5, 2.0) == pytest.approx(51.0)
    
    def test_work_negative_force(self):
        """Test work with negative force."""
        assert work(-50, 10) == -500


class TestPower:
    """Test power calculation function."""
    
    def test_power_basic(self):
        """Test basic power calculation."""
        assert power(500, 10) == 50
        assert power(1000, 20) == 50
    
    def test_power_zero_work(self):
        """Test power with zero work."""
        assert power(0, 10) == 0
    
    def test_power_decimal(self):
        """Test power with decimal values."""
        assert power(100.5, 2.0) == pytest.approx(50.25)
    
    def test_power_zero_time_raises(self):
        """Test that zero time raises ValueError."""
        with pytest.raises(ValueError, match="Time must be positive"):
            power(500, 0)
    
    def test_power_negative_time_raises(self):
        """Test that negative time raises ValueError."""
        with pytest.raises(ValueError, match="Time must be positive"):
            power(500, -10)


class TestPressure:
    """Test pressure calculation function."""
    
    def test_pressure_basic(self):
        """Test basic pressure calculation."""
        assert pressure(1000, 2) == 500
        assert pressure(500, 5) == 100
    
    def test_pressure_zero_force(self):
        """Test pressure with zero force."""
        assert pressure(0, 10) == 0
    
    def test_pressure_decimal(self):
        """Test pressure with decimal values."""
        assert pressure(150.5, 2.0) == pytest.approx(75.25)
    
    def test_pressure_zero_area_raises(self):
        """Test that zero area raises ValueError."""
        with pytest.raises(ValueError, match="Area must be positive"):
            pressure(1000, 0)
    
    def test_pressure_negative_area_raises(self):
        """Test that negative area raises ValueError."""
        with pytest.raises(ValueError, match="Area must be positive"):
            pressure(1000, -5)


class TestAdvancedPhysicsIntegration:
    """Integration tests combining multiple advanced physics functions."""
    
    def test_complete_work_power_scenario(self):
        """Test a complete scenario from force to power."""
        # Apply 50N force over 10m
        w = work(50, 10)
        assert w == 500  # 500 J
        
        # Work done in 10 seconds
        p = power(w, 10)
        assert p == 50  # 50 W
    
    def test_force_work_chain(self):
        """Test chaining force and work calculations."""
        # Object with 10kg mass accelerating at 5 m/s²
        f = force(10, 5)
        assert f == 50  # 50 N
        
        # Force applied over 20m
        w = work(f, 20)
        assert w == 1000  # 1000 J
    
    def test_pressure_from_force(self):
        """Test calculating pressure from force scenario."""
        # Object with 50kg mass under gravity (assuming ~10 m/s²)
        f = force(50, 10)
        assert f == 500  # 500 N
        
        # Pressure on 2 m² area
        p = pressure(f, 2)
        assert p == 250  # 250 Pa
    
    def test_realistic_lifting_scenario(self):
        """Test a realistic lifting scenario."""
        # Lift a 20kg object (force against gravity ~196 N assuming g≈9.8)
        # Using simplified g=10 for easier calculation
        f = force(20, 10)
        assert f == 200  # 200 N
        
        # Lift it 3 meters
        w = work(f, 3)
        assert w == 600  # 600 J
        
        # Takes 5 seconds
        p = power(w, 5)
        assert p == 120  # 120 W


class TestTorque:
    """Test torque calculation function."""
    
    def test_torque_basic(self):
        """Test basic torque calculation."""
        assert torque(50, 2) == 100
        assert torque(100, 0.5) == 50
    
    def test_torque_zero_force(self):
        """Test torque with zero force."""
        assert torque(0, 5) == 0
    
    def test_torque_zero_radius(self):
        """Test torque with zero radius."""
        assert torque(50, 0) == 0
    
    def test_torque_decimal(self):
        """Test torque with decimal values."""
        assert torque(25.5, 2.0) == pytest.approx(51.0)


class TestAngularVelocity:
    """Test angular velocity calculation function."""
    
    def test_angular_velocity_basic(self):
        """Test basic angular velocity calculation."""
        import math
        # One full rotation (2π rad) in 1 second
        assert angular_velocity(2 * math.pi, 1) == pytest.approx(2 * math.pi)
    
    def test_angular_velocity_decimal(self):
        """Test angular velocity with decimal values."""
        assert angular_velocity(10.5, 2.0) == pytest.approx(5.25)
    
    def test_angular_velocity_zero_time_raises(self):
        """Test that zero time raises ValueError."""
        with pytest.raises(ValueError, match="Time must be positive"):
            angular_velocity(10, 0)
    
    def test_angular_velocity_negative_time_raises(self):
        """Test that negative time raises ValueError."""
        with pytest.raises(ValueError, match="Time must be positive"):
            angular_velocity(10, -5)


class TestCentripetalForce:
    """Test centripetal force calculation function."""
    
    def test_centripetal_force_basic(self):
        """Test basic centripetal force calculation."""
        # F = (10 * 5²) / 2 = 250 / 2 = 125 N
        assert centripetal_force(10, 5, 2) == 125
    
    def test_centripetal_force_decimal(self):
        """Test centripetal force with decimal values."""
        # F = (5 * 4²) / 2 = 80 / 2 = 40 N
        assert centripetal_force(5, 4, 2) == pytest.approx(40.0)
    
    def test_centripetal_force_doubles_with_mass(self):
        """Test that centripetal force doubles when mass doubles."""
        f1 = centripetal_force(5, 10, 5)
        f2 = centripetal_force(10, 10, 5)
        assert f2 == pytest.approx(2 * f1)
    
    def test_centripetal_force_zero_radius_raises(self):
        """Test that zero radius raises ValueError."""
        with pytest.raises(ValueError, match="Radius must be positive"):
            centripetal_force(10, 5, 0)
    
    def test_centripetal_force_negative_radius_raises(self):
        """Test that negative radius raises ValueError."""
        with pytest.raises(ValueError, match="Radius must be positive"):
            centripetal_force(10, 5, -2)


class TestGravitationalForce:
    """Test gravitational force calculation function."""
    
    def test_gravitational_force_basic(self):
        """Test basic gravitational force calculation."""
        # F = 6.674e-11 * (1000 * 1000) / 1² = 6.674e-5 N
        result = gravitational_force(1000, 1000, 1)
        assert result == pytest.approx(6.674e-5)
    
    def test_gravitational_force_earth_moon_order(self):
        """Test gravitational force has correct order of magnitude."""
        # Simplified calculation (not actual values)
        m_earth = 5.972e24  # kg
        m_moon = 7.342e22   # kg
        distance = 3.844e8  # m
        
        result = gravitational_force(m_earth, m_moon, distance)
        # Force should be around 10^20 N
        assert 1e19 < result < 1e21
    
    def test_gravitational_force_zero_distance_raises(self):
        """Test that zero distance raises ValueError."""
        with pytest.raises(ValueError, match="Distance must be positive"):
            gravitational_force(1000, 1000, 0)
    
    def test_gravitational_force_negative_distance_raises(self):
        """Test that negative distance raises ValueError."""
        with pytest.raises(ValueError, match="Distance must be positive"):
            gravitational_force(1000, 1000, -5)
    
    def test_gravitational_force_inverse_square(self):
        """Test that force follows inverse square law."""
        f1 = gravitational_force(1000, 1000, 1)
        f2 = gravitational_force(1000, 1000, 2)
        # Force at 2x distance should be 1/4 of original
        assert f2 == pytest.approx(f1 / 4)


class TestElasticPotentialEnergy:
    """Test elastic potential energy calculation function."""
    
    def test_elastic_potential_energy_basic(self):
        """Test basic elastic potential energy calculation."""
        # PE = 0.5 * 100 * 2² = 200 J
        assert elastic_potential_energy(100, 2) == 200
    
    def test_elastic_potential_energy_zero_displacement(self):
        """Test elastic PE with zero displacement."""
        assert elastic_potential_energy(100, 0) == 0
    
    def test_elastic_potential_energy_decimal(self):
        """Test elastic PE with decimal values."""
        # PE = 0.5 * 50 * 0.5² = 6.25 J
        assert elastic_potential_energy(50, 0.5) == pytest.approx(6.25)
    
    def test_elastic_potential_energy_quadruples_with_double_displacement(self):
        """Test that PE quadruples when displacement doubles."""
        pe1 = elastic_potential_energy(100, 1)
        pe2 = elastic_potential_energy(100, 2)
        assert pe2 == pytest.approx(4 * pe1)


class TestEfficiency:
    """Test efficiency calculation function."""
    
    def test_efficiency_perfect(self):
        """Test 100% efficiency."""
        assert efficiency(100, 100) == 100
    
    def test_efficiency_fifty_percent(self):
        """Test 50% efficiency."""
        assert efficiency(50, 100) == 50
    
    def test_efficiency_decimal(self):
        """Test efficiency with decimal values."""
        assert efficiency(75.5, 100) == pytest.approx(75.5)
    
    def test_efficiency_greater_than_100(self):
        """Test that efficiency can be > 100 (for theoretical scenarios)."""
        # In practice impossible, but mathematically valid
        assert efficiency(150, 100) == 150
    
    def test_efficiency_zero_input_raises(self):
        """Test that zero input energy raises ValueError."""
        with pytest.raises(ValueError, match="Input energy must be positive"):
            efficiency(50, 0)
    
    def test_efficiency_negative_input_raises(self):
        """Test that negative input energy raises ValueError."""
        with pytest.raises(ValueError, match="Input energy must be positive"):
            efficiency(50, -100)


class TestElectricPower:
    """Test electric power calculation function."""
    
    def test_electric_power_basic(self):
        """Test basic electric power calculation."""
        assert electric_power(12, 2) == 24
        assert electric_power(120, 0.5) == 60
    
    def test_electric_power_zero_voltage(self):
        """Test electric power with zero voltage."""
        assert electric_power(0, 10) == 0
    
    def test_electric_power_zero_current(self):
        """Test electric power with zero current."""
        assert electric_power(120, 0) == 0
    
    def test_electric_power_decimal(self):
        """Test electric power with decimal values."""
        assert electric_power(9.5, 2.0) == pytest.approx(19.0)
    
    def test_electric_power_household(self):
        """Test electric power for household appliance."""
        # 120V at 10A = 1200W
        assert electric_power(120, 10) == 1200


class TestAdvancedPhysicsExtendedIntegration:
    """Extended integration tests for new advanced physics functions."""
    
    def test_rotational_motion_scenario(self):
        """Test a rotational motion scenario."""
        # Apply 50N force at 2m radius
        tau = torque(50, 2)
        assert tau == 100  # 100 N·m
        
        # Angular displacement of π radians in 2 seconds
        import math
        omega = angular_velocity(math.pi, 2)
        assert omega == pytest.approx(math.pi / 2)
    
    def test_circular_motion_scenario(self):
        """Test circular motion with centripetal force."""
        # 5kg object moving at 10 m/s in 2m radius circle
        fc = centripetal_force(5, 10, 2)
        assert fc == 250  # 250 N
    
    def test_spring_compression_scenario(self):
        """Test spring compression energy."""
        # Spring with k=200 N/m compressed 0.5m
        pe = elastic_potential_energy(200, 0.5)
        assert pe == 25  # 25 J
    
    def test_electrical_system_scenario(self):
        """Test electrical power in a system."""
        # 240V circuit with 5A current
        p_elec = electric_power(240, 5)
        assert p_elec == 1200  # 1200 W
        
        # If mechanical output is 1000W, efficiency is
        eff = efficiency(1000, p_elec)
        assert eff == pytest.approx(83.333, rel=0.001)
