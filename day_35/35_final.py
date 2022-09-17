import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("MY_API_KEY")
account_sid = os.environ.get("MY_SID")
auth_token = os.environ.get("MY_AUTH_TOKEN")


weather_params = {
    "lat" : 35.165608,
    "lon" : 128.054650,
    # "exclude" : "current,minutely,daily",
    "appid" : api_key,
    }


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]


will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    proxy_client = TwilioHttpClient()
    try:
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    except KeyError:
        pass
    else:

        client = Client(account_sid, auth_token, http_client=proxy_client)
        
        message = client.messages \
            .create(
                body="내일 비가 온다고 합니다. 우산 챙겨 나가도록 하세요 :)",
                from_='my fake phone number',
                to='your friends phone number (verified'
                )
        print(message.status)

