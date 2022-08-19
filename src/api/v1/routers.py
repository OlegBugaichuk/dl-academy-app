from fastapi import APIRouter

from .users.routers import users_router

router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(users_router)
