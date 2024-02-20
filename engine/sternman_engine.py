"""This module defines a specilised engine named SternmanEngine,
which is responsible for creating SternmanEngine objects.
"""
from datetime import datetime
from engine.base_engine import Engine
from secuirity.input_validator import validate_date, validate_bool



class SternmanEngine(Engine):
    """Creates SternmanEngine objects.
    Inherits from the Engine class.

    methods:
        needs_serviced: Determines if the engine should be serviced.
    """
    def __init__(self, last_service_date: datetime, warning_light_is_on:bool):
        # validate input
        last_service_date = validate_date(last_service_date)
        warning_light_is_on = validate_bool(warning_light_is_on, 'warning_light_is_on')
        # initialize instance
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        """Determines if the engine should be serviced.
        Returns:
            bool: True if the warning light is on False otherwise.
        """
        return self.warning_light_is_on
