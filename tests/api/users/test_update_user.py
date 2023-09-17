from typing import Any

from pytest import mark

from api.api import EnumMethods, TestRequest
from api.services.reqres_users import ReqresUsers
from api.status_codes import StatusCodes
from scheme.schema_user import UpdateUserResponse


class TestUpdateUser(TestRequest):

    @mark.parametrize('number_of_id_users', [1, 2, 3])
    def test_update_put_user(self, number_of_id_users: int):
        response = ReqresUsers().work_with_user(
            method=EnumMethods.PUT,
            user_id=number_of_id_users,
            body={'name': 'morpheus', 'job': 'zion resident'}
        )
        assert response.status_code == StatusCodes.STATUS_200, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        UpdateUserResponse.model_validate(response.json())

    @mark.parametrize('number_of_id_users', [1, 2, 3])
    def test_update_patch_user(self, number_of_id_users: int):
        response = ReqresUsers().work_with_user(
            method=EnumMethods.PATCH,
            user_id=number_of_id_users,
            body={'name': 'neo', 'job': 'zion resident'}
        )
        assert response.status_code == StatusCodes.STATUS_200, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        UpdateUserResponse.model_validate(response.json())

    @mark.bug
    @mark.parametrize('number_of_id_users', ['string', True, [3]])
    def test_negative_update_put_user(self, number_of_id_users: Any):
        response = ReqresUsers().work_with_user(
            method=EnumMethods.PUT,
            user_id=number_of_id_users,
            body={'name': 'morpheus', 'job': 'zion resident'}
        )
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'
        UpdateUserResponse.model_validate(response.json())

    @mark.bug
    @mark.parametrize('number_of_id_users', ['string', True, [3]])
    def test_negative_update_patch_user(self, number_of_id_users: Any):
        response = ReqresUsers().work_with_user(
            method=EnumMethods.PATCH,
            user_id=number_of_id_users,
            body={'name': 'neo', 'job': 'zion resident'}
        )
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'
        UpdateUserResponse.model_validate(response.json())
