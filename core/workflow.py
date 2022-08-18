from typing import List, Union
from dataclasses import dataclass, field

from models.condition import Condition
from models.task import Task

@dataclass
class WorkFlowNode:
    id: str
    task: Task
    child_nodes: List['WorkFlowNode'] = field(default_factory=list)

class WorkFlow:
    """ This class is used to organize group of tasks and conditions into a workflow
    """
    
    def __init__(self, trigger_task: Task):
        if issubclass(type(trigger_task), Task):
            self.__id_counter = 1
            self.root_node = WorkFlowNode(f"TASK_{self.__id_counter}", trigger_task)
            self.is_published = False
            return None
        raise TypeError("Trigger task must be a subclass of Task")

    def __get_parent_task_node(self, task_id, node: WorkFlowNode) -> WorkFlowNode:
        """ This gets the the parent task node by its id
        """
        children_nodes = node.child_nodes
        if task_id in [child_node.id for child_node in children_nodes]:
            return node
            
        for child_node in node.child_nodes:
            parent_node = self.__get_parent_task_node(task_id, child_node)
            if parent_node:
                return parent_node
        else:
            return None

    def __get_task_node(self, task_id, node: WorkFlowNode) -> WorkFlowNode:
        """ This gets the the task node and the parent task node by its id
        """
        if task_id == node.id:
            return node
        for child_node in node.child_nodes:
            task_node = self.__get_task_node(task_id, child_node)
            if task_node:
                return task_node
        return None

    def get_task(self, task_id: str) -> WorkFlowNode:
        """ This returns a task by its id
        """
        task_node = self.__get_task_node(task_id, self.root_node)
        if task_node:
            return task_node
        return None

    def get_child_tasks(self, task_id = None) -> List[WorkFlowNode]:
        """ Get all child tasks nodes from a parent task node
        """
        if task_id:
            task_node = self.__get_task_node(task_id, self.root_node)
            if task_node:
                return task_node.child_nodes
            return []
        return self.node.child_nodes

    def add_task(self, parent_task_id: str, task: Task) -> WorkFlowNode:
        """ This adds a task to the workflow
        """
        if issubclass(type(task), Task):
            task_node = self.__get_task_node(parent_task_id, self.root_node)
            if task_node:
                self.__id_counter += 1
                new_task_node = WorkFlowNode(f"TASK_{self.__id_counter}", task)
                task_node.child_nodes.append(new_task_node)
                task_node.task.attach_observer(task)
                return new_task_node
            raise ValueError("Parent task does not exist")
        raise TypeError("Task must be a subclass of Task")

    def add_condition(self, parent_task_id: str, condition: Condition) -> Condition:
        """ This adds a condition to the workflow
        """
        if issubclass(type(condition), Condition):
            task_node = self.__get_task_node(parent_task_id, self.root_node)
            if task_node:
                task_node.task.add_condition(condition)
                return condition
            raise ValueError("Parent task does not exist")
        raise TypeError("Condition must be a subclass of Condition")

    def remove_task_node(self, task_id: str):
        """ This removes a task from the workflow
        """
        parent_node = self.__get_parent_task_node(task_id, self.root_node)
        if parent_node:
            task_node = list(filter(lambda node: node.id == task_id, parent_node.child_nodes))[0]
            parent_node.task.detach_observer(task_node.task)
            parent_node.child_nodes.remove(task_node)
            return None
        raise ValueError("Task does not exist")

    def remove_condition(self, task_id: str, condition_id: str):
        """ This removes a condition from the workflow
        """
        task_node = self.__get_task_node(task_id, self.root_node)
        if task_node:
            task_node.task.remove_condition(condition_id)
            return None
        raise ValueError("Task does not exist")

    def execute(self):
        """ This executes the workflow
        """
        self.root_node.task.execute()
        self.root_node.task.notify()
        self.is_published  = True
        return None
