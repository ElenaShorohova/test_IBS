from requests import Response

from api.api import EnumMethods
from api.services.reqres import ReqresApi


class ReqresResources(ReqresApi):
    """Класс методов ресурсов"""

    def __init__(self):
        super().__init__()

    def get_list_resource(self) -> Response:
        """Получить список ресурсов

        Returns:
            Объект ответа
        """
        return self.common_request(method=EnumMethods.GET, url=f'{self.url}/unknown')

    def get_single_resource(self, user_id: int) -> Response:
        """Получить ресурс

        Args:
            user_id: айди пользователя

        Returns:
            Объект ответа
        """
        return self.common_request(method=EnumMethods.GET, url=f'{self.url}/unknown/{user_id}')

    def get_resource_not_found(self, user_id: int) -> Response:
        """Получить данные, что ресурс не существует

        Args:
            user_id: айди пользователя

        Returns:
            Объект ответа
        """
        return self.common_request(method=EnumMethods.GET, url=f'{self.url}/unknown/{user_id}')
