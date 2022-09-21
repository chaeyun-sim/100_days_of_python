# Cheep Flight Finder (API)

import requests
# from twilio
from pprint import pprint
from datetime import datetime
from flight_search import FlightSearch
from data_manager import DataManager

FLIGHT_API_KEY = "rxnJB0qn6KnD39LS6JdkDYp7Qs1KQtSU"
API_ID = ""
TOKEN = 'Y2hhZXl1bjpjb2Ric2FqdHdvZGRsMTIz'
USERNAME = ""
PASSWORD = ""
TRIP_COUNTRY = ""
LIMIT_PRICE = 123
SHEET_ENDPOINT = 'https://api.sheety.co/5c285828057ed114987d9150c97b40af/flightDeals/prices'
now = datetime.now().strftime("%X")
today = datetime.now().strftime("%d/%m/%Y")

datamanager = DataManager()
flight_search = FlightSearch()

sheet_data = datamanager.destination_datas()
# print(sheet_data)


for i in sheet_data:
    if i['iataCode'] == "":
        i['iataCode'] = flight_search.destination_code(i['city'])
print(sheet_data)




# for item in result['prices']:
#     sheet_data = {
#         'workout':
#             {"date": today,
#              "time": now,
#              "exercise": item['user_input'].title(),
#              "duration": item['duration_min'],
#              "calories": item['nf_calories']
#              }
#     }
#     bearer_headers = {"Authorization": f'Basic {TOKEN}'}
#     # data_response = requests.post(sheet_endpoints, json=sheet_data)
#     data_response = requests.post(SHEET_ENDPOINT, json=sheet_data, headers=bearer_headers)
#     print(data_response.text)