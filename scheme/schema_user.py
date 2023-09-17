from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """Схема пользователя"""
    id_: int = Field(alias='id')
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str


class SupportSchema(BaseModel):
    """Схема саппорта"""
    url: str
    text: str


class SingleUserResponse(BaseModel):
    """Схема ответа запроса пользователя"""
    data: UserSchema
    support: SupportSchema


class ListUsersResponse(BaseModel):
    """Схема ответа запроса списка пользователей"""
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[UserSchema]
    support: SupportSchema


class UpdateUserResponse(BaseModel):
    """Схема ответа на запрос обновления данных пользователя"""
    name: str
    job: str
    updatedAt: str


class CreateUserResponse(BaseModel):
    """Схема ответа запроса создания пользователя"""
    name: str
    job: str
    id_: str = Field(alias='id')
    createdAt: str

