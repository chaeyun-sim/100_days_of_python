import requests


endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "2834387742b25d5393a21e88fee8246a"


weather_params = {
    "lat" : 35.165608,
    # "lat" : 37.566536
    "lon" : 128.054650,
    # "lon" : 126.977966
    "exclude" : "current,minutely,daily",
    "appid" : api_key,
    }


response = requests.get(endpoint, params=weather_params)
print(response.status_code)
weather_data = response.json()
print(weather_data)