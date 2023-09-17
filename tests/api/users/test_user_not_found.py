from pytest import mark

from api.services.reqres_users import ReqresUsers
from api.status_codes import StatusCodes


class TestSingleUserNotFound:

    @mark.parametrize('number_of_id_users', [22, 23, 24])
    def test_single_user_not_found(self, number_of_id_users: int):
        response = ReqresUsers().get_single_user(user_id=number_of_id_users)
        assert response.status_code == StatusCodes.STATUS_404, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_404}'
        assert not response.json()
