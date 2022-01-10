from fastapi.exceptions import HTTPException
from api.covid_api.covid_api import response
from fastapi import FastAPI
import datetime
from dateutil.relativedelta import relativedelta
from api.routes import root

def return_specific_data_response(date) -> dict:
    date_indicator = "year" if len(date) == 4 else "month" if len(date) == 7 else "date"
    data_list = {
        date_indicator: date,
        "positive": 0,
        "recovered": 0,
        "deaths": 0,
        "active": 0,
    }
    for data in response["update"]["harian"]:
        if (data["key_as_string"][: + len(date)] == date):
            data_list["positive"] += int(data["jumlah_positif"]["value"])
            data_list["recovered"] += int(data["jumlah_sembuh"]["value"])
            data_list["deaths"] += int(data["jumlah_meninggal"]["value"])
            data_list["active"] += int(data["jumlah_positif"]["value"]) - int(data["jumlah_sembuh"]["value"]) - int(data["jumlah_meninggal"]["value"])
    return_dict = {
        "ok": True,
        "data": data_list,
        "message": "success"
    }
    return return_dict

def return_yearly_list_object(since, upto) -> dict:
    current_timestamp = str(datetime.datetime.now())

    #Error Handling
    if since > upto:
        return {"ok": False, "message": "since can't be higher than upto!"}
    if upto > int(current_timestamp[:4]):
        return {"ok": False, "message": "upto can't exceed now!"}
    if since < 2020:
        return {"ok": False, "message": "since can't be lower than 2020!"}
    
    data_list_to_show = []

    for years in range(since, upto+1):
        data_list_to_show.append(return_specific_data_response(str(years))["data"])

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }

def return_monthly_list_object(since, upto) -> dict:
    data_list_to_show = []

    current_month = datetime.datetime.strptime(since, "%Y.%m")
    target_upto_month = datetime.datetime.strptime(upto, "%Y.%m")

    while current_month <= target_upto_month:
        data_list_to_show.append(return_specific_data_response(str(current_month)[:7])["data"])
        current_month += relativedelta(months = 1)

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }

def return_monthly_list_object_with_year(since, upto, year) -> dict:
    if since[:4] != upto[:4]:
        return HTTPException(422, "the year between two parameters must be the same year!")
    if str(since[:4]) != str(year) or str(upto[:4]) != str(year):
        return HTTPException(422, "query parameter year must be same with path parameter year!")
    if year == "2020":
        since = since[:5] + "03"
    if year != "2020":
        since = year + since[4:]
        upto = year + upto[4:]

    data_list_to_show = []

    current_month = datetime.datetime.strptime(since, "%Y.%m")
    target_upto_month = datetime.datetime.strptime(upto, "%Y.%m")

    while current_month <= target_upto_month:
        data_list_to_show.append(return_specific_data_response(str(current_month)[:7])["data"])
        current_month += relativedelta(months = 1)

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }

def return_daily_list_object(since, upto) -> dict:
    data_list_to_show = []

    current_date = datetime.datetime.strptime(since, "%Y.%m.%d")
    target_upto_date = datetime.datetime.strptime(upto, "%Y.%m.%d") if response["update"]["penambahan"]["tanggal"] == str(upto.replace(".", "-")) else datetime.datetime.strptime(upto, "%Y.%m.%d") - datetime.timedelta(days=1)

    while current_date <= target_upto_date:
        data_list_to_show.append(return_specific_data_response(str(current_date)[:10])["data"])
        current_date += datetime.timedelta(days=1)

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }

def return_daily_list_object_with_year(since, upto, year) -> dict:
    data_list_to_show = []

    if since[:4] != upto[:4]:
        return HTTPException(422, "the year between two parameters must be the same year!")
    if str(since[:4]) != str(year) or str(upto[:4]) != str(year):
        return HTTPException(422, "query parameter year must be same with path parameter year!")
    if year == "2020":
        since = since[:5] + "03.20"
    if year != "2020":
        since = year + since[4:]
        upto = year + upto[4:]

    current_date = datetime.datetime.strptime(since, "%Y.%m.%d")
    target_upto_date = datetime.datetime.strptime(upto, "%Y.%m.%d") if response["update"]["penambahan"]["tanggal"] == str(upto.replace(".", "-")) else datetime.datetime.strptime(upto, "%Y.%m.%d") - datetime.timedelta(days=1)

    while current_date <= target_upto_date:
        data_list_to_show.append(return_specific_data_response(str(current_date)[:10])["data"])
        current_date += datetime.timedelta(days=1)

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }

def return_daily_list_object_with_year_and_monthly(since, upto, year, month) -> dict:
    data_list_to_show = []

    current_date = datetime.datetime.strptime(since, "%Y.%m.%d")
    target_upto_date = datetime.datetime.strptime(upto, "%Y.%m.%d") if response["update"]["penambahan"]["tanggal"] == str(upto.replace(".", "-")) else datetime.datetime.strptime(upto, "%Y.%m.%d") - datetime.timedelta(days=1)

    while current_date <= target_upto_date:
        data_list_to_show.append(return_specific_data_response(str(current_date)[:10])["data"])
        current_date += datetime.timedelta(days=1)

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }

app = FastAPI()

app.include_router(root.router)

@app.get("/yearly")
async def read_query(since: int = 2020, upto: int = 2022):
    return return_yearly_list_object(since.replace(".", "-"), upto.replace(".", "-"))

@app.get("/yearly/{year}")
async def read_parameter(year: str):
    return return_specific_data_response(year)

@app.get("/monthly")
async def read_query(since: str = "2020.03", upto: str = str(datetime.datetime.now())[:7].replace("-", ".")):
    return return_monthly_list_object(since, upto)

@app.get("/monthly/{year}")
async def read_query_and_parameter(year: str, since: str = "2020.01", upto: str = "2020.12"):
    return return_monthly_list_object_with_year(since, upto, year)

@app.get("/monthly/{year}/{month}")
async def read_parameter(year: str, month: str):
    return return_specific_data_response((year + "." + month).replace(".", "-"))

@app.get("/daily")
async def read_query(since: str = "2020.03.02", upto: str = str(datetime.datetime.now())[:10].replace("-", ".")):
    return return_daily_list_object(since, upto)

@app.get("/daily/{year}")
async def read_query(since: str = "2020.03.02", upto: str = "2020.12.31", year: str = "2020"):
    return return_daily_list_object_with_year(since, upto, year)

@app.get("/daily/{year}/{month}")
async def read_query(since: str = "2020.03.02", upto: str = "2020.03.31", year: str = "2020", month: str = "03"):
    return return_daily_list_object_with_year_and_monthly(since, upto, year, month)

@app.get("/daily/{year}/{month}/{date}")
async def read_parameter(year: str, month: str, date: str):
    return return_specific_data_response((year + "." + month + "." + date).replace(".", "-"))