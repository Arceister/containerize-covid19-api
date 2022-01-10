import fastapi
from api.routes.monthly_router import router
from fastapi.testclient import TestClient

client = TestClient(router)

def test_monthly_endpoint_function_with_year_and_month():  
    test_response = client.get('/monthly/2021/04')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_monthly_endpoint_function_with_year_with_default_parameters():  
    test_response = client.get('/monthly/2020/')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_monthly_endpoint_function_with_year_with_different_parameters():  
    test_response = client.get('/monthly/2021/')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_monthly_endpoint_function_with_year_with_given_parameters_on_since():  
    test_response = client.get('/monthly/2020/?since=2020.04')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_monthly_endpoint_function_with_year_with_given_parameters_on_upto():  
    test_response = client.get('/monthly/2020/?upto=2020.10')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_monthly_endpoint_function_with_year_with_given_parameters_on_since_and_upto():  
    test_response = client.get('/monthly/2020/?since=2020.04&upto=2020.08')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_monthly_endpoint_function_with_default_parameters():  
    test_response = client.get('/monthly')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_monthly_endpoint_function_with_given_parameters_on_since():  
    test_response = client.get('/monthly?since=2020.08')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_monthly_endpoint_function_with_given_parameters_on_upto():  
    test_response = client.get('/monthly?upto=2021.02')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_monthly_endpoint_function_with_given_parameters_on_since_and_upto():  
    test_response = client.get('/monthly?since=2020.09&upto=2021.02')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }