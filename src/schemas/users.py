from pydantic import BaseModel, EmailStr, root_validator
from enum import IntEnum


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
    type: UserType = UserType.student


class UserNew(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @root_validator
    def check_passwords_match(cls, values):
        pw1, pw2 = values.get('password'), values.get('confirm_password')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return values


class User(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    token: 