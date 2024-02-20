"""Defines the Car class."""

from serviceable import Serviceable
from engine.base_engine import Engine
from battery.base_battery import Battery

class Car(Serviceable):
    """Creates a Car object.
    Returns: a car object with components like engine and battery

    Usage:
        >>> engine = Engine_type(......)
        >>> battery = Battery_type(......)
        >>> car_instance = Car(engine, battery)
    """
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        """Check if Car needs to be serviced
        The fucntion checks the service status of each of 
        the components to determine if the car needs service
        """
        return self.engine.needs_service() or self.battery.needs_service()
