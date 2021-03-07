from pydantic import BaseModel
from typing import Optional


class StoreBase(BaseModel):
    name: str = ''
    address: str = ''


class PostParent(StoreBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class StoreList(StoreBase):
    id: Optional[int]


class StoreSingle(StoreBase):
    pass


class StoreCreate(StoreBase):
    class Config:
        orm_mode = True
