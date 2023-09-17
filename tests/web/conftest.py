import pytest
from requests import Response

from api.api import EnumMethods
from api.services.reqres_login import ReqresLogin
from api.services.reqres_register import ReqresRegister
from api.services.reqres_resources import ReqresResources
from api.services.reqres_users import ReqresUsers


@pytest.fixture
def get_list_users() -> Response:
    """Получение тела ответа запроса list users"""
    return ReqresUsers().get_list_users(params={'page': 2})


@pytest.fixture
def get_single_user() -> Response:
    """Получение тела ответа запроса single user"""
    return ReqresUsers().get_single_user(user_id=2)


@pytest.fixture
def delay() -> Response:
    """Получение тела ответа запроса delay"""
    return ReqresUsers().delay_users(delay=2)


@pytest.fixture
def delete_user() -> Response:
    """Получение тела ответа запроса delete user"""
    return ReqresUsers().delete_user(user_id=2)


@pytest.fixture
def user_not_found() -> Response:
    """Получение тела ответа запроса delay"""
    return ReqresUsers().work_with_user(
        method=EnumMethods.PUT,
        user_id=2,
        body={"name": "morpheus", "job": "zion resident"}
    )


@pytest.fixture
def successful_login() -> Response:
    """Получение тела ответа запроса login"""
    return ReqresLogin().login_user(body={"email": "eve.holt@reqres.in", "password": "cityslicka"})


@pytest.fixture
def unsuccessful_login() -> Response:
    """Получение тела ответа запроса login"""
    return ReqresLogin().login_user(body={"email": "eve.holt@reqres.in"})


@pytest.fixture
def successful_register() -> Response:
    """Получение тела ответа запроса register"""
    return ReqresRegister().register_user(body={"email": "eve.holt@reqres.in", "password": "pistol"})


@pytest.fixture
def unsuccessful_register() -> Response:
    """Получение тела ответа запроса register"""
    return ReqresRegister().register_user(body={"email": "eve.holt@reqres.in"})


@pytest.fixture
def get_list_resources() -> Response:
    """Получение тела ответа запроса get list resources"""
    return ReqresResources().get_list_resource()


@pytest.fixture
def get_single_resource() -> Response:
    """Получение тела ответа запроса get single resource"""
    return ReqresResources().get_single_resource(user_id=2)
