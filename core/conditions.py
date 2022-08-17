from models.condition import Condition

class TrafficSourceCondition(Condition):
    """ This class is used to check if the traffic source is correct
    """
    def __init__(self, traffic_source: str, actual_traffic_source: str, expected_result: bool):
        super().__init__()
        self.traffic_source = traffic_source
        self.actual_traffic_source = actual_traffic_source
        self.expected_result = expected_result

    def execute(self) -> bool:
        """ This executes the condition
        """
        return (self.traffic_source == self.actual_traffic_source) == self.expected_result

class CheckProductStatus(Condition):
    """ This class is used to check if the product status is correct
    """
    def __init__(self, product_status: str, expected_result: bool):
        super().__init__()
        self.product_status = product_status
        self.expected_result = expected_result

    def execute(self) -> bool:
        """ This executes the condition
        """
        return self.expected_result

class OnSignUp(Condition):
    """ This class is used to check if the condition is on sign up
    """
    def __init__(self, is_signed_up: bool, expected_result: bool):
        super().__init__()
        self.is_signed_up = is_signed_up
        self.expected_result = expected_result

    def execute(self) -> bool:
        """ This executes the condition
        """
        return self.expected_result == self.is_signed_up