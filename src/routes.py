from fastapi import APIRouter
from src.apps.references.stores import store

routes = APIRouter()

routes.include_router(store.router, prefix="/references/stores")
