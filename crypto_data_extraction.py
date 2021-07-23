import requests
import csv
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ.get("API_KEY")

# attach to end of URLstring
url_api_part = "&api_key=" + apikey


# URL to get a list of coins from cryptocompare API
URLcoinslist = "https://min-api.cryptocompare.com/data/all/coinlist"

# Get list of cryptos with their symbols
res1 = requests.get(URLcoinslist)
res1_json = res1.json()
data1 = res1_json["Data"]
symbol_array = []
cryptoDict = dict(data1)

# write to CSV
with open("coin_info.csv", mode="w") as test_file:
    test_file_writer = csv.writer(
        test_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
    )
    for coin in cryptoDict.values():
        coin_id = coin["Id"]
        name = coin["Name"]
        symbol = coin["Symbol"]
        symbol_array.append(symbol)
        coin_name = coin["CoinName"]
        full_name = coin["FullName"]
        description = coin["Description"]
        algorithm = coin["Algorithm"]
        proof_type = coin["ProofType"]
        entry = [symbol, coin_name, description, algorithm, proof_type]
        test_file_writer.writerow(entry)
print("Done getting crypto names and symbols. See coin_info.csv for result")

# Populate BTC prices in USD

URL = (
    "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=500"
    + url_api_part
)
res = requests.get(URL)
res_json = res.json()
data = res_json["Data"]
# write required fields into csv
with open("btc_prices.csv", mode="a") as test_file:
    test_file_writer = csv.writer(
        test_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    for day in data:
        rawts = day["time"]
        ts = datetime.utcfromtimestamp(rawts).strftime("%Y-%m-%d %H:%M:%S")
        o = day["open"]
        h = day["high"]
        l = day["low"]
        c = day["close"]
        vfrom = day["volumefrom"]
        vto = day["volumeto"]
        symbol = "BTC"
        entry = [ts, o, h, l, c, vfrom, vto, symbol]
        test_file_writer.writerow(entry)
print("Done getting price data for btc. See btc_prices.csv for result")

# Populate ETH prices in USD

URL = (
    "https://min-api.cryptocompare.com/data/histoday?fsym=ETH&tsym=USD&limit=500"
    + url_api_part
)
res = requests.get(URL)
res_json = res.json()
data = res_json["Data"]
# write required fields into csv
with open("eth_prices.csv", mode="a") as test_file:
    test_file_writer = csv.writer(
        test_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    for day in data:
        rawts = day["time"]
        ts = datetime.utcfromtimestamp(rawts).strftime("%Y-%m-%d %H:%M:%S")
        o = day["open"]
        h = day["high"]
        l = day["low"]
        c = day["close"]
        vfrom = day["volumefrom"]
        vto = day["volumeto"]
        symbol = "ETH"
        entry = [ts, o, h, l, c, vfrom, vto, symbol]
        test_file_writer.writerow(entry)
print("Done getting price data for eth. See eth_prices.csv for result")

# Populate LTC prices in USD

URL = (
    "https://min-api.cryptocompare.com/data/histoday?fsym=LTC&tsym=USD&limit=500"
    + url_api_part
)
res = requests.get(URL)
res_json = res.json()
data = res_json["Data"]
# write required fields into csv
with open("ltc_prices.csv", mode="a") as test_file:
    test_file_writer = csv.writer(
        test_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    for day in data:
        rawts = day["time"]
        ts = datetime.utcfromtimestamp(rawts).strftime("%Y-%m-%d %H:%M:%S")
        o = day["open"]
        h = day["high"]
        l = day["low"]
        c = day["close"]
        vfrom = day["volumefrom"]
        vto = day["volumeto"]
        symbol = "LTC"
        entry = [ts, o, h, l, c, vfrom, vto, symbol]
        test_file_writer.writerow(entry)
print("Done getting price data for ltc. See ltc_prices.csv for result")

# Populate DOGE prices in USD

progress4 = 0
# get data for DOGE price in USD
URL = (
    "https://min-api.cryptocompare.com/data/histoday?fsym=DOGE&tsym=USD&limit=500"
    + url_api_part
)
res = requests.get(URL)
res_json = res.json()
data = res_json["Data"]
# write required fields into csv
with open("doge_prices.csv", mode="a") as test_file:
    test_file_writer = csv.writer(
        test_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    for day in data:
        rawts = day["time"]
        ts = datetime.utcfromtimestamp(rawts).strftime("%Y-%m-%d %H:%M:%S")
        o = day["open"]
        h = day["high"]
        l = day["low"]
        c = day["close"]
        vfrom = day["volumefrom"]
        vto = day["volumeto"]
        symbol = "DOGE"
        entry = [ts, o, h, l, c, vfrom, vto, symbol]
        test_file_writer.writerow(entry)
print("Done getting price data for doge. See doge_prices.csv for result")

# Populate Cardano prices in USD

URL = (
    "https://min-api.cryptocompare.com/data/histoday?fsym=ADA&tsym=USD&limit=500"
    + url_api_part
)
res = requests.get(URL)
res_json = res.json()
data = res_json["Data"]
# write required fields into csv
with open("ada_prices.csv", mode="a") as test_file:
    test_file_writer = csv.writer(
        test_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    for day in data:
        rawts = day["time"]
        ts = datetime.utcfromtimestamp(rawts).strftime("%Y-%m-%d %H:%M:%S")
        o = day["open"]
        h = day["high"]
        l = day["low"]
        c = day["close"]
        vfrom = day["volumefrom"]
        vto = day["volumeto"]
        symbol = "ADA"
        entry = [ts, o, h, l, c, vfrom, vto, symbol]
        test_file_writer.writerow(entry)
print("Done getting price data for ada. See ada_prices.csv for result")

# Populate XRP prices in USD

URL = (
    "https://min-api.cryptocompare.com/data/histoday?fsym=XRP&tsym=USD&limit=500"
    + url_api_part
)
res = requests.get(URL)
res_json = res.json()
data = res_json["Data"]
# write required fields into csv
with open("xrp_prices.csv", mode="a") as test_file:
    test_file_writer = csv.writer(
        test_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    for day in data:
        rawts = day["time"]
        ts = datetime.utcfromtimestamp(rawts).strftime("%Y-%m-%d %H:%M:%S")
        o = day["open"]
        h = day["high"]
        l = day["low"]
        c = day["close"]
        vfrom = day["volumefrom"]
        vto = day["volumeto"]
        symbol = "XRP"
        entry = [ts, o, h, l, c, vfrom, vto, symbol]
        test_file_writer.writerow(entry)
print("Done getting price data for xrp. See xrp_prices.csv for result")
