from api.covid_api.covid_api import response

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