import requests
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "bf65f474ee75416085b253e155a35afa"
STOCK_API_KEY = "KHIP80SUCMELLLS2"
TWILIO_SID = 'AC3f9782873573fdc17b5afd00b5372f21'
TWILIO_NUM = "+19014459477"
TWILIO_AUTH_TOKEN = "bbe34d00bb9bc7b3e9c13f3e9dc143fc"

stock_params = {"function": "TIME_SERIES_DAILY", "symbol": STOCK, "apikey": STOCK_API_KEY}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()['Time Series (Daily)']
stock_data_lst = [v for (k, v) in stock_data.items()]

yesterday_data = stock_data_lst[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = stock_data_lst[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

diff = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

up_down = None
if diff > 0:
    up_down = '⬆'
else:
    up_down = '⬇'


diff_percent = round((diff / float(yesterday_closing_price)) * 100, 2)


if abs(diff_percent) > 0:
    news_params = {"q": COMPANY_NAME, "apiKey": NEWS_API_KEY, "qInTitle": COMPANY_NAME}
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    # print(three_articles)
    article_format = [f"{STOCK} {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief:" \
                      f" {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in article_format:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUM,
            to='+821036833426',
        )
    print("Sent!")