from core.tasks import SendEmail, SendSMS, VisitWebsite, AddOrRemoveFromList, ApplyOrRemoveTags, RegisterForWebinar
from core.conditions import CheckProductStatus, OnSignUp, TrafficSourceCondition
from core.workflow import WorkFlow

workflow_one = WorkFlow(AddOrRemoveFromList("add", "Sample Item"))
root_id = workflow_one.node.id

# Add a task to the workflow
email_added_task =  workflow_one.add_task(root_id, SendEmail("oforkansi.shadrach@gmail.com"))
# Add a condition to the email task
workflow_one.add_condition(email_added_task.id, OnSignUp(True, True))
webinar_added_task = workflow_one.add_task(email_added_task.id, RegisterForWebinar("https://www.webinar.com", "oforkansi.shadrach@gmail.com"))


# Add a task to the workflow
sms_added_task =  workflow_one.add_task(root_id, SendSMS("+972522222222"))
# Add a condition to the sms task
workflow_one.add_condition(sms_added_task.id, OnSignUp(True, True))

workflow_one.execute()