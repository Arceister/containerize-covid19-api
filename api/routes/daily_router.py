from fastapi import APIRouter
from api.controllers import daily_controller
import datetime

router = APIRouter()

@router.get("/daily")
async def read_query(since: str = "2020.03.02", upto: str = str(datetime.datetime.now())[:10].replace("-", ".")):
    return daily_controller.return_daily_list_object(since, upto)

@router.get("/daily/{year}")
async def read_query(since: str = "2020.03.02", upto: str = "2020.12.31", year: str = "2020"):
    return daily_controller.return_daily_list_object_with_year(since, upto, year)

@router.get("/daily/{year}/{month}")
async def read_query(since: str = "2020.03.02", upto: str = "2020.03.31", year: str = "2020", month: str = "03"):
    return daily_controller.return_daily_list_object_with_year_and_monthly(since, upto, year, month)

@router.get("/daily/{year}/{month}/{date}")
async def read_parameter(year: str, month: str, date: str):
    return daily_controller.return_daily_object((year + "." + month + "." + date).replace(".", "-"))