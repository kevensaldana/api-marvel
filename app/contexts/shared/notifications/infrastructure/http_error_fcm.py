from builtins import Exception


class HttpErrorFCM(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
