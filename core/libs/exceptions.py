class FyleError(Exception):
    def __init__(self, status_code=400, message="An error occurred"):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
