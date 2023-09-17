from typing import Any

from pytest import mark

from api.api import TestRequest
from api.services.reqres_users import ReqresUsers
from api.status_codes import StatusCodes


class TestDeleteUser(TestRequest):

    @mark.parametrize('number_of_id_users', [1, 2, 3])
    def test_delete_user(self, number_of_id_users: int):
        response = ReqresUsers().delete_user(user_id=number_of_id_users)
        assert response.status_code == StatusCodes.STATUS_204, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_204}'

    @mark.bug
    @mark.parametrize('number_of_id_users', ['string', True, [3]])
    def test_negative_delete_user(self, number_of_id_users: Any):
        response = ReqresUsers().delete_user(user_id=number_of_id_users)
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'
