from typing import Any

from pytest import mark

from api.api import TestRequest
from api.services.reqres_users import ReqresUsers
from api.status_codes import StatusCodes
from scheme.schema_user import ListUsersResponse


class TestDelayUsers(TestRequest):

    @mark.parametrize('number_of_sec', [1, 2, 3])
    def test_delay_users(self, number_of_sec: int):
        response = ReqresUsers().delay_users(delay=number_of_sec)
        assert response.status_code == StatusCodes.STATUS_200, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        ListUsersResponse.model_validate(response.json())

    @mark.bug
    @mark.parametrize('number_of_sec', ['string', True, [3]])
    def test_negative_delay_users(self, number_of_sec: Any):
        response = ReqresUsers().delay_users(delay=number_of_sec)
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'
