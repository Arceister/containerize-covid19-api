from fastapi import APIRouter
from api.controllers import monthly_controller
import datetime

router = APIRouter()

@router.get("/monthly")
async def read_query(since: str = "2020.03", upto: str = str(datetime.datetime.now())[:7].replace("-", ".")):
    return monthly_controller.return_monthly_list_object(since, upto)

@router.get("/monthly/{year}")
async def read_query_and_parameter(year: str, since: str = "2020.01", upto: str = "2020.12"):
    return monthly_controller.return_monthly_list_object_with_year(since, upto, year)

@router.get("/monthly/{year}/{month}")
async def read_parameter(year: str, month: str):
    return monthly_controller.return_monthly_object((year + "." + month).replace(".", "-"))