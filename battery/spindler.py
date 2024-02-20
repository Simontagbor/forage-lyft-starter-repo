"""This module defines a specilised Battery named Spindler Battery.
"""

from datetime import datetime
from battery.base_battery import Battery
from secuirity.input_validator import validate_date


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
        last_service_date = validate_date(last_service_date)
        current_date = validate_date(current_date)
        super().__init__(last_service_date)
        self.current_date = datetime.strptime(current_date)
        self.last_service_date = datetime.strptime(last_service_date)


    def needs_service(self) -> bool:
        """Determines if the Spindler Battery should be serviced.
        Returns:
            bool: True if it's been Two years(730 days) since the last service date.
        Usage:
            >>> battery = SpindlerBattery(....)
            >>> battery.needs_service()
        """
        time_difference = (self.current_date - self.last_service_date)
        return time_difference.days >= 730