from pydantic import BaseModel, Field

from scheme.schema_user import SingleUserResponse


class ResourceSchema(BaseModel):
    """Схема ресурса"""
    id_: int = Field(alias='id')
    name: str
    year: int
    color: str
    pantone_value: str


class ListResourcesResponse(SingleUserResponse):
    """Схема ответа запроса списка ресурсов"""
    data: list[ResourceSchema]


class SingleResourceResponse(SingleUserResponse):
    """Схема ответа запроса ресурса"""
    data: ResourceSchema
