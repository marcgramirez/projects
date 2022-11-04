import requests
from twilio.rest import Client

STOCK_NAME = "SQ"
COMPANY_NAME = "Block Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "A81I8TDJ0V3H4W8V"
NEWS_API_KEY = "1a434fc5dc664c679ef02199f6aeacaf"
TWILIO_SID = "AC52938ca4e0f1573de2a37ee8101f5933"
TWILIO_AUTH_TOKEN = "78d7818e09185ab8f7a8c71b35d1c85a"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY

}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing = yesterday_data["4. close"]
print(yesterday_closing)

day_before_yesterday = data_list[1]
day_before_yesterday_closing = day_before_yesterday["4. close"]
print(day_before_yesterday_closing)

difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

diff_percent = round((difference / float(yesterday_closing)) * 100)
print(diff_percent)

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = (news_response.json()["articles"])
    print(articles)

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nheadline: {article ['title']}. \nBrief: {article['description']}" for article in three_articles]


    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+14692422196",
            to="3239797585"
        )
