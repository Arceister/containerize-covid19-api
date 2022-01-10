from requests.models import HTTPError
from api.routes.yearly_router import router
# from api.covid_api.covid_api import response
from fastapi.testclient import TestClient
import pytest

client = TestClient(router)    

def test_yearly_endpoint_function():  
    test_response = client.get('/yearly/2021')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_yearly_endpoint_function_with_default_parameters():
    test_response = client.get('/yearly')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_yearly_endpoint_function_with_given_parameters_on_since():
    test_response = client.get('/yearly?since=2021')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_yearly_endpoint_function_with_given_parameters_on_upto():
    test_response = client.get('/yearly?upto=2021')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_yearly_endpoint_function_with_given_parameters_on_since_and_upto():
    test_response = client.get('/yearly?since=2021&upto=2022')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }