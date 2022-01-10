from api.routes.root import app
from api.covid_api.covid_api import response
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root_function():
    response_result = client.get("/")
    assert response_result.status_code == 200
    assert response_result.json() == {
        "ok": True,
        "data": {
            "total_positive": response["update"]["total"]["jumlah_positif"],
            "total_recovered": response["update"]["total"]["jumlah_sembuh"],
            "total_deaths": response["update"]["total"]["jumlah_meninggal"],
            "total_active": response["update"]["total"]["jumlah_dirawat"],
            "new_positive": response["update"]["penambahan"]["jumlah_positif"],
            "new_recovered": response["update"]["penambahan"]["jumlah_sembuh"],
            "new_deaths": response["update"]["penambahan"]["jumlah_meninggal"],
            "new_active": response["update"]["penambahan"]["jumlah_dirawat"]
        },
        "message": "success"
    }