from fastapi import APIRouter
from api.controllers import yearly_controller

router = APIRouter()

@router.get("/yearly")
async def read_query(since: int = 2020, upto: int = 2022):
    return yearly_controller.return_yearly_list_object(since, upto)

@router.get("/yearly/{year}")
async def read_parameter(year: str):
    return yearly_controller.return_yearly_object(year)