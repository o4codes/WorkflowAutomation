from abc import ABC, abstractmethod
from uuid import uuid4

class Condition(ABC):
    """ Abstract class for conditions
    """

    def __init__(self) -> None:
        self.__id = uuid4()

    @property
    def id(self) -> str:
        """ This returns the id of the condition
        """
        return self.__id

    @abstractmethod
    def execute(self, expected_result) -> bool:
        pass