from enum import Enum

from fastapi import Form
from pydantic import BaseModel, EmailStr, root_validator


class UserType(str, Enum):
    OWNER = 'owner'
    LECTOR = 'lector'
    MENTOR = 'mentor'
    STUDENT = 'student'


class UserBase(BaseModel):
    first_name: str = ""
    last_name: str = ""
    phone: str = ""
    email: EmailStr
    patronomyc: str = ""
    type: UserType = UserType.STUDENT

    class Config:
        orm_mode = True

class SignIn(BaseModel):
    email: EmailStr
    password: str


class SignUp(SignIn):
    confirm_password: str

    @root_validator
    def check_passwords_match(cls, values):
        pw1, pw2 = values.get('password'), values.get('confirm_password')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return values


class User(UserBase):
    id: int
    password: str
    active: str = False

    class Config:
        orm_mode = True


class Token(BaseModel):
    token: str
    token_type: str = 'Bearer'
