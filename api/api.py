from enum import Enum
from typing import Optional

import requests as requests


class EnumMethods(Enum):
    """Перечисление методов"""
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    UPDATE = 'UPDATE'


class TestRequest:
    """Класс сервиса апи"""

    @staticmethod
    def common_request(
            method: EnumMethods,
            url: str,
            body: Optional[dict] = None,
            headers: Optional[dict] = None,
            params: Optional[dict] = None
    ):
        response = requests.request(
            method=method.value,
            url=url,
            json=body if body else {},
            headers=headers if headers else {},
            params=params if params else {}
        )
        return response
