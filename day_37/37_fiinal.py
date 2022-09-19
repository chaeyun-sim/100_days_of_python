import requests
from datetime import datetime

# create pixela account # https://pixe.la/@chaeyun
USERNAME = 'chaeyun-sim'
TOKEN = "codbsajtwoddl123"
GRAPHID = "graph1"
TODAY = datetime.now()

# upload info
pixela_endpoint = "https://pixe.la/v1/users"
user_param = {"token": TOKEN, "username": USERNAME, "agreeTermsOfService": "yes", "notMinor": "yes"}
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

# graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {"id": GRAPHID, "name": 'Study Graph', "unit": "minutes", "type": "int", "color": "sora"}
headers = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post value
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
post_config = {"date": TODAY.strftime("%Y%m%d"), "quantity": input("How much did you study today?")}
# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

# modify value
# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{TODAY.strftime('%Y%m%d')}"
# new_data = {"quantity": "120"}
# response = requests.put(url=put_endpoint, json=new_data, headers=headers)
# print(response.text)

# delete value
# del_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{TODAY.strftime('%Y%m%d')}"
# response = requests.delete(url=del_endpoint, headers=headers)
# print(response.text)
