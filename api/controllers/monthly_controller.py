import datetime
from dateutil.relativedelta import relativedelta
from api.covid_api.covid_api import response
from fastapi.exceptions import HTTPException
from api.controllers.return_data import return_specific_data_response

def return_monthly_object(month) -> dict:
    current_month = datetime.datetime.strptime(month, "%Y-%m")
    target_upto_month = datetime.datetime.strptime(str(response["update"]["penambahan"]["tanggal"])[:7], "%Y-%m")

    if (current_month > target_upto_month or current_month < datetime.datetime.strptime("2020-03", "%Y-%m")):
        raise HTTPException(404, "the month you're looking at is not found!")
    return return_specific_data_response(month)

def return_monthly_list_object(since, upto) -> dict:
    current_month = datetime.datetime.strptime(month, "%Y-%m")
    target_upto_month = datetime.datetime.strptime(str(response["update"]["penambahan"]["tanggal"])[:7], "%Y-%m")

    if (current_month > target_upto_month or current_month < datetime.datetime.strptime("2020-03", "%Y-%m")):
        raise HTTPException(404, "the month you're looking at is not found!")

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
        raise HTTPException(422, "the year between two parameters must be the same year!")
    if str(since[:4]) != str(year) or str(upto[:4]) != str(year) and year != "2020":
        since = year + since[4:]
        upto = year + upto[4:]
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