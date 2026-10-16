from abc import ABC, abstractmethod


class Tax(ABC):
    """
    Abstract tax base class.
    """

    @abstractmethod
    def calculate(self, ctx):
        pass