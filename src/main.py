from fastapi import FastAPI

from src.api.v1.routers import router_v1

app = FastAPI()
app.include_router(router_v1)


@app.get('/')
async def index():
    return {'message': 'Dl academy App, ready'}
