"""Unit Tests for the Base Battery and Derived Nubbin and Spindler Batteries
"""

import unittest
from abc import ABC
from datetime import datetime
from battery.base_battery import Battery
from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery

from utils.input_validator import validate_date


class TestBattery(unittest.TestCase):
    """Tests for the Battery Class
    This tests that the Battery base class is correctly implemented according to specification
    """
    def test_battery_is_subclass_of_abstract_base_class(self):
        """Test that the Battery class is an instance of the ABC class"""
        self.assertTrue(issubclass(Battery, ABC))

    def test_battery_needs_service(self):
        """Test that the Battery class has a needs_service method"""
        self.assertTrue(hasattr(Battery, 'needs_service'))


class TestNubbinBattery(unittest.TestCase):
    """Tests for the NubbinBattery Class
    This tests that the NubbinBattery class is correctly implemented
    """
    def test_nubbin_battery_is_subclass_of_battery(self):
        """Test that the NubbinBattery class is an instance of the Battery class"""
        self.assertTrue(issubclass(NubbinBattery, Battery))

    def test_nubbin_battery_needs_service(self):
        """Test that the NubbinBattery class has a needs_service method"""
        self.assertTrue(hasattr(NubbinBattery, 'needs_service'))

    def test_nubbin_battery_needs_service_returns_bool(self):
        """Test that the needs_service method returns a boolean"""
        current_date = validate_date(datetime.now())
        last_service_date = validate_date(datetime.now())
        self.assertIsInstance(NubbinBattery(last_service_date, current_date).needs_service(), bool)
    
    def test_nubbin_battery_needs_service_returns_true(self):
        """Test that the needs_service method returns True when the battery needs service"""
        current_date = validate_date(datetime.now())
        base_year = 2024
        current_year = datetime.now().year
        year_difference = 6 + ((current_year - base_year) // 3)
        last_service_date = current_date.replace(year=current_date.year - year_difference)
        self.assertTrue(NubbinBattery(last_service_date, current_date).needs_service())

    def test_nubbin_battery_needs_service_returns_false(self):
        """Test that the needs_service method returns 
        False when the battery does not need service"""
        current_date = validate_date(datetime.now())
        last_service_date = validate_date(datetime.now())
        self.assertFalse(NubbinBattery(last_service_date, current_date).needs_service())


class TestSpindlerBattery(unittest.TestCase):
    """Tests for the SpindlerBattery Class
    This tests that the SpindlerBattery class is correctly implemented
    """
    def test_spindler_battery_is_subclass_of_battery(self):
        """Test that the SpindlerBattery class is an
        instance of the Battery class"""
        self.assertTrue(issubclass(SpindlerBattery, Battery))

    def test_spindler_battery_needs_service(self):
        """Test that the SpindlerBattery class has a needs_service method"""
        self.assertTrue(hasattr(SpindlerBattery, 'needs_service'))

    def test_spindler_battery_needs_service_returns_bool(self):
        """Test that the needs_service method returns a boolean"""
        current_date = validate_date(datetime.now())
        last_service_date = validate_date(datetime.now())
        self.assertIsInstance(SpindlerBattery(last_service_date, current_date).needs_service(), bool)

    def test_spindler_battery_needs_service_returns_true(self):
        """Test that the needs_service method returns True when the battery needs service"""
        current_date = validate_date(datetime.now())
        base_year = 2024
        current_year = datetime.now().year
        year_difference = 3 + ((current_year - base_year) // 3)
        last_service_date = current_date.replace(year=current_date.year - year_difference)
        self.assertTrue(SpindlerBattery(last_service_date, current_date).needs_service())

    def test_spindler_battery_needs_service_returns_false(self):
        """Test that the needs_service method
        returns False when the battery does not need service"""
        current_date = validate_date(datetime.now())
        last_service_date = validate_date(datetime.now())
        self.assertFalse(SpindlerBattery(last_service_date, current_date).needs_service())


if __name__ == '__main__':
    unittest.main()
