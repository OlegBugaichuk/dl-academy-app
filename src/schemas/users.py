from enum import IntEnum

from fastapi import Form
from pydantic import BaseModel, EmailStr, root_validator


class UserType(IntEnum):
    OWNER = 1
    LECTOR = 2
    MENTOR = 3
    STUDENT = 4


class UserBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    patronomyc: str = ""
    type: UserType = UserType.STUDENT


class SignIn():
    def __init__(self, email: str = Form(), password: str = Form()):
        self.email = email
        self.password = password


class SignUp(SignIn):
    def __init__(self,
                 email: str = Form(),
                 password: str = Form(),
                 confirm_password: str = Form()):

        self.confirm_password = confirm_password
        super().__init__(email, password)

    # @root_validator
    # def check_passwords_match(cls, values):
    #     pw1, pw2 = values.get('password'), values.get('confirm_password')
    #     if pw1 is not None and pw2 is not None and pw1 != pw2:
    #         raise ValueError('passwords do not match')
    #     return values


class User(UserBase):
    id: int
    hashed_password: str
    active: str = False

    class Config:
        orm_mode = True


class Token(BaseModel):
    token: str
    token_type: str = 'Bearer'
