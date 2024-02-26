"""Defines a specilised Battery named Nubin Battery.
"""

from datetime import datetime
from battery.base_battery import Battery
from utils.input_validator import validate_date


class NubbinBattery(Battery):
    """Creates NubbinBattery instances.
    Inherits from the Battery class.

    methods:
        needs_service: Determines if the battery should be serviced.
    """
    def __init__(self, last_service_date: datetime, current_date: datetime):
        """Ïnitializes NubbinBattery objects."""
        # validate input
        last_service_date = validate_date(last_service_date)
        current_date = validate_date(current_date)
        # initialize instance
        self.current_date = current_date
        self.last_service_date = last_service_date


    def needs_service(self) -> bool:
        """Determines if the NubbinBattery should be serviced.
        Usage:
            >>> battery = NubbinBattery(....)
            >>> battery.needs_service()
        """
        service_time_threshold = self.current_date - self.last_service_date
        return service_time_threshold.days >= 1460
