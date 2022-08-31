from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.groups import Group as GroupModel
from src.schemas.groups import Group, NewGroup


async def get_groups_list(db: AsyncSession) -> list[Group]:
    groups = await db.execute(select(GroupModel))
    groups = groups.scalars().all()
    return [Group.from_orm(group) for group in groups]


async def get_group_by_id(db: AsyncSession, id: int) -> Union[Group, None]:
    group_in_db = await db.execute(select(GroupModel).where(GroupModel.id==id))
    group_in_db = group_in_db.scalars().first()
    if not group_in_db:
        return None
    return Group.from_orm(group_in_db)


async def add_group(db: AsyncSession, data: NewGroup) -> Group:
    new_group = GroupModel(**data.dict())
    db.add(new_group)
    await db.commit()
    await db.refresh(new_group)
    return Group.from_orm(new_group)
