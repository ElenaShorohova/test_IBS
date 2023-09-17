from typing import Any

from pytest import mark

from api.services.reqres_users import ReqresUsers
from api.status_codes import StatusCodes
from scheme.schema_user import ListUsersResponse


class TestGetListUsers:

    @mark.parametrize('number_of_pages', [1, 2, 3])
    def test_get_list_users(self, number_of_pages: int):
        response = ReqresUsers().get_list_users(params={'page': number_of_pages})
        assert response.status_code == StatusCodes.STATUS_200, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        ListUsersResponse.model_validate(response.json())

    @mark.bug
    @mark.parametrize('number_of_pages', ['string', True, [3]])
    def test_negative_get_list_users(self, number_of_pages: Any):
        response = ReqresUsers().get_list_users(params={'page': number_of_pages})
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'
