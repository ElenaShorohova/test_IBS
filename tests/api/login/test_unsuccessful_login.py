from api.api import TestRequest
from api.services.reqres_login import ReqresLogin
from api.status_codes import StatusCodes
from scheme.schema_register_login import LoginUserResponse


class TestUnsuccessfulLogin(TestRequest):

    def test_unsuccessful_login_user(self):
        response = ReqresLogin().login_user(body={'email': 'eve.holt@reqres.in'})
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'
        LoginUserResponse.model_validate(response.json())

