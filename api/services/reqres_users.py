from requests import Response

from api.api import EnumMethods
from api.services.reqres import ReqresApi


class ReqresUsers(ReqresApi):
    """Класс методов пользователей"""

    def __init__(self):
        super().__init__()

    def get_list_users(self, params: dict) -> Response:
        """ Получить список пользователей

        Args:
            params: Параметры запроса:
                page - номер страницы
                delay - таймаут перед отправкой

        Returns:
            Объект ответа
        """
        return self.common_request(method=EnumMethods.GET, url=f'{self.url}/users', params=params)

    def get_single_user(self, user_id: int) -> Response:
        """ Получить информацию о пользователе

        Args:
            user_id: айди пользователя

        Returns:
            Объект ответа
        """
        return self.common_request(method=EnumMethods.GET, url=f'{self.url}/users/{user_id}')

    def create_user(self, body: dict) -> Response:
        """ Создать запись о пользователе

        Args:
            body: тело запроса:
                name - имя пользователя
                job - профессия пользователя

        Returns:
            Объект ответа
        """
        return self.common_request(method=EnumMethods.POST, url=f'{self.url}/users', body=body)

    def update_user(self, user_id: int, body: dict) -> Response:
        """ Изменить запись о пользователе

              Args:
                  user_id: айди пользователя
                  body: тело запроса:
                      name - имя пользователя
                      job - профессия пользователя

              Returns:
                  Объект ответа
              """
        return self.common_request(method=EnumMethods.PUT, url=f'{self.url}/users/{user_id}', body=body)

    def work_with_user(self, method: EnumMethods, user_id: int, body: dict) -> Response:
        """Обновить данные о пользователе

        Args:
            method: методы запроса:
            PUT - частичное обновление данных
            PATCH - полное обновление данных
            user_id: айди пользователя
            body: тело запроса
                name - имя пользователя
                job - профессия пользователя

        Returns:
            Объект ответа
        """
        return self.common_request(method=method, url=f'{self.url}/users/{user_id}', body=body)

    def delete_user(self, user_id: int) -> Response:
        """Удалить запись о пользователе

        Args:
            user_id: айди пользователя

        Returns:
            Объект ответа
        """
        return self.common_request(method=EnumMethods.DELETE, url=f'{self.url}/users/{user_id}')

    def delay_users(self, delay: int) -> Response:
        """Задержка

        Args:
            delay: количество секунд до тайм-аута

        Returns:
            Объект ответа
        """
        return self.common_request(method=EnumMethods.GET, url=f'{self.url}/users?delay{delay}')
