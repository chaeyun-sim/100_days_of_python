import requests
from datetime import datetime
import os

API_ID = '42020348'
API_KEY = '21704ed61f9fe815689f1c996ab6e2cb'
USERNAME = 'chaeyun'
PASSWORD = 'codbsajtwoddl123'
TOKEN = 'Y2hhZXl1bjpjb2Ric2FqdHdvZGRsMTIz'
my_height = 160.9
my_weight = 46.7
my_age = 25
now = datetime.now().strftime("%X")
today = datetime.now().strftime("%d/%m/%Y")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
headers = {"x-app-id": API_ID, "x-app-key": API_KEY}
parameters = {
    "query": exercise_text,
    "gender": 'female',
    "weight_kg": my_weight,
    "height_cm": my_height,
    "age": my_age}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)


SHEET_ENDPOINT = 'https://api.sheety.co/5c285828057ed114987d9150c97b40af/workoutTracking/workouts'

for item in result['exercises']:
    sheet_data = {
        'workout':
            {"date": today,
             "time": now,
             "exercise": item['user_input'].title(),
             "duration": item['duration_min'],
             "calories": item['nf_calories']
             }
    }
    bearer_headers = {"Authorization": f'Basic {TOKEN}'}
    # data_response = requests.post(sheet_endpoints, json=sheet_data)
    data_response = requests.post(SHEET_ENDPOINT, json=sheet_data, headers=bearer_headers)
    # print(data_response.text)