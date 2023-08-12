import urequests
import json

def get_btc_price():
    response = urequests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
    data = response.json()
    currency = data["data"]["base"]
    price = data["data"]["amount"]
    return price
