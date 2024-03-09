"""Defines the Car class."""
from serviceable import Serviceable
from engine.base_engine import Engine
from battery.base_battery import Battery
from tire.base_tire import Tire

class Car(Serviceable):
    """Creates a Car object.

    The Car object is composed of an Engine, Battery and Tire.

    Usage:
        engine = Engine_type(......)
        battery = Battery_type(......)
        tire = Tire_type(......)
        car_instance = Car(engine, battery, tire, ...)
    """
    def __init__(self, engine: Engine, battery: Battery, tire: Tire = None):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        """Check if Car needs to be serviced
        The fucntion checks the service status of each of 
        the components to determine if the car needs service
        """
        return self.engine.needs_service() or self.battery.needs_service()
