from builtins import Exception


class HttpErrorMarvel(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
