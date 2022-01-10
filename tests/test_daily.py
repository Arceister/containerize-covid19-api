from api.routes.daily_router import router
from fastapi.testclient import TestClient

client = TestClient(router)

def test_daily_endpoint_function_with_year_month_and_day():  
    test_response = client.get('/daily/2021/04/02')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_and_month_with_default_parameters():  
    test_response = client.get('/daily/2021/04/')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_and_month_with_different_parameters():  
    test_response = client.get('/daily/2020/09/')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_and_month_with_given_parameters_on_since():  
    test_response = client.get('/daily/2020/09/?since=2020.09.12')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_and_month_with_given_parameters_on_upto():  
    test_response = client.get('/daily/2020/09/?upto=2020.09.25')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_and_month_with_given_parameters_on_since_and_upto():  
    test_response = client.get('/daily/2020/09/?since=2020.09.04&upto=2020.09.25')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_with_default_parameters():  
    test_response = client.get('/daily/2020/')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_with_different_parameters():  
    test_response = client.get('/daily/2021/')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_with_given_parameters_on_since():  
    test_response = client.get('/daily/2020/?since=2020.04.04')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_with_given_parameters_on_upto():  
    test_response = client.get('/daily/2020/?upto=2020.10.03')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_year_with_given_parameters_on_since_and_upto():  
    test_response = client.get('/daily/2020/?since=2020.04.02&upto=2020.08.15')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_default_parameters():  
    test_response = client.get('/daily')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_given_parameters_on_since():  
    test_response = client.get('/daily?since=2020.08.06')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_given_parameters_on_upto():  
    test_response = client.get('/daily?upto=2021.02.12')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }

def test_daily_endpoint_function_with_given_parameters_on_since_and_upto():  
    test_response = client.get('/daily?since=2020.09.21&upto=2021.02.23')
    data_list_from_response = test_response.json()["data"]
    assert test_response.status_code == 200
    assert test_response.json() == {
        "ok": True,
        "data": data_list_from_response,
        "message": "success"
    }