from typing import Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.courses import (Course as CourseModel,
                                Module as ModuleModel,
                                Lesson as LessonModel)

from src.schemas.courses import (Course, CourseModules, CourseNew, Module,
                                 ModuleNew, ModuleLessons, Lesson, LessonNew)


async def get_course_list(db: AsyncSession) -> list[Course]:
    courses = await db.execute(select(CourseModel))
    courses = courses.scalars().all()
    return [Course.from_orm(course) for course in courses]


async def get_course_by_id(db: AsyncSession, id: int) -> Union[Course, None]:
    course_in_db = await db.execute(
        select(CourseModel).where(CourseModel.id==id)
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
