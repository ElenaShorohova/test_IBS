from requests import Response

from api.api import EnumMethods
from api.services.reqres import ReqresApi


class ReqresLogin(ReqresApi):
    """Класс метода логина пользователя"""

    def __init__(self):
        super().__init__()

    def login_user(self, body: dict) -> Response:
        """Получить токен для логина

        Args:
            body: Тело запроса:
                email: почта пользователя
                password: пароль пользователя

        Returns:
            Объект ответа

        """
        return self.common_request(method=EnumMethods.POST, url=f'{self.url}/login', body=body)
