
class InvalidLoanInputFormat(Exception):
    def __init__(self, message):
        self.message = message + "\n"


class UnexpectedError(Exception):
    def __init__(self, message):
        self.message = message + "\n"

