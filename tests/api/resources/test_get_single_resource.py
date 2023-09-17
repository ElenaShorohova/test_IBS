from typing import Any

from pytest import mark

from api.services.reqres_resources import ReqresResources
from api.status_codes import StatusCodes
from scheme.schema_resources import SingleResourceResponse


class TestGetSingleResource:

    @mark.parametrize('number_of_id', [1, 2, 3])
    def test_get_single_resource(self, number_of_id: int):
        response = ReqresResources().get_single_resource(user_id=number_of_id)
        assert response.status_code == StatusCodes.STATUS_200, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        SingleResourceResponse.model_validate(response.json())

    @mark.parametrize('number_of_id', ['string', [1, 2, 3], True])
    def test_negative_get_single_resource(self, number_of_id: Any):
        response = ReqresResources().get_single_resource(user_id=number_of_id)
        assert response.status_code == StatusCodes.STATUS_404, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_404}'

