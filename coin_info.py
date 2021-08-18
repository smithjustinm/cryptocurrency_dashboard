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
