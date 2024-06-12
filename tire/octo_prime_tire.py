"""This module defines a specilised Tire named Octo Prime Tire."""

from tire.base_tire import Tire
from utils.input_validator import validate_array


class OctoprimeTire(Tire):
    """Creates OctoprimeTire instances.
    Inherits from the Tire class.

    methods:
        needs_serviced: Determines if the tire should be serviced.
    """
    tire_wear_sensor = []

    def __init__(self, tire_wear_sensor: list):
        """Initializes OctoprimeTire objects."""
        # validate input
        tire_wear_sensor = validate_array(tire_wear_sensor, 'tire_wear_sensor')
        self.tire_wear_sensor = tire_wear_sensor

    def needs_service(self) -> bool:
        """Determines if the OctoprimeTire should be serviced.

        Returns:
            bool: True when the sum of all values in the tire wear
            array is greater than or equal to 3

        Usage:
            tire = OctoprimeTire([0.5, 0.8, 0.9])
            tire.needs_service()
        """
        return sum(self.tire_wear_sensor) >= 3
