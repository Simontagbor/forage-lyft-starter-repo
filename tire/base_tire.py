"""Defines the base class for creating tire objects.
"""

from abc import ABC, abstractmethod


class Tire(ABC):
    """Creates Tire objects.

    Inherits from the ABC class.

    methods:
        needs_serviced: Determines if the tire should be serviced.
    """
    @abstractmethod
    def needs_service(self):
        """Determines if the tire should be serviced.

        This method Needs to be implemented by the subclass.
        """
