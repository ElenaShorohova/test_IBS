from api.services.reqres_resources import ReqresResources
from api.status_codes import StatusCodes
from scheme.schema_resources import ListResourcesResponse


class TestGetListResources:

    def test_get_list_resources(self):
        response = ReqresResources().get_list_resource()
        assert response.status_code == StatusCodes.STATUS_200, \
            f'Статус код {response.status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        ListResourcesResponse.model_validate(response.json())


