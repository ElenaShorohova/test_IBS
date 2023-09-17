from typing import Optional

from pydantic import BaseModel, Field


class LoginUserResponse(BaseModel):
    """Схема ответа запроса успешного логина пользователя"""
    token: Optional[str] = None
    error: Optional[str] = None


class RegisterUserResponse(LoginUserResponse):
    """Схема ответа запроса авторизации"""
    id_: Optional[int] = Field(None, alias='id')
