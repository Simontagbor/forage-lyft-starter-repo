"""This module implements the Engine class,
which is responsible for creating engine objects."""

from abc import ABC, abstractmethod

class Engine(ABC):
    """This class is responsible for creating different types of engine objects.
    """
    @abstractmethod
    def needs_service(self):
        """Determines if the engine should be serviced.

        This method Needs to be implemented by the subclass.
        """
