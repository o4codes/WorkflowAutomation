from models.condition import Condition

class TrafficSourceCondition(Condition):
    """ This class is used to check if the traffic source is correct
    """
    def __init__(self, traffic_source: str):
        super().__init__()
        self.traffic_source = traffic_source

    def execute(self, expected_result: str) -> bool:
        """ This executes the condition
        """
        return self.traffic_source.casefold() == expected_result.casefold()

class CheckProductStatus(Condition):
    """ This class is used to check if the product status is correct
    """
    def __init__(self, product_status: str):
        super().__init__()
        self.product_status = product_status

    def execute(self, expected_result: str) -> bool:
        """ This executes the condition
        """
        return self.product_status.casefold() == expected_result.casefold()

class OnSignUp(Condition):
    """ This class is used to check if the condition is on sign up
    """
    def __init__(self, is_signed_up: bool):
        super().__init__()
        self.is_signed_up = is_signed_up

    def execute(self, expected_result: bool) -> bool:
        """ This executes the condition
        """
        return self.is_signed_up == expected_result