from typing import Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.courses import Course as CourseModel

from src.models.groups import Group
from src.models.users import User

from src.schemas.courses import Course, CourseNew


async def get_course_list(db: AsyncSession) -> list[Course]:
    courses = await db.execute(select(CourseModel))
    courses = courses.scalars().all()
    return [Course.from_orm(course) for course in courses]


async def get_course_by_id(db: AsyncSession, id: int) -> Union[Course, None]:
    course_in_db = await db.execute(
        select(CourseModel).where(CourseModel.id == id)
    )
    course_in_db = course_in_db.scalars().first()
    if not course_in_db:
        return None
    return Course.from_orm(course_in_db)


async def add_course(db: AsyncSession, data: CourseNew) -> Course:
    new_course = CourseModel(**data.dict())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return Course.from_orm(new_course)


async def get_user_courses(db: AsyncSession, user_id: int) -> list[Course]:
    user_groups = await db.execute(
        select(Group.course).where(Group.students.any(User.id == user_id))
    )
    print(user_groups.scalars().all())
    return []
