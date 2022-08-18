from fastapi import APIRouter, Form
from src.schemas.users import User, UserNew
from .email_services import signup_confirm_email_send
from .auth_helpers import verify_hash, get_hash


users_router = APIRouter(prefix='users')


@users_router.get('/', response_model=list[User])
async def users_list() -> list[User]:
    return []


@users_router.get('/{id}', response_model=User)
async def user_detail(id: int) -> User:
    return {'id': id}


@users_router.post('/signup')
async def signup(data: UserNew = Form()):
    await signup_confirm_email_send(data.email)