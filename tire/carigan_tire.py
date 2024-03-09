"""Implements a subclass of the Tire class.

The module contains the CariganTire class that inherits from the Tire class.
"""

from tire.base_tire import Tire
from utils.input_validator import validate_array


class CariganTire(Tire):
    """Creates CariganTire tires.

    Inherits from the Tire class.

    methods:
        needs_serviced: Determines if the tire should be serviced.
    """
    tire_wear_sensor = []

    def __init__(self, tire_wear_sensor: list):
        """Initializes CariganTire objects."""
        # validate input
        tire_wear_sensor = validate_array(tire_wear_sensor, 'tire_wear_sensor')
        self.tire_wear_sensor = tire_wear_sensor

    def needs_service(self) -> bool:
        """Determines if the CariganTire should be serviced.

        Returns:
            bool: True if one or more of the values in the
            tire wear sensor array is greater than or equal to 0.9 and
            False otherwise.

        Usage:
            tire = CariganTire([0.5, 0.8, 0.9])
            tire.needs_service()
        """
        return any(i >= 0.9 for i in self.tire_wear_sensor)
