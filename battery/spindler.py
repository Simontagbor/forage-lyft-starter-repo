"""This module defines a specilised Battery named Spindler Battery.
"""

from datetime import datetime
from battery.base_battery import Battery
from utils.input_validator import validate_date


class SpindlerBattery(Battery):
    """Creates SpindlerBattery instances.
    Inherits from the Battery class.

    methods:
        needs_serviced: Determines if the battery should be serviced.
    """
    def __init__(self, last_service_date: datetime,
                 current_date: datetime):
        """Ïnitializes SpindlerBattery objects."""
        # validate input
        current_date = validate_date(current_date)
        self.current_date = current_date
        self.last_service_date = last_service_date


    def needs_service(self) -> bool:
        """Determines if the Spindler Battery should be serviced.
        Returns:
            bool: True if it's been Two years(730 days) since the last service date.
        Usage:
            >>> battery = SpindlerBattery(....)
            >>> battery.needs_service()
        """
        service_time_threshold = self.current_date - self.last_service_date
        return service_time_threshold.days >=  730