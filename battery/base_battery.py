"""This module implements the Battery class,
which is responsible for creating Battery objects."""


from abc import ABC, abstractmethod


class Battery(ABC):
    """This class defines basic attributes of Batteries objects.
    """
    @abstractmethod
    def needs_service(self):
        """Determines if the batery should be serviced. 

        This method Needs to be implemented by the subclass.
        """
