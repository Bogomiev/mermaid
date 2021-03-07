from fastapi import FastAPI

from src.core.config import PROJECT_NAME
from src.core.db import database
from src.routes import routes

app = FastAPI(title=PROJECT_NAME, debug=False)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(routes)
