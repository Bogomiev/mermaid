from .models import stores
from .schemas import StoreCreate
from src.core.db import database
from sqlalchemy import select


async def get_store_list():
    store_list = await database.fetch_all(query=stores.select())
    return [dict(result) for result in store_list]


async def get_store(pk: int):
    store_list = await database.fetch_all(query=stores.select().where(stores.c.id == pk))
    if store_list is not None:
        return [dict(result) for result in store_list]
    return None


async def create_store(item: StoreCreate):
    store = stores.insert().values(**item.dict())
    pk = await database.execute(store)
    return {**item.dict(), "id": pk}


async def update_store(pk: int, item: StoreCreate):
    store = stores.update().where((stores.c.id == pk))
    return await database.execute(store)


async def delete_store(pk: int):
    store = stores.delete().where((stores.c.id == pk))
    return await database.execute(store)