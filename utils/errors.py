# A file to handle exception classes.

class SuchClientExists(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class ClientNotFound(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class ClientsNotFound(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)