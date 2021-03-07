
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from . import service
from . schemas import StoreCreate, StoreList, StoreSingle


router = APIRouter()


@router.get("/", response_model=List[StoreList])
async def store_list():
    return await service.get_store_list()


@router.post("/", status_code=201, response_model=StoreSingle)
async def store_create(item: StoreCreate):
    return await service.create_store(item)


@router.get("/{pk}", response_model=StoreSingle)
async def store_single(pk: int):
    store = await service.get_store(pk)
    if store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@router.put("/{pk}", status_code=201, response_model=StoreSingle)
async def store_create(
        pk: int, item: StoreCreate
    ):
    return await service.update_store(pk, item)


@router.delete("/{pk}", status_code=204)
async def store_create(pk: int):
    return await service.delete_store(pk)