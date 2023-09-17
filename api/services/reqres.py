from api.api import TestRequest


class ReqresApi(TestRequest):
    """Корневой класс сервиса API reqres.in"""

    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.url = 'https://reqres.in/api'
