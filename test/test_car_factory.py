"""Tests for the CarFactory class.
This module contains the following test classes:
    TestCarFactory: Tests the CarFactory class.

    Summary of:
            test_create_[car_type]: Tests the Factory methods designed for 
            creating specialised instances of the  Car class.
            test_[car_type]_components: Currently Tests the engine and battery components of created Car objects.
"""
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from car_factory import CarFactory

# import engines
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
# import batteries
from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery


class TestCarFactory(unittest.TestCase):
    """Tests the CarFactory class."""
    @patch('car_factory.Car', autospec=True)
    @patch('car_factory.CapuletEngine')
    @patch('car_factory.SpindlerBattery')
    def test_create_calliope(self,  mock_battery, mock_engine, mock_car):
        """Tests the creation of a Calliope car."""
        # Arrange Mock calliope car
        factory = CarFactory()
        mock_car.return_value = mock_car
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        mock_engine.return_value = MagicMock()
        mock_battery.return_value = MagicMock()
        # create calliope car
        car = factory.create_calliope(current_date,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)

        # Assert
        mock_car.assert_called_once_with(mock_engine.return_value, mock_battery.return_value)
        self.assertEqual(car, mock_car)

    def test_calliope_components(self):
        """Tests the creation of a Calliope engine and battery."""
        # Arrange
        factory = CarFactory()
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_calliope(current_date,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)

        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)



    @patch('car_factory.Car', autospec=True)
    @patch('car_factory.WilloughbyEngine')
    @patch('car_factory.SpindlerBattery')
    def test_create_glissade(self, mock_battery, mock_engine, mock_car):
        """Tests the creation of a Glissade car."""	
        # Arrange Mock glisade car
        factory = CarFactory()
        mock_car.return_value = mock_car
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        mock_engine.return_value = MagicMock()
        mock_battery.return_value = MagicMock()

        # create glissade car
        car = factory.create_glissade(current_date,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)
        # Assert
        mock_car.assert_called_once_with(mock_engine.return_value, mock_battery.return_value)
        self.assertEqual(car, mock_car)

    def test_glissade_components(self):
        """Tests the creation of a glissade engine and battery."""
        # Arrange
        factory = CarFactory()
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_glissade(current_date,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)

        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    @patch('car_factory.Car', autospec=True)
    @patch('car_factory.SternmanEngine')
    @patch('car_factory.SpindlerBattery')
    def test_create_palindrome(self, mock_battery, mock_engine, mock_car):
        """Tests the creation of a Palindrome car."""
        # Arrange Mock sternman car
        factory = CarFactory()
        mock_car.return_value = mock_car
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        warning_light_is_on = False

        mock_engine.return_value = MagicMock()
        mock_battery.return_value = MagicMock()
        # create palindrome car
        car = factory.create_palindrome(current_date,
                                        last_service_date,
                                        warning_light_is_on)

        # Assert
        mock_car.assert_called_once_with(mock_engine.return_value, mock_battery.return_value)
        self.assertEqual(car, mock_car)

    def test_palindrome_components(self):
        """Tests the creation of 
        engine and battery components of palindrome."""
        # Arrange
        factory = CarFactory()
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        warning_light_is_on = False

        car = factory.create_palindrome(current_date,
                                      last_service_date,
                                      warning_light_is_on)

        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    @patch('car_factory.Car', autospec=True)
    @patch('car_factory.WilloughbyEngine')
    @patch('car_factory.NubbinBattery')
    def test_create_rorschach(self, mock_battery, mock_engine, mock_car):
        """Tests the creation of a Rorschach car."""
        # Arrange Mock rorschach car
        factory = CarFactory()
        mock_car.return_value = mock_car
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        mock_engine.return_value = MagicMock()
        mock_battery.return_value = MagicMock()

        # create rorschach car
        car = factory.create_rorschach(current_date,
                                       last_service_date,
                                       current_mileage,
                                       last_service_mileage)

        # Assert
        mock_car.assert_called_once_with(mock_engine.return_value, mock_battery.return_value)
        self.assertEqual(car, mock_car)

    def test_rorschach_components(self):
        """Tests the creation of the appropriate engine and battery for rorschach."""
        # Arrange
        factory = CarFactory()
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_rorschach(current_date,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)

        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)

    @patch('car_factory.Car', autospec=True)
    @patch('car_factory.CapuletEngine')
    @patch('car_factory.NubbinBattery')
    def test_create_thovex(self, mock_battery, mock_engine, mock_car):
        """Tests the creation of a Thovex car."""
        # Arrange Mock thovex car
        factory = CarFactory()
        mock_car.return_value = mock_car
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        mock_engine.return_value = MagicMock()
        mock_battery.return_value = MagicMock()

        # create thovex car
        car = factory.create_thovex(current_date,
                                    last_service_date,
                                    current_mileage,
                                    last_service_mileage)

        # Assert
        mock_car.assert_called_once_with(mock_engine.return_value, mock_battery.return_value)
        self.assertEqual(car, mock_car)

    # test thovex components
    def test_thovex_components(self):
        """Tests the creation of a thovex engine and battery."""
        # Arrange
        factory = CarFactory()
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = factory.create_thovex(current_date,
                                      last_service_date,
                                      current_mileage,
                                      last_service_mileage)

        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, NubbinBattery)



if __name__ == '__main__':
    unittest.main()
