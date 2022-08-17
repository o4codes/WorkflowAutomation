# Task Automation Tool Proof of Concept

## Introduction

This is a proof of concept to demostrate tasks workflow automation tool.
This proof of concept demonstrate how a group of tasks can be run in a manner to form workflow.
Conditions can be created and attached to each task. Therefore, the result of the condition can 
decide either to progress to lower node task, or to end.

## Dependencies

1. Language: Python
2. Minimum version to be used: Python 3.8
3. No external libraries was used

## Setup

1. Download Python3.8 according to Operating System being used
2. Clone the repository with the command `git clone https://github.com/o4codes/WorkflowAutomationPOC`
3. cd into the WorkflowAutomationPOC folder.
4. Run the example workflow using the command `python runner.py`

## Project Desription

The project is divided into three major structure: Task(Actions), Conditions, Workflows

### Task (Action)

A task is an action that would be carried out. Tasks could contain conditions that must run in order before the task can be carried out.
The specification of task is located in the /models/task.py file. A Task abstract class is defined within the file and it specifies the necessary
characteristics of any class that implements it.
A task object can include other set of tasks and set of conditions. The task uses an observer pattern, meaning that once a task is executed,
the notify method can be called. The notify method executes other tasks attached to that single tasl.
Every class that inherits the Task Abstract class must override the execute method to provide it's own means of execution.
In /core/tasks.py file sample tasks classes were created to demonstrate the how tasks can be created.
Sample tasks provided are SendEmail, SendSMS, VisitWebsite, AddOrRemoveFromList, ApplyOrRemoveTags, RegisterForWebinar

### Condition

A condition is an operation which must return a boolean result (True or False) after execution.
Conditions can be attached to a Task to determine if the task should be executed or not.
The specification for a condition is defined in the models/condition.py file. An abstract class is defined 
which provides an abstract method execute. Therefore every sample condition must provide it's own implementation of the execute method.
In core/conditions.py sample condition were provided to demostrate how tasks can be created.
Sample conditions provided are: CheckProductStatus, OnSignUp, TrafficSourceCondition

### Workflow

A workflow is a series of tasks defined in a tree structure and executed in same manner.
A class Workflow inside the core/workflow.py file is defined to descibe the structure of a workflow.
The workflow creates a series of tasks as a tree of task. Therefore this means a single task represent a node in the structure.
Set of other node tasks can be attached to a single task. Therefore those set of tasks depend on their root node to execute before
their execution.
Each task node created in a workflow is assigned an id, therefore using that id, other tasks_nodes can be attached to the task.

For the workflow to be initalised a root_node has to be defined. Other tasks created can then be added to the task. Conditions are evaluated firstly, before a task is executed

The workflow class defines the following methods:

1. get task: gets a task node
2. get_child_tasks: gets list of child task of parent
3. add_task: adds task to a parent task node
4. add_condition: adds a conditon to a tasl
5. remove_task_node: removes a task node and it's dependencies from the workflow
6. remove_condition: removes condition from task node
7. execute: executes workflow

## Example

An example is located in the runner.py file. It was designed to reflect the workflow in diagram below

!['example diagram'](/diagrams/diagram.png)