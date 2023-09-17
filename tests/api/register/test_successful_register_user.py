from api.api import TestRequest
from api.services.reqres_register import ReqresRegister
from api.status_codes import StatusCodes
from scheme.schema_register_login import RegisterUserResponse


class TestSuccessfulRegister(TestRequest):

    def test_successful_register_user(self):
        response = ReqresRegister().register_user(body={'email': 'eve.holt@reqres.in', 'password': 'pistol'})
        assert response.status_code == StatusCodes.STATUS_200, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        RegisterUserResponse.model_validate(response.json())

    def test_negative_successful_register_user(self):
        response = ReqresRegister().register_user(body={'email': '123', 'password': 'pistol'})
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'

