from api.api import TestRequest
from api.services.reqres_register import ReqresRegister
from api.status_codes import StatusCodes
from scheme.schema_register_login import LoginUserResponse


class TestUnsuccessfulRegister(TestRequest):

    def test_unsuccessful_register_user(self):
        response = ReqresRegister().register_user(body={'email': 'eve.holt@reqres.in'})
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'
        LoginUserResponse.model_validate(response.json())

