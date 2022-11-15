from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.courses import get_course_by_id
from src.crud.groups import add_group, get_group_by_id, get_groups_list
from src.crud.users import get_user_by_id
from src.db.depends import get_db
from src.schemas.groups import Group, NewGroup

groups_router = APIRouter(prefix='/groups')


@groups_router.get('/', response_model=list[Group])
async def groups_list(db: AsyncSession = Depends(get_db)) -> list[Group]:
    return await get_groups_list(db)


@groups_router.post('/', response_model=Group)
async def create_group(data: NewGroup,
                       db: AsyncSession = Depends(get_db)) -> Group:
    course = await get_course_by_id(db, data.course_id)
    if course is None:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='This Course not exist')

    lector = await get_user_by_id(db, data.lector_id)
    if lector is None:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='This Lector not exist')

    new_group = await add_group(db, data)
    return new_group


@groups_router.get('/{id}', response_model=Group)
async def get_group(id: int, db: AsyncSession = Depends(get_db)) -> Group:
    group = await get_group_by_id(db, id)
    if group is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail='This Group not found')
    return group
