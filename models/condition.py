from abc import ABC, abstractmethod

class Condition(ABC):
    """ Abstract class for conditions
    """

    @abstractmethod
    def execute(self, expected_result: bool=True) -> bool:
        pass