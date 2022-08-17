import unittest
from models.task import Task
from models.condition import Condition
from core.workflow import WorkFlow, WorkFlowNode
from core.tasks import SendEmail, SendSMS, VisitWebsite, AddOrRemoveFromList, ApplyOrRemoveTags, RegisterForWebinar
from core.conditions import CheckProductStatus, OnSignUp, TrafficSourceCondition

class TestWorkflow(unittest.TestCase):
    def setUp(self):
        self.workflow = WorkFlow(VisitWebsite(url="https://test.com/signup"))

    def test_create_workflow(self):
        root_id = "TASK_1"
        self.assertEqual(root_id, self.workflow.root_node.id)

    def test_get_task_success(self):
        root_id = "TASK_1"
        task_node = self.workflow.get_task(root_id)
        self.assertEqual(WorkFlowNode, type(task_node))
        self.assertEqual(issubclass(type(task_node.task), Task), True)

    def test_get_task_fail(self):
        root_id = "022"
        task_node = self.workflow.get_task(root_id)
        self.assertEqual(task_node, None)

    def test_get_child_tasks(self):
        root_id = "TASK_1"
        self.workflow.add_task(root_id, SendEmail("oforkansi.shadrach"))
        self.assertEqual(len(self.workflow.get_child_tasks(root_id)), 1)

    def test_add_task(self):
        root_id = "TASK_1"
        task_node = self.workflow.add_task(root_id, SendEmail("oforkansi.shadrach"))
        task_node = self.workflow.get_task(task_node.id)
        self.assertNotEqual(task_node, None)

    def test_execute(self):
        root_id = "TASK_1"
        task_node = self.workflow.add_task(root_id, SendEmail("oforkansi.shadrach"))
        self.workflow.execute()
        self.assertTrue(self.workflow.is_published)