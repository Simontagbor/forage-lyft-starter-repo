"""This module defines a specilised engine named SternmanEngine,
which is responsible for creating SternmanEngine objects.
"""
from engine.base_engine import Engine
from utils.input_validator import validate_bool

class SternmanEngine(Engine):
    """Creates SternmanEngine objects.
    Inherits from the Engine class.

    methods:
        needs_serviced: Determines if the engine should be serviced.
    """
    def __init__(self, warning_light_is_on:bool):
        # validate input
        warning_light_is_on = validate_bool(warning_light_is_on, 'warning_light_is_on')
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        """Determines if the engine should be serviced.
        Returns:
            bool: True if the warning light is on False otherwise.
        """
        if self.warning_light_is_on:
            return True
        return False

