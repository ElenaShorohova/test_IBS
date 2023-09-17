from requests import Response

from api.api import EnumMethods
from api.services.reqres import ReqresApi


class ReqresRegister(ReqresApi):
    """Класс метода регистрации пользователя"""

    def __init__(self):
        super().__init__()

    def register_user(self, body: dict) -> Response:
        """Зарегистрировать нового пользователя

        Args:
            body: тело запроса:
                email: почта пользователя
                password: пароль пользователя

        Returns:
            Объект ответа
        """
        return self.common_request(method=EnumMethods.POST, url=f'{self.url}/register', body=body)
