from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.courses import add_course, get_course_by_id, get_course_list
from src.db.depends import get_db
from src.schemas.courses import Course, CourseNew

courses_router = APIRouter(prefix='/courses')


@courses_router.get('/', response_model=list[Course])
async def course_list(db: AsyncSession = Depends(get_db)) -> list[Course]:
    return await get_course_list(db)


@courses_router.post('/', response_model=Course)
async def create_course(data: CourseNew,
                        db: AsyncSession = Depends(get_db)) -> Course:
    new_course = await add_course(db, data)
    return new_course


@courses_router.get('/{id}', response_model=Course)
async def get_course(id: int, db: AsyncSession = Depends(get_db)) -> Course:
    course = await get_course_by_id(db, id)
    if course is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail='This Course not found')
    return course