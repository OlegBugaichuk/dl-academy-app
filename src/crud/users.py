from typing import Union

from src.schemas.users import User, UserBase

fake_users = {
    'non_active@gmail.com':{
        'id': 1,
        'email': 'non_active@gmail.com',
        'first_name': 'Aaron',
        'last_name': 'Gibson',
        'phone': '832-885-2596',
        'hashed_password': '$2b$12$pB4z4fHbDVQcbPlBqt0mtOkglKLkdjCamH6hJMbogYp9BZXh8YF9O'
    },
    'active@gmail.com':{
        'id': 2,
        'email': 'active@gmail.com',
        'first_name': 'Lena',
        'last_name': 'Kuka',
        'phone': '832-885-2596',
        'hashed_password': '$2b$12$pB4z4fHbDVQcbPlBqt0mtOkglKLkdjCamH6hJMbogYp9BZXh8YF9O',
        'active': True
    }
}


async def get_users_list() -> list[UserBase]:
    return [UserBase(**fake_user) for fake_user in fake_users.values()]


async def get_user_by_email(email: str) -> Union[User, None]:
    user_in_db = fake_users.get(email)
    if not user_in_db:
        return None
    return User(**user_in_db)


async def get_user_by_id(id: int) -> Union[UserBase, None]:
    for _, fake_user in fake_users.items():
        if fake_user.get('id') == id:
            return UserBase(**fake_user)
    return None
