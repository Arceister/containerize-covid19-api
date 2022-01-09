import requests
import json
from fastapi import FastAPI

def print_object(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

base_url = "https://data.covid19.go.id/public/api/"
response = requests.get(base_url + "update.json").json()

def base_return_response():
    return_dict = {}
    return_dict["ok"] = True
    return return_dict

def return_normal_data():
    return_dict = base_return_response()
    return_dict["data"] = response["update"]["total"]
    return_dict["message"] = "success"
    return return_dict

def return_one_response(date):
    return_dict = base_return_response()
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
    return_dict.update(data_list)
    return return_dict

app = FastAPI()

@app.get("/")
async def root():
    return return_normal_data()

@app.get("/yearly/{year}")
async def read_parameter(year):
    return return_one_response(year)

@app.get("/monthly/{year}/{month}")
async def read_parameter(year, month):
    return return_one_response((year + "." + month).replace(".", "-"))

@app.get("/daily/{year}/{month}/{date}")
async def read_parameter(year, month, date):
    return return_one_response((year + "." + month + "." + date).replace(".", "-"))