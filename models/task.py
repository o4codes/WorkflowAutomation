from concurrent.futures import ThreadPoolExecutor
from typing import List
from abc import ABC, abstractmethod

from models.condition import Condition

class Task(ABC):
    """
    This class serves as a base class for all all tasks
    """

    def __init__(self):
        self.__observers: List[Task] = []
        self.__conditions: List[Condition] = []

    @abstractmethod
    def execute(self) -> bool:
        """ This executes the task
        """
        pass
    
    def __notify_routine(self, observer: 'Task'):
        """ This is a routine that is used to notify all observers
        """
        if observer.execute_conditions():
            observer.execute()
            observer.notify()

    def notify(self):
        """ This notifies all observers about task execution
        """
        with ThreadPoolExecutor(max_workers=len(self.__observers)) as executor:
            executor.map(self.__notify_routine, self.__observers)

    def execute_conditions(self) -> bool:
        """ This checks all conditions
        """
        for condition in self.__conditions:
            if not condition.execute():
                return False
        return True

    def attach_observer(self, task: 'Task'):
        """ This adds a given task to the list of observers
        """
        self.__observers.append(task)

    def detach_observer(self, task: 'Task'):
        """ This removes a given task from the list of observers
        """
        self.__observers.remove(task)

    def add_condition(self, condition):
        """ This adds a condition to the list of conditions
        """
        self.__conditions.append(condition)

    def remove_condition(self, condition):
        """ This removes a condition from the list of conditions
        """
        self.__conditions.remove(condition)
