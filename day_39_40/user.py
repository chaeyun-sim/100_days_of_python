import requests

API_ID = '42020348'
API_KEY = '21704ed61f9fe815689f1c996ab6e2cb'
USER_SHEETY_ENDPOINT = 'https://api.sheety.co/5c285828057ed114987d9150c97b40af/flightDeals/users'

print("Welcome to Angela's Flight Club.\nWe find the best flight deals and email you.")
firstname = input("What is your first name?\n")
lastname = input("What is your last name?\n")
email = input("What is your email?\n")
confirm_email = input("Type your email again.\n")

if email == confirm_email:
    print("You're in the club!")
    config = {"user": {"firstName": firstname, "lastName": lastname, 'email': email}}
    response = requests.post(USER_SHEETY_ENDPOINT, json=config)
    # print(response.text)
else:
    print("Error! Doesn't match.")