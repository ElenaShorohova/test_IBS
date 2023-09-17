from api.api import TestRequest
from api.services.reqres_login import ReqresLogin
from api.status_codes import StatusCodes
from scheme.schema_register_login import LoginUserResponse


class TestSuccessfulLogin(TestRequest):

    def test_successful_login_user(self):
        response = ReqresLogin().login_user(body={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'})
        assert response.status_code == StatusCodes.STATUS_200, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        LoginUserResponse.model_validate(response.json())

    def test_negative_successful_login_user(self):
        response = ReqresLogin().login_user(body={'email': '123', 'password': 'cityslicka'})
        assert response.status_code == StatusCodes.STATUS_400, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'

