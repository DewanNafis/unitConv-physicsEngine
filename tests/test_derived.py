"""Unit tests for derived physics formulas."""

import pytest
from physics.derived import (
    speed, acceleration, density,
    momentum, kinetic_energy, potential_energy,
    impulse, frequency, period
)


class TestSpeed:
    """Test speed calculation function."""
    
    def test_speed_basic(self):
        """Test basic speed calculation."""
        assert speed(100, 10) == 10
        assert speed(50, 5) == 10
    
    def test_speed_decimal(self):
        """Test speed calculation with decimal values."""
        assert speed(100, 9.5) == pytest.approx(10.526, rel=0.001)
    
    def test_speed_zero_distance(self):
        """Test speed with zero distance."""
        assert speed(0, 10) == 0
    
    def test_speed_zero_time_raises(self):
        """Test that zero time raises ValueError."""
        with pytest.raises(ValueError, match="Time must be positive"):
            speed(100, 0)
    
    def test_speed_negative_time_raises(self):
        """Test that negative time raises ValueError."""
        with pytest.raises(ValueError, match="Time must be positive"):
            speed(100, -5)


class TestAcceleration:
    """Test acceleration calculation function."""
    
    def test_acceleration_positive(self):
        """Test acceleration with increasing velocity."""
        assert acceleration(30, 0, 5) == 6
        assert acceleration(20, 10, 2) == 5
    
    def test_acceleration_negative(self):
        """Test deceleration (negative acceleration)."""
        assert acceleration(0, 30, 5) == -6
        assert acceleration(10, 20, 2) == -5
    
    def test_acceleration_no_change(self):
        """Test acceleration with constant velocity."""
        assert acceleration(10, 10, 5) == 0
    
    def test_acceleration_decimal(self):
        """Test acceleration with decimal values."""
        assert acceleration(15.5, 5.5, 2.0) == pytest.approx(5.0)
    
    def test_acceleration_zero_time_raises(self):
        """Test that zero time raises ValueError."""
        with pytest.raises(ValueError, match="Time must be positive"):
            acceleration(30, 0, 0)
    
    def test_acceleration_negative_time_raises(self):
        """Test that negative time raises ValueError."""
        with pytest.raises(ValueError, match="Time must be positive"):
            acceleration(30, 0, -5)


class TestDensity:
    """Test density calculation function."""
    
    def test_density_water(self):
        """Test density calculation approximating water."""
        assert density(1000, 1) == 1000
    
    def test_density_steel(self):
        """Test density calculation approximating steel."""
        # Steel: ~7800 kg/m³
        assert density(7.8, 0.001) == 7800
    
    def test_density_air(self):
        """Test density calculation approximating air."""
        # Air: ~1.2 kg/m³
        assert density(1.2, 1) == pytest.approx(1.2)
    
    def test_density_decimal(self):
        """Test density with decimal values."""
        assert density(5.5, 2.2) == pytest.approx(2.5)
    
    def test_density_zero_volume_raises(self):
        """Test that zero volume raises ValueError."""
        with pytest.raises(ValueError, match="Volume must be positive"):
            density(100, 0)
    
    def test_density_negative_volume_raises(self):
        """Test that negative volume raises ValueError."""
        with pytest.raises(ValueError, match="Volume must be positive"):
            density(100, -5)


class TestMomentum:
    """Test momentum calculation function."""
    
    def test_momentum_basic(self):
        """Test basic momentum calculation."""
        assert momentum(10, 5) == 50
        assert momentum(2, 20) == 40
    
    def test_momentum_zero_velocity(self):
        """Test momentum with zero velocity."""
        assert momentum(10, 0) == 0
    
    def test_momentum_zero_mass(self):
        """Test momentum with zero mass."""
        assert momentum(0, 10) == 0
    
    def test_momentum_decimal(self):
        """Test momentum with decimal values."""
        assert momentum(5.5, 2.0) == pytest.approx(11.0)


class TestKineticEnergy:
    """Test kinetic energy calculation function."""
    
    def test_kinetic_energy_basic(self):
        """Test basic kinetic energy calculation."""
        # KE = 0.5 * 10 * 5² = 125 J
        assert kinetic_energy(10, 5) == 125
    
    def test_kinetic_energy_zero_velocity(self):
        """Test kinetic energy with zero velocity."""
        assert kinetic_energy(10, 0) == 0
    
    def test_kinetic_energy_decimal(self):
        """Test kinetic energy with decimal values."""
        # KE = 0.5 * 2 * 3² = 9 J
        assert kinetic_energy(2, 3) == pytest.approx(9.0)
    
    def test_kinetic_energy_doubles_with_mass(self):
        """Test that KE doubles when mass doubles."""
        ke1 = kinetic_energy(5, 10)
        ke2 = kinetic_energy(10, 10)
        assert ke2 == pytest.approx(2 * ke1)
    
    def test_kinetic_energy_quadruples_with_double_velocity(self):
        """Test that KE quadruples when velocity doubles."""
        ke1 = kinetic_energy(10, 5)
        ke2 = kinetic_energy(10, 10)
        assert ke2 == pytest.approx(4 * ke1)


class TestPotentialEnergy:
    """Test potential energy calculation function."""
    
    def test_potential_energy_basic(self):
        """Test basic potential energy calculation."""
        # PE = 10 * 9.81 * 5 = 490.5 J
        assert potential_energy(10, 5) == pytest.approx(490.5)
    
    def test_potential_energy_custom_gravity(self):
        """Test potential energy with custom gravity."""
        # PE = 10 * 10 * 5 = 500 J
        assert potential_energy(10, 5, g=10) == 500
    
    def test_potential_energy_zero_height(self):
        """Test potential energy at ground level."""
        assert potential_energy(10, 0) == 0
    
    def test_potential_energy_decimal(self):
        """Test potential energy with decimal values."""
        assert potential_energy(5.5, 2.0, g=10) == pytest.approx(110.0)


class TestImpulse:
    """Test impulse calculation function."""
    
    def test_impulse_basic(self):
        """Test basic impulse calculation."""
        assert impulse(50, 2) == 100
        assert impulse(100, 0.5) == 50
    
    def test_impulse_zero_force(self):
        """Test impulse with zero force."""
        assert impulse(0, 10) == 0
    
    def test_impulse_zero_time(self):
        """Test impulse with zero time."""
        assert impulse(50, 0) == 0
    
    def test_impulse_decimal(self):
        """Test impulse with decimal values."""
        assert impulse(25.5, 2.0) == pytest.approx(51.0)


class TestFrequency:
    """Test frequency calculation function."""
    
    def test_frequency_basic(self):
        """Test basic frequency calculation."""
        assert frequency(1) == 1
        assert frequency(0.5) == 2
        assert frequency(2) == 0.5
    
    def test_frequency_decimal(self):
        """Test frequency with decimal period."""
        assert frequency(0.25) == pytest.approx(4.0)
    
    def test_frequency_zero_period_raises(self):
        """Test that zero period raises ValueError."""
        with pytest.raises(ValueError, match="Period must be positive"):
            frequency(0)
    
    def test_frequency_negative_period_raises(self):
        """Test that negative period raises ValueError."""
        with pytest.raises(ValueError, match="Period must be positive"):
            frequency(-1)


class TestPeriod:
    """Test period calculation function."""
    
    def test_period_basic(self):
        """Test basic period calculation."""
        assert period(1) == 1
        assert period(2) == 0.5
        assert period(0.5) == 2
    
    def test_period_decimal(self):
        """Test period with decimal frequency."""
        assert period(4.0) == pytest.approx(0.25)
    
    def test_period_zero_frequency_raises(self):
        """Test that zero frequency raises ValueError."""
        with pytest.raises(ValueError, match="Frequency must be positive"):
            period(0)
    
    def test_period_negative_frequency_raises(self):
        """Test that negative frequency raises ValueError."""
        with pytest.raises(ValueError, match="Frequency must be positive"):
            period(-1)


class TestFrequencyPeriodRelationship:
    """Test the inverse relationship between frequency and period."""
    
    def test_frequency_period_inverse(self):
        """Test that frequency and period are inverses."""
        f = 5.0
        assert period(frequency(period(f))) == pytest.approx(period(f))
    
    def test_period_frequency_inverse(self):
        """Test that period and frequency are inverses."""
        t = 0.2
        assert frequency(period(frequency(t))) == pytest.approx(frequency(t))


class TestDerivedPhysicsIntegration:
    """Integration tests combining multiple derived physics functions."""
    
    def test_moving_object_scenario(self):
        """Test a complete scenario of a moving object."""
        # Object travels 100m in 10s
        v = speed(100, 10)
        assert v == 10  # 10 m/s
        
        # Object accelerates from 0 to 10 m/s in 5s
        a = acceleration(v, 0, 5)
        assert a == 2  # 2 m/s²
    
    def test_material_properties(self):
        """Test calculating material properties."""
        # A 10kg object with 5m³ volume
        rho = density(10, 5)
        assert rho == 2  # 2 kg/m³
    
    def test_energy_conservation_scenario(self):
        """Test energy conservation in a falling object."""
        mass = 5.0  # kg
        height = 10.0  # m
        
        # Initial potential energy
        pe_initial = potential_energy(mass, height, g=10)
        assert pe_initial == 500  # 500 J
        
        # When it hits ground, all PE converts to KE
        # v² = 2gh, so v = sqrt(2*10*10) = 14.14 m/s
        # For simplicity, using v = 14.14
        velocity = 14.14
        ke_final = kinetic_energy(mass, velocity)
        assert ke_final == pytest.approx(pe_initial, rel=0.01)
    
    def test_momentum_impulse_relationship(self):
        """Test relationship between momentum change and impulse."""
        # Object with 10kg mass moving at 5 m/s
        p_initial = momentum(10, 5)
        assert p_initial == 50  # kg·m/s
        
        # Apply 20N force for 2.5s
        j = impulse(20, 2.5)
        assert j == 50  # N·s
        
        # Final momentum should be initial + impulse
        # p_final = 50 + 50 = 100 kg·m/s
        # v_final = 100/10 = 10 m/s
        p_final = p_initial + j
        v_final = p_final / 10
        assert v_final == 10
