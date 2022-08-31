from fastapi import APIRouter

from .courses.routers import courses_router
from .groups.routers import groups_router
from .users.routers import users_router

router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(users_router, tags=['users'])
router_v1.include_router(groups_router, tags=['groups'])
router_v1.include_router(courses_router, tags=['courses'])
