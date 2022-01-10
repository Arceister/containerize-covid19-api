from fastapi import APIRouter
from api.controllers.root_controller import return_normal_data

router = APIRouter()

@router.get("/")
async def root():
    return return_normal_data()