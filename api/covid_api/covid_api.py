import requests

base_url = "https://data.covid19.go.id/public/api/"
response = requests.get(base_url + "update.json").json()