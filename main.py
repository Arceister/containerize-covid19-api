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

def return_yearly_with_year(year):
    return_dict = base_return_response()
    yearly_data_list = {
        "year": year,
        "positive": 0,
        "recovered": 0,
        "deaths": 0,
        "active": 0,
        "message": ""
    }
    for data in response["update"]["harian"]:
        if (data["key_as_string"][:4] == year):
            yearly_data_list["positive"] += int(data["jumlah_positif"]["value"])
            yearly_data_list["recovered"] += int(data["jumlah_sembuh"]["value"])
            yearly_data_list["deaths"] += int(data["jumlah_meninggal"]["value"])
            yearly_data_list["active"] += int(data["jumlah_dirawat"]["value"])
    return_dict.update(yearly_data_list)
    return return_dict


app = FastAPI()

@app.get("/")
async def root():
    return return_normal_data()

@app.get("/yearly/{year}")
async def read_item(year):
    return return_yearly_with_year(year)

