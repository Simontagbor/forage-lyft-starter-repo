"""This module defines a specilised engine named CapuletEngine,
which is responsible for creating CapuletEngine objects.
"""
from datetime import datetime
from engine.base_engine import Engine
from secuirity.input_validator import validate_date, validate_int

# input validators
class CapuletEngine(Engine):
    """Creates CapuletEngine objects.
    Inherits from the Engine class.

    methods:
        needs_serviced: Determines if the engine should be serviced.
    """
    def __init__(self, last_service_date: datetime,
                 current_mileage: int,
                 last_service_mileage: int):
        """Initializes CapuletEngine objects."""
        # validate input
        last_service_date = validate_date(last_service_date)
        current_mileage = validate_int(current_mileage, 'current_mileage')
        last_service_mileage = validate_int(last_service_mileage, 'last_service_mileage')
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        """Determines if the engine should be serviced.
        Returns:
            bool: True if the engine should be serviced, False otherwise.
        """
        return self.current_mileage - self.last_service_mileage > 30000
