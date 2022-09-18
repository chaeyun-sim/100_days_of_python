# I made the tkinter UI for the stock trading news alert project I did today
# Stock name and company name are entered through the tkinter UI


import requests
from twilio.rest import Client
from tkinter import *

COLOR = '#FCF8E8'
former_stocks = []


def if_clicked():
    STOCK = stock_input.get()
    COMPANY_NAME = company_input.get()

    former_name.config(text=f"Stock Subscribed: {COMPANY_NAME}")

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
        check_label.config(text='Sent!', fg='red')
        timer = window.after(500, remove_check)


def remove_check():
    check_label.config(text="", fg='black')


# UI Part
# window
window = Tk()
window.title("Stock Trading News Alert")
window.config(padx=20, pady=20, bg=COLOR)

canvas = Canvas(width=300, height=50, bg=COLOR)
text = canvas.create_text(150, 30, width=280, text="Type the stock you want to subscribe.",
                          font=('Arial', 16, 'italic'))
canvas.grid(column=0, row=1, columnspan=2, pady=20)

# Labels
stock_name = Label(text="Stock Name: ", bg=COLOR)
stock_name.grid(column=0, row=2)

company_name = Label(text="Company Name: ", bg=COLOR)
company_name.grid(column=0, row=3)

former_name = Label(text="Stock Sent: None", bg=COLOR, font=('Arial', 10, 'normal'))
former_name.grid(column=1, row=0)

# Entries
stock_input = Entry(width=20, highlightbackground=COLOR, background=COLOR)
stock_input.insert(END, string="")
stock_input.grid(column=1, row=2)

company_input = Entry(width=20, highlightbackground=COLOR, background=COLOR)
company_input.insert(END, string="")
company_input.grid(column=1, row=3)

# Send button
button = Button(width=18, text='Send', highlightbackground=COLOR, command=if_clicked)
button.grid(column=1, row=4)

# message label
check_label = Label(text="", bg=COLOR)
check_label.grid(column=0, row=4)

window.mainloop()
