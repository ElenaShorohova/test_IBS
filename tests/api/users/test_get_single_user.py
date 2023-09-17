from typing import Any

from pytest import mark

from api.services.reqres_users import ReqresUsers
from api.status_codes import StatusCodes
from scheme.schema_user import SingleUserResponse


class TestGetUser:

    @mark.parametrize('number_of_id_users', [1, 2, 3])
    def test_get_user(self, number_of_id_users: int):
        response = ReqresUsers().get_single_user(user_id=number_of_id_users)
        assert response.status_code == StatusCodes.STATUS_200, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        SingleUserResponse.model_validate(response.json())

    @mark.parametrize('number_of_id_users', ['string', True, [3]])
    def test_get_user(self, number_of_id_users: Any):
        response = ReqresUsers().get_single_user(user_id=number_of_id_users)
        assert response.status_code == StatusCodes.STATUS_404, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_404}'
