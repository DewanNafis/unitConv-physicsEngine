"""Unit tests for motion simulations."""

import pytest
import math
from simulation.motion import falling_body, projectile_range, GRAVITY


class TestFallingBody:
    """Test falling body simulation function."""
    
    def test_falling_body_at_zero_time(self):
        """Test falling body at time zero."""
        assert falling_body(0) == 0
    
    def test_falling_body_one_second(self):
        """Test falling body after one second."""
        expected = 0.5 * GRAVITY * 1**2
        assert falling_body(1) == pytest.approx(expected)
        assert falling_body(1) == pytest.approx(4.905)
    
    def test_falling_body_two_seconds(self):
        """Test falling body after two seconds."""
        expected = 0.5 * GRAVITY * 2**2
        assert falling_body(2) == pytest.approx(expected)
        assert falling_body(2) == pytest.approx(19.62)
    
    def test_falling_body_three_seconds(self):
        """Test falling body after three seconds."""
        expected = 0.5 * GRAVITY * 3**2
        assert falling_body(3) == pytest.approx(expected)
        assert falling_body(3) == pytest.approx(44.145)
    
    def test_falling_body_decimal_time(self):
        """Test falling body with decimal time."""
        expected = 0.5 * GRAVITY * 1.5**2
        assert falling_body(1.5) == pytest.approx(expected)
    
    def test_falling_body_negative_time_raises(self):
        """Test that negative time raises ValueError."""
        with pytest.raises(ValueError, match="Time cannot be negative"):
            falling_body(-1)


class TestProjectileRange:
    """Test projectile range simulation function."""
    
    def test_projectile_range_45_degrees(self):
        """Test projectile range at 45 degrees (maximum range angle)."""
        # At 45 degrees, sin(90°) = 1, so R = u²/g
        u = 20
        expected = (u ** 2) / GRAVITY
        assert projectile_range(u, 45) == pytest.approx(expected, rel=0.001)
    
    def test_projectile_range_zero_angle(self):
        """Test projectile range at 0 degrees (horizontal)."""
        # At 0 degrees, sin(0) = 0, so range should be 0
        assert projectile_range(20, 0) == pytest.approx(0, abs=0.001)
    
    def test_projectile_range_90_degrees(self):
        """Test projectile range at 90 degrees (vertical)."""
        # At 90 degrees, sin(180°) = 0, so range should be 0
        assert projectile_range(20, 90) == pytest.approx(0, abs=0.001)
    
    def test_projectile_range_30_degrees(self):
        """Test projectile range at 30 degrees."""
        u = 20
        angle = 30
        expected = (u ** 2 * math.sin(math.radians(2 * angle))) / GRAVITY
        assert projectile_range(u, angle) == pytest.approx(expected, rel=0.001)
    
    def test_projectile_range_60_degrees(self):
        """Test projectile range at 60 degrees."""
        u = 20
        angle = 60
        expected = (u ** 2 * math.sin(math.radians(2 * angle))) / GRAVITY
        assert projectile_range(u, angle) == pytest.approx(expected, rel=0.001)
    
    def test_projectile_range_symmetry(self):
        """Test that complementary angles give the same range."""
        u = 25
        # 30° and 60° should give same range (complementary angles)
        range_30 = projectile_range(u, 30)
        range_60 = projectile_range(u, 60)
        assert range_30 == pytest.approx(range_60, rel=0.001)
    
    def test_projectile_range_zero_velocity(self):
        """Test projectile range with zero initial velocity."""
        assert projectile_range(0, 45) == 0
    
    def test_projectile_range_negative_velocity_raises(self):
        """Test that negative initial velocity raises ValueError."""
        with pytest.raises(ValueError, match="Initial velocity cannot be negative"):
            projectile_range(-20, 45)


class TestMotionSimulationsIntegration:
    """Integration tests for motion simulations."""
    
    def test_falling_body_increases_with_time(self):
        """Test that falling distance increases with time."""
        d1 = falling_body(1)
        d2 = falling_body(2)
        d3 = falling_body(3)
        
        assert d1 < d2 < d3
    
    def test_falling_body_quadratic_relationship(self):
        """Test that falling distance has quadratic relationship with time."""
        # Distance at 2s should be 4x distance at 1s
        d1 = falling_body(1)
        d2 = falling_body(2)
        assert d2 == pytest.approx(4 * d1)
    
    def test_projectile_maximum_at_45_degrees(self):
        """Test that maximum range occurs at 45 degrees."""
        u = 30
        range_30 = projectile_range(u, 30)
        range_45 = projectile_range(u, 45)
        range_60 = projectile_range(u, 60)
        
        assert range_45 > range_30
        assert range_45 > range_60
    
    def test_projectile_range_increases_with_velocity(self):
        """Test that range increases with initial velocity."""
        angle = 45
        r1 = projectile_range(10, angle)
        r2 = projectile_range(20, angle)
        r3 = projectile_range(30, angle)
        
        assert r1 < r2 < r3
    
    def test_realistic_falling_scenarios(self):
        """Test realistic falling scenarios."""
        # Drop from 1 meter (should take ~0.45s)
        # Using d = 0.5*g*t² => t = sqrt(2*d/g)
        time_1m = math.sqrt(2 * 1 / GRAVITY)
        assert falling_body(time_1m) == pytest.approx(1, rel=0.01)
        
        # Drop from 10 meters (should take ~1.43s)
        time_10m = math.sqrt(2 * 10 / GRAVITY)
        assert falling_body(time_10m) == pytest.approx(10, rel=0.01)
    
    def test_realistic_projectile_scenarios(self):
        """Test realistic projectile scenarios."""
        # A ball thrown at 15 m/s at 45° should travel ~23m
        range_val = projectile_range(15, 45)
        assert 22 < range_val < 24  # Should be around 22.94m
        
        # A ball thrown at 20 m/s at 30° should travel ~35m
        range_val = projectile_range(20, 30)
        assert 34 < range_val < 36  # Should be around 35.35m
