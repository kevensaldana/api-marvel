from builtins import Exception


class ErrorTimeoutMarvel(Exception):
    def __init__(self):
        self.code = 408
