import datetime
from api.controllers.return_data import return_specific_data_response
from api.covid_api.covid_api import response
from fastapi import HTTPException

def return_daily_object(date) -> dict:
    request_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.datetime.strptime(str(response["update"]["penambahan"]["tanggal"])[:10], "%Y-%m-%d")

    if (request_date > current_date or request_date < datetime.datetime.strptime("2020-03-02", "%Y-%m-%d")):
        raise HTTPException(404, "the date you're looking at is not found!")

    return return_specific_data_response(date)

def return_daily_list_object(since, upto) -> dict:
    since_date = datetime.datetime.strptime(since, "%Y.%m.%d")
    upto_date = datetime.datetime.strptime(upto, "%Y.%m.%d")
    current_date = datetime.datetime.strptime(str(response["update"]["penambahan"]["tanggal"])[:10], "%Y-%m-%d")

    if (since_date > current_date or since_date < datetime.datetime.strptime("2020-03-01", "%Y-%m-%d")
        or upto_date > current_date or upto_date < datetime.datetime.strptime("2020-03-01", "%Y-%m-%d")):
        raise HTTPException(404, "the date you're looking at is not found!")

    data_list_to_show = []    

    while since_date <= upto_date:
        data_list_to_show.append(return_specific_data_response(str(since_date)[:10])["data"])
        since_date += datetime.timedelta(days=1)

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }

def return_daily_list_object_with_year(since, upto, year) -> dict:
    since_date = datetime.datetime.strptime(since, "%Y.%m.%d")
    upto_date = datetime.datetime.strptime(upto, "%Y.%m.%d")
    current_date = datetime.datetime.strptime(str(response["update"]["penambahan"]["tanggal"])[:10], "%Y-%m-%d")

    data_list_to_show = []

    if (since_date > current_date or since_date < datetime.datetime.strptime("2020-03-02", "%Y-%m-%d")
        or upto_date > current_date or upto_date < datetime.datetime.strptime("2020-03-02", "%Y-%m-%d")):
        raise HTTPException(404, "the date you're looking at is not found!")
    if since[:4] != upto[:4]:
        raise HTTPException(422, "the year between two parameters must be the same year!")
    if str(since[:4]) != str(year) or str(upto[:4]) != str(year) and year != "2020":
        since = year + since[4:]
        upto = year + upto[4:]
    if year != "2020":
        since = year + since[4:]
        upto = year + upto[4:]

    since_date = datetime.datetime.strptime(since, "%Y.%m.%d")
    upto_date = datetime.datetime.strptime(upto, "%Y.%m.%d")

    while since_date <= upto_date:
        data_list_to_show.append(return_specific_data_response(str(since_date)[:10])["data"])
        since_date += datetime.timedelta(days=1)

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }

def return_daily_list_object_with_year_and_month(since, upto, year, month) -> dict:
    since_date = datetime.datetime.strptime(since, "%Y.%m.%d")
    upto_date = datetime.datetime.strptime(upto, "%Y.%m.%d")
    current_date = datetime.datetime.strptime(str(response["update"]["penambahan"]["tanggal"])[:10], "%Y-%m-%d")

    if (since_date > current_date or since_date < datetime.datetime.strptime("2020-03-02", "%Y-%m-%d")
        or upto_date > current_date or upto_date < datetime.datetime.strptime("2020-03-02", "%Y-%m-%d")):
        raise HTTPException(404, "the date you're looking at is not found!")
    if since[:4] != upto[:4]:
        raise HTTPException(422, "the year between two parameters must be the same year!")
    if str(since[:4]) != str(year) or str(upto[:4]) != str(year) and year != "2020":
        since = year + since[4:]
        upto = year + upto[4:]
    if year == "2020":
        since = since[:5] + "03"
    if year == "2020" and since[:5] == "01.01":
        since = since[:5] + "03.02"

    data_list_to_show = []

    while since_date <= upto_date:
        data_list_to_show.append(return_specific_data_response(str(since_date)[:10])["data"])
        since_date += datetime.timedelta(days=1)

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }