from core.tasks import SendEmail, SendSMS, VisitWebsite, AddOrRemoveFromList, ApplyOrRemoveTags, RegisterForWebinar
from core.conditions import CheckProductStatus, OnSignUp, TrafficSourceCondition
from core.workflow import WorkFlow

workflow_one = WorkFlow(VisitWebsite(url="https://test.com/signup"))
root_id = workflow_one.root_node.id

# branch one
visit_facebook = workflow_one.add_task(root_id, VisitWebsite(url="https://facebook.com"))
workflow_one.add_condition(visit_facebook.id, TrafficSourceCondition("facebook", "facebook", True))

# branch two
facebook_upgrade_page = workflow_one.add_task(root_id, VisitWebsite(url="https://facebook.com/upgrade"))
workflow_one.add_condition(facebook_upgrade_page.id, TrafficSourceCondition("facebook", "facebook", True))
workflow_one.add_condition(facebook_upgrade_page.id, CheckProductStatus("purchase", "purchase"))

# branch three
find_facebook_page = workflow_one.add_task(root_id, VisitWebsite(url='https://facebook.com/find'))
workflow_one.add_condition(find_facebook_page.id, OnSignUp(True, True))
workflow_one.add_condition(find_facebook_page.id, TrafficSourceCondition("Unknown", "google", False))

#branch four
facebook_upgrade_page_2 = workflow_one.add_task(root_id, VisitWebsite(url="https://facebook.com/upgrade"))
workflow_one.add_condition(facebook_upgrade_page_2.id, OnSignUp(True, True))
workflow_one.add_condition(facebook_upgrade_page_2.id, TrafficSourceCondition("google", "google", True))

# execute workflow
workflow_one.execute()