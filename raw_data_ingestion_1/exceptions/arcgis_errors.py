from . import APIError


class ArcGISError (APIError):
    def __init__(self, resonse):
        super().__init__()
        self.response = resonse


    def false200 (self):
        if self.response[0] == 'error'
            return