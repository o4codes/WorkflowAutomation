from concurrent.futures import ThreadPoolExecutor
from typing import List
from abc import ABC, abstractmethod
from uuid import uuid4

from models.condition import Condition

class Task(ABC):
    """
    This class serves as a base class for all all tasks
    """

    def __init__(self):
        self.__id = uuid4()
        self.__observers: List[Task] = []
        self.__conditions: List[Condition] = []

    @abstractmethod
    def execute(self) -> bool:
        """ This executes the task
        """
        pass
    
    @property
    def id(self) -> str:
        """ This returns the id of the task
        """
        return self.__id

    def __notify_routine(self, observer: 'Task'):
        """ This is a routine that is used to notify all observers

        Args:
            observer (Task): The observer to notify
        """
        if observer.execute_conditions():
            observer.execute()
            observer.notify()

    def notify(self):
        """ This notifies all observers about task execution
        """
        if len(self.__observers) > 0:
            with ThreadPoolExecutor(max_workers=len(self.__observers)) as executor:
                executor.map(self.__notify_routine, self.__observers)
        return None

    def execute_conditions(self) -> bool:
        """ This checks all conditions
        """
        for condition in self.__conditions:
            if not condition.execute():
                return False
        return True

    def get_observers(self) -> List['Task']:
        """ This returns the list of observers
        """
        return self.__observers

    def get_conditions(self) -> List[Condition]:
        """ This returns the list of conditions
        """
        return self.__conditions

    def attach_observer(self, task: 'Task') -> 'Task':
        """ This adds a given task to the list of observers

        Args:
            task (Task): The observer to add

        Returns:
            Task: The observer added
        """
        if issubclass(type(task), Task):
            self.__observers.append(task)
            return task
        raise TypeError("Observer must be a subclass of Task")

    def detach_observer(self, task: 'Task'):
        """ This removes a given task from the list of observers

        Args:
            task (Task): The observer to remove

        Raises:
            ValueError: If the observer does not exist
            TypeError: If the observer is not a subclass of Task
        """
        if issubclass(type(task), Task):
            task_search = list(filter(lambda observer: str(observer.id) == str(task.id), self.__observers))
            if len(task_search) > 0:
                self.__observers.remove(task_search[0])
                return None
            raise ValueError("Observer not found")
        raise TypeError("Observer must be a subclass of Task")

    def add_condition(self, condition: Condition) -> Condition:
        """ This adds a condition to the list of conditions

        Args:
            condition (Condition): The condition to add
        
        Returns:
            Condition: The condition added
        
        Raises:
            TypeError: If the condition is not a subclass of Condition
        """
        if issubclass(type(condition), Condition):
            self.__conditions.append(condition)
            return condition
        raise TypeError("Condition must be a subclass of Condition")

    def remove_condition(self, condition_id: str):
        """ This removes a condition from the list of conditions

        Args:
            condition_id (str): The id of the condition to remove
        
        Raises:
            ValueError: If the condition does not exist
        """
        condition_search = list(filter(lambda cond: str(cond.id) == str(condition_id), self.__conditions))
        if len(condition_search) > 0:
            self.__conditions.remove(condition_search[0])
            return None
        raise ValueError("Condition not found")
