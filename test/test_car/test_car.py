"""Tests the creation of Car onjects"""
import unittest
from datetime import datetime

from car_factory import CarFactory

factory = CarFactory()


class TestCalliope(unittest.TestCase):
    """Tests the servicing criteria of a calliope car"""
    def test_battery_needs_service(self):
        """Test Need for Calliope Car Servicing -> Consideration: Battery"""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_calliope(today, last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_needs_no_service(self):
        """Test No Need For Calliope Car Servicing. -> Consideration: Battery"""
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
        """Test Need for Calliope Car Servicing -> Consideration: Engine"""
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
        """Test No Need for Calliope Car Servicing -> Consideration: Engine"""
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
    """Tests the servicing criteria of a Glissade car"""
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
        """Test No Need for Glissade Car Servicing -> Consideration: Engine"""
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
        """Test Need for Palindrome Car Servicing -> Consideration: Battery"""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = factory.create_palindrome(today,
                                        last_service_date,
                                        warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_needs_no_service(self):
        """Test No Need for Palindrome Car Servicing -> Consideration: Battery"""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = factory.create_palindrome(today,
                                        last_service_date,
                                        warning_light_is_on)
       
        self.assertFalse(car.battery.needs_service())

    def test_engine_needs_service(self):
        """Test Need for Palindrome Car Servicing -> Consideration: Engine"""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = factory.create_palindrome(today,
                                        last_service_date,
                                        warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_needs_no_service(self):
        """Test No Need for Palindrome Car Servicing -> Consideration: Engine"""
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = factory.create_palindrome(today,
                                        last_service_date,
                                        warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    """Test Servicing criteria for a Rorschach Car"""
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
        """Test No Need for Rorschach Car Servicing -> Consideration: Battery"""
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
