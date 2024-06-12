"""This module implements the CarFactory class, which is responsible for creating car objects.
"""
from datetime import datetime
from abc import ABC
from car import Car

# import engines
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
# import batteries
from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery


class CarFactory(ABC):
    """This class is responsible for creating different types of Car objects.
    """

    def create_calliope(self, current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int, last_service_mileage: int) -> Car:

        """Creates a Calliope car object.

        Args:
           current_date (datetime): The current date.
           last_service_date (datetime): The date when the car was last serviced.
           current_mileage (int): The current mileage of the car.
           last_service_mileage (int): The mileage when the car was last serviced.

        Returns:
            Car: car object.
        """
        engine = CapuletEngine(current_mileage,
                               last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        calliope = Car(engine, battery)
        return calliope

    def create_glissade(self, current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int, last_service_mileage: int) -> Car:

        """Creates a Glissade car object.

        Args:
            current_date (datetime): The current date.
            last_service_date (datetime): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage when the car was last serviced.

        Returns:
            Car: car object.
        """
        engine = WilloughbyEngine(current_mileage,
                                  last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        glissade = Car(engine, battery)

        return glissade

    def create_palindrome(self, current_date: datetime,
                          last_service_date: datetime,
                          warning_light_is_on: bool) -> Car:
        """Creates a Palindrome car object.

        Args:
            current_date (datetime): The current date.
            last_service_date (datetime): The date when the car was last serviced.
            warning_light_is_on (bool): True if the warning light is on, False otherwise.

        Returns:
            Car: car object.
        """
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        palindrome = Car(engine, battery)

        return palindrome

    def create_rorschach(self, current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int, last_service_mileage: int) -> Car:

        """Creates a Rorschach car object.

        Args:
            current_date (datetime): The current date.
            last_service_date (datetime): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage when the car was last serviced.

        Returns:
            Car: car object.
        """
        engine = WilloughbyEngine(current_mileage,
                                  last_service_mileage)
        battery = NubbinBattery(last_service_date,
                                          current_date)
        rorschach = Car(engine, battery)
        return rorschach

    def create_thovex(self, current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int, last_service_mileage: int) -> Car:
        """Creates a Thovex car object.

        Args:
            current_date (datetime): The current date.
            last_service_date (datetime): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage when the car was last serviced.

        Returns:
            Car: car object.
        """
        engine = CapuletEngine(current_mileage,
                               last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)

        thovex = Car(engine, battery)

        return thovex
