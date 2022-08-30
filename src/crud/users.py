from typing import Union

from pydantic import parse_obj_as
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.api.v1.users.auth_helpers import get_hash
from src.models.users import User as UserModel
from src.schemas.users import SignUp, User, UserBase


async def get_users_list(db: AsyncSession) -> list[UserBase]:
    users = await db.execute(select(UserModel))
    users = users.scalars().all()
    return [UserBase.from_orm(user) for user in users]


async def get_user_by_email(db: AsyncSession, email: str) -> Union[User, None]:
    user_in_db = await db.execute(
        select(UserModel).where(UserModel.email==email)
    )
    user_in_db = user_in_db.scalars().first()
    if not user_in_db:
        return None
    return User.from_orm(user_in_db)


async def get_user_by_id(db: AsyncSession, id: int) -> Union[UserBase, None]:
    user_in_db = await db.execute(select(UserModel).where(UserModel.id==id))
    user_in_db = user_in_db.scalars().first()
    if not user_in_db:
        return None
    return User.from_orm(user_in_db)


async def signup_user(db: AsyncSession, signup_data: SignUp) -> User:
    hashed_password = get_hash(signup_data.password)
    user = UserModel(email=signup_data.email, password=hashed_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return User.from_orm(user)
