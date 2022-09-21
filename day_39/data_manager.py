import requests
from flight_search import FlightSearch
from pprint import pprint

SHEET_ENDPOINT = 'https://api.sheety.co/5c285828057ed114987d9150c97b40af/flightDeals/prices'


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def destination_datas(self):
        response = requests.get(SHEET_ENDPOINT)
        sheet_data = response.json()
        self.destination_data = sheet_data['prices']
        return self.destination_data

    def update_destination(self):
        # parameters = {"email": {"name": "chaeyun", "email": "cysh2635@naver.com"}}
        for city in self.destination_data:
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=new_code)
            print(response.text)
