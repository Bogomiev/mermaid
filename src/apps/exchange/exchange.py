from typing import List
from fastapi import APIRouter, Depends, HTTPException
from . import service


router = APIRouter()


# @router.post("/", response_model=List[PostList])
# async def post_list():
#     return await service.get_post_list()