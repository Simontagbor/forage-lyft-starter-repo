"""Tests the creation of Car onjects."""
import unittest
from unittest.mock import Mock
from datetime import datetime

from car import Car
from serviceable import Serviceable

from car_factory import CarFactory
factory = CarFactory()

class TestCarImplementation(unittest.TestCase):
    """Tests the appropriate implementation of the car class."""
    def setUp(self):
        """set up the test fixtures"""
        self.mock_engine = Mock()
        self.mock_battery = Mock()
        self.mock_tire = Mock()

        self.car = Car(self.mock_engine, self.mock_battery, self.mock_tire)

    def test_car_is_subclass_of_serviceable(self):
        """Test if Car is a subclass of Serviceable."""
        self.assertTrue(issubclass(Car, Serviceable))

    def test_car_has_battery_attribute(self):
        """Test if Car has a battery attribute"""
        self.assertTrue(hasattr(self.car, 'battery'),
                        "Car object doesn't have a battery attribute")

    def test_car_has_engine_attribute(self):
        """Test if Car has an engine attribute"""
        self.assertTrue(hasattr(self.car, 'engine'),
                        "Car object doesn't have an engine attribute")

    def test_car_has_tire_attribute(self):
        """Test if Car has a tire attribute"""
        self.assertTrue(hasattr(self.car, 'tire'),
                        "Car object doesn't have a tire attribute")

    def test_car_has_needs_service_method(self):
        """Test if Car has a needs_service method"""
        self.assertTrue(hasattr(self.car, 'needs_service'),
                        "Car object doesn't have a needs_service method.")

class TestCalliope(unittest.TestCase):
    """Tests the servicing criteria of a calliope car"""
    def test_battery_needs_service(self):
        """Test Need for Calliope Car Servicing -> Consideration: Battery."""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_calliope(today, last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_needs_no_service(self):
        """Test No Need For Calliope Car Servicing. -> Consideration: Battery."""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_calliope(today,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_needs_service(self):
        """Test Need for Calliope Car Servicing -> Consideration: Engine."""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = factory.create_calliope(today,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_needs_no_service(self):
        """Test No Need for Calliope Car Servicing -> Consideration: Engine."""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = factory.create_calliope(today,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    """Tests the servicing criteria of a Glissade car."""
    def test_battery_needs_service(self):
        """Test Need for Glissade Car Servicing -> Consideration: Battery"""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_glissade(today,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_needs_no_service(self):
        """Test No Need For Glissade Car Servicing. -> Consideration: Battery"""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_glissade(today,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_needs_service(self):
        """Test Need for Glissade Car Servicing -> Consideration: Engine"""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = factory.create_glissade(today,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_needs_no_service(self):
        """Test No Need for Glissade Car Servicing -> Consideration: Engine."""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = factory.create_glissade(today,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    """Test Servicing criteria for a Palindrome Car"""
    def test_battery_needs_service(self):
        """Test Need for Palindrome Car Servicing -> Consideration: Battery."""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = factory.create_palindrome(today,
                                        last_service_date,
                                        warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_needs_no_service(self):
        """Test No Need for Palindrome Car Servicing -> Consideration: Battery."""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = factory.create_palindrome(today,
                                        last_service_date,
                                        warning_light_is_on)

        self.assertFalse(car.battery.needs_service())

    def test_engine_needs_service(self):
        """Test Need for Palindrome Car Servicing -> Consideration: Engine."""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = factory.create_palindrome(today,
                                        last_service_date,
                                        warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_needs_no_service(self):
        """Test No Need for Palindrome Car Servicing -> Consideration: Engine."""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = factory.create_palindrome(today,
                                        last_service_date,
                                        warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    """Test Servicing criteria for a Rorschach Car."""
    def test_battery_needs_service(self):
        """Test Need for Rorschach Car Servicing -> Consideration: Battery"""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_rorschach(today,
                                       last_service_date,
                                       current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_needs_no_service(self):
        """Test No Need for Rorschach Car Servicing -> Consideration: Battery."""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_rorschach(today,
                                       last_service_date,
                                       current_mileage,
                                       last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_needs_service(self):
        """Test Need for Rorschach Car Servicing -> Consideration: Engine"""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = factory.create_rorschach(today,
                                       last_service_date,
                                       current_mileage,
                                       last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_needs_no_service(self):
        """Test No Need for Rorschach Car Servicing -> Consideration: Engine"""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = factory.create_rorschach(today,
                                       last_service_date,
                                       current_mileage,
                                       last_service_mileage)

        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    """Test Servicing criteria for a Thovex Car"""
    def test_battery_needs_service(self):
        """Test the Need for Thovex Car Servicing -> Consideration: Battery"""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_thovex(today,
                                    last_service_date,
                                    current_mileage,
                                    last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        """Test No Need for Thovex Car Servicing -> Consideration: Battery"""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_thovex(today,
                                    last_service_date,
                                    current_mileage,
                                    last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_needs_service(self):
        """Test the Need for Thovex Car Servicing -> Consideration: Engine"""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = factory.create_thovex(today,
                                    last_service_date,
                                    current_mileage,
                                    last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_needs_no_service(self):
        """Test No Need for Thovex Car Servicing -> Consideration: Engine"""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = factory.create_thovex(today, last_service_date,
                                    current_mileage,
                                    last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
