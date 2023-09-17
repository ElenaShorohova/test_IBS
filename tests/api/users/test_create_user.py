from _pytest import mark

from api.api import TestRequest
from api.services.reqres_users import ReqresUsers
from api.status_codes import StatusCodes
from scheme.schema_user import CreateUserResponse


class TestCreateUser(TestRequest):

    def test_create_user(self):
        response = ReqresUsers().create_user(body={'name': 'morpheus', 'job': 'leader'})
        assert response.status_code == StatusCodes.STATUS_201, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_201}'
        CreateUserResponse.model_validate(response.json())

    @mark.bug
    def test_negative_create_user(self):
        response = ReqresUsers().create_user(body={'name': 123, 'job': ''})
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'

