from models.task import Task

class SendEmail(Task):
    """ This class is used to send an email
    """
    def __init__(self, email: str):
        super().__init__()
        self.email = email

    def execute(self) -> bool:
        """ This executes the task
        """
        print(f"Sending email to {self.email}")
        return True

class SendSMS(Task):
    """ This class is used to send an SMS
    """
    def __init__(self, mobile_number: str):
        super().__init__()
        self.mobile_number = mobile_number
    
    def execute(self) -> bool:
        """ This executes the task
        """
        print(f"Sending SMS to {self.mobile_number}")
        return True

class VisitWebsite(Task):
    """ This class is used to visit a website
    """
    def __init__(self, url: str):
        super().__init__()
        self.url = url
    
    def execute(self) -> bool:
        """ This executes the task
        """
        print(f"Visiting website {self.url}")
        return True

class AddOrRemoveFromList(Task):
    """ This class is used to add or remove an item from a list
    """
    def __init__(self, action: str, item: str):
        super().__init__()
        self.action = action
        self.item = item
    
    def execute(self) -> bool:
        """ This executes the task
        """
        print(f"{self.action}ing {self.item} from the list")
        return True

class ApplyOrRemoveTags(Task):
    """ This class is used to apply or remove tags to an item
    """
    def __init__(self, action: str, item: str):
        super().__init__()
        self.action = action
        self.item = item
    
    def execute(self) -> bool:
        """ This executes the task
        """
        print(f"{self.action}ing {self.item} tags")
        return True

class RegisterForWebinar(Task):
    """ This class is used to register for a webinar
    """
    def __init__(self, webinar: str, email: str):
        super().__init__()
        self.webinar = webinar
        self.email = email
    
    def execute(self) -> bool:
        """ This executes the task
        """
        print(f"Registering for {self.webinar} with {self.email}")
        return True