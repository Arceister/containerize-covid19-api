from fastapi.exceptions import HTTPException
import requests
from fastapi import FastAPI
from typing import Optional
import datetime

base_url = "https://data.covid19.go.id/public/api/"
response = requests.get(base_url + "update.json").json()

def return_normal_data():
    return_dict = {
        "ok": True,
        "data": response["update"]["total"],
        "message": "success"
    }
    return return_dict

def return_specific_data_response(date):
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

def return_yearly_list_object(since, upto):
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

    return data_list_to_show

app = FastAPI()

@app.get("/")
async def root():
    return return_normal_data()

@app.get("/yearly")
async def read_query(since: int = 2020, upto: int = 2022):
    return return_yearly_list_object(since, upto)

@app.get("/yearly/{year}")
async def read_parameter(year: str):
    return return_specific_data_response(year)

@app.get("/monthly/{year}/{month}")
async def read_parameter(year: str, month: str):
    return return_specific_data_response((year + "." + month).replace(".", "-"))

@app.get("/daily/{year}/{month}/{date}")
async def read_parameter(year: str, month: str, date: str):
    return return_specific_data_response((year + "." + month + "." + date).replace(".", "-"))