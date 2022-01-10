from fastapi.exceptions import HTTPException
from api.controllers.return_data import return_specific_data_response
from api.covid_api.covid_api import response

def return_yearly_object(year) -> dict:
    if (int(year) > int(response["update"]["penambahan"]["tanggal"][:4]) or int(year) < 2020):
        raise HTTPException(404, "the year you're looking at is not found!")
    return return_specific_data_response(year)

def return_yearly_list_object(since, upto) -> dict:

    #Error Handling
    if since > upto:
        raise HTTPException(422, "since can't be higher than upto!")
    if upto > int(response["update"]["penambahan"]["tanggal"][:4]):
        raise HTTPException(404, "the year you're looking at from upto is not found!")
    if since < 2020:
        raise HTTPException(404, "the year you're looking at from since is not found!")
    
    data_list_to_show = []

    for years in range(since, upto+1):
        data_list_to_show.append(return_specific_data_response(str(years))["data"])

    return {
        "ok": True,
        "data": data_list_to_show,
        "message": "success"
    }