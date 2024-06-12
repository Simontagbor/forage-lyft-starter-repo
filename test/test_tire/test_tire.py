"""Unittests for Tire objects.

The tests cover creation of tire objects and the needs_service method.
"""

import unittest
from abc import ABC
from tire.base_tire import Tire
from tire.carigan_tire import CariganTire
from tire.octo_prime_tire import OctoprimeTire


class TestTire(unittest.TestCase):
    """Tests for the Tire Class.

    The tests checks for the correct implementation of the Tire class.
    """
    def test_tire_is_subclass_of_abstract(self):
        """Test that the Tire class is an instance of the ABC class."""
        self.assertTrue(issubclass(Tire, ABC))

    def test_tire_needs_service(self):
        """Test that the Tire class has a needs_service method."""
        self.assertTrue(hasattr(Tire, 'needs_service'))


class TestCariganTire(unittest.TestCase):
    """Tests for the CariganTire Class.

    The tests checks for the correct implementation of the CariganTire class.
    """
    def test_carigan_tire_is_subclass_of_tire(self):
        """Test that the CariganTire class is an instance of the Tire class"""
        self.assertTrue(issubclass(CariganTire, Tire))

    def test_carigan_tire_needs_service(self):
        """Test that the CariganTire class has a needs_service method"""
        self.assertTrue(hasattr(CariganTire, 'needs_service'))

    def test_carigan_tire_has_tire_wear_sensor(self):
        """Test that the CariganTire class has a tire_wear_sensor attribute"""
        self.assertTrue(hasattr(CariganTire, 'tire_wear_sensor'))

    def test_carigan_tire_wear_sensor_is_array(self):
        """Test that the CariganTire tire wear sensor is implemented as an array attribute"""
        self.assertTrue(isinstance(CariganTire.tire_wear_sensor, list))

    def test_caringan_tire_needs_service_returns_bool(self):
        """Test that the needs_service method returns a boolean"""
        self.assertIsInstance(CariganTire([0.5, 0.8, 0.9]).needs_service(), bool)

    def test_caringan_tire_needs_service_returns_true(self):
        """Test that the needs_service method returns True 
        when one or more of the values in the tire wear sensor array is greater than or equal to 0.9
        """
        self.assertTrue(CariganTire([0.3, 0.9, 0.9]).needs_service())

    def test_caringan_tire_needs_service_returns_false(self):
        """Test that the needs_service method returns False.
        when all the values in the tire wear sensor array is less than 0.9
        """
        self.assertFalse(CariganTire([0.3, 0.8, 0.8]).needs_service())


class TestOctoprimeTire(unittest.TestCase):
    """Tests for the OctoprimeTire Class.

    The tests checks for the correct implementation of the OctoprimeTire class
    """
    def test_octoprime_tire_is_subclass_of_tire(self):
        """Test that the OctoprimeTire class is an instance of the Tire class"""
        self.assertTrue(issubclass(OctoprimeTire, Tire))

    def test_octoprime_tire_needs_service(self):
        """Test that the OctoprimeTire class has a needs_service method"""
        self.assertTrue(hasattr(OctoprimeTire, 'needs_service'))

    def test_octoprime_tire_has_tire_wear_sensor(self):
        """Test that the OctoprimeTire class has a tire_wear_sensor attribute"""
        self.assertTrue(hasattr(OctoprimeTire, 'tire_wear_sensor'))

    def test_octoprime_tire_wear_sensor_is_array(self):
        """Test that the OctoprimeTire tire wear sensor is implemented as an array attribute"""
        self.assertTrue(isinstance(OctoprimeTire.tire_wear_sensor, list))

    def test_octoprime_tire_needs_service_returns_bool(self):
        """Test that the needs_service method returns a boolean"""
        self.assertIsInstance(OctoprimeTire([0.5, 0.8, 0.9]).needs_service(), bool)

    def test_octoprime_tire_needs_service_returns_true(self):
        """Test that the needs_service method returns True 
        when the sum of all values in the tire wear array is greater than or equal to 3
        """
        self.assertTrue(OctoprimeTire([1.0, 1.0, 1.0]).needs_service())

    def test_octoprime_tire_needs_service_returns_false(self):
        """Test that the needs_service method returns False 
        when the sum of all values in the tire wear array is less than 3
        """
        self.assertFalse(OctoprimeTire([1.0, 1.0, 0.9]).needs_service())


if __name__ == '__main__':
    unittest.main()
