"""An interface for serviceable objects."""

from abc import ABC, abstractmethod

class Serviceable(ABC):
    """An interface for serviceable objects.
    """
    @abstractmethod
    def needs_service(self):
        """Determines if the object needs to be serviced.

        This method needs to be implemented by the subclass.
        """

