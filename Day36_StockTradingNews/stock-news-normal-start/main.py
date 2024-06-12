import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_APIKEY = ...
NEWS_API = ...

account_sid = ...
account_token = ...
#Step1

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_APIKEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

testing = data["Time Series (Daily)"]
new_data = [value for (key, value) in testing.items()]

yesterday_price = new_data[0]["4. close"]
before_yesterday_price = new_data[1]["4. close"]

difference = round(float(yesterday_price) - float(before_yesterday_price))
up_down = None
if difference > 0:
    up_down = "🔻"
else:
    up_down = "🟩"

percent = round(difference / float(yesterday_price) * 100)

if abs(percent) > 0:

    parameters2 = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
    }

    news = []

    response2 = requests.get(url=NEWS_ENDPOINT, params=parameters2)
    response2.raise_for_status()
    data2 = response2.json()['articles']
    three_articles = data2[:3]

    formatted_articles = [f"{STOCK_NAME}:{up_down}{percent}%\nHeadline: {article['title']}." for article in three_articles]

    client = Client(account_sid, account_token)

    message = client.messages \
        .create(
        body=formatted_articles[1],
        from_='+13854062084',
        to='+79778326425'
    )
    print(message.status)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.


#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

