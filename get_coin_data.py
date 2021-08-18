import requests
import csv
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ.get("API_KEY")

# attach to end of URLstring
url_api_part = "&api_key=" + apikey

# header for all csv files
header = ["time", "symbol", "open", "high", "low", "close", "volume_from", "volume_to"]


def get_day_coin_data(fsym, tsym="USD", limit="365"):
    """Returns CSV of daily crypto coin OHLC data with volume.

    ...

    Attributes
    ----------
    fsym: str
        Coin's trading symbol
    tsym: str
        Fiat currency, default USD
    limit: str
        Number of data points to return, default 365
    """

    URL = (
        "https://min-api.cryptocompare.com/data/v2/histoday?"
        + "fsym="
        + fsym
        + "&tsym="
        + tsym
        + "&limit="
        + limit
        + url_api_part
    )
    res = requests.get(URL)
    res_json = res.json()
    data = res_json["Data"]["Data"]
    # write required fields into csv
    with open(fsym.lower() + "_day_prices.csv", mode="a") as f:
        file_writer = csv.writer(
            f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        file_writer.writerow(header)  # write the header

        for day in data:
            rawts = day["time"]
            ts = datetime.utcfromtimestamp(rawts).strftime("%Y-%m-%d %H:%M:%S")
            o = day["open"]
            h = day["high"]
            l = day["low"]
            c = day["close"]
            vfrom = day["volumefrom"]
            vto = day["volumeto"]
            symbol = fsym
            entry = [ts, symbol, o, h, l, c, vfrom, vto]
            file_writer.writerow(entry)


def get_hour_coin_data(fsym, tsym="USD", limit="8760"):
    """Returns CSV of hourly crypto coin OHLC data with volume.

    ...

    Attributes
    ----------
    fsym: str
        Coin's trading symbol
    tsym: str
        Fiat currency, default USD
    limit: str
        Number of data points to return, default 8760 (1 year in hours)
    """

    URL = (
        "https://min-api.cryptocompare.com/data/v2/histohour?"
        + "fsym="
        + fsym
        + "&tsym="
        + tsym
        + "&limit="
        + limit
        + url_api_part
    )
    res = requests.get(URL)
    res_json = res.json()
    data = res_json["Data"]["Data"]
    # write required fields into csv
    with open(fsym.lower() + "_hour_prices.csv", mode="a") as f:
        file_writer = csv.writer(
            f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        file_writer.writerow(header)  # write the header

        for hour in data:
            rawts = hour["time"]
            ts = datetime.utcfromtimestamp(rawts).strftime("%Y-%m-%d %H:%M:%S")
            o = hour["open"]
            h = hour["high"]
            l = hour["low"]
            c = hour["close"]
            vfrom = hour["volumefrom"]
            vto = hour["volumeto"]
            symbol = fsym
            entry = [ts, symbol, o, h, l, c, vfrom, vto]
            file_writer.writerow(entry)


def get_min_coin_data(fsym, tsym="USD", limit="525600"):
    """Returns CSV of minute crypto coin OHLC data with volume.

    ...

    Attributes
    ----------
    fsym: str
        Coin's trading symbol
    tsym: str
        Fiat currency, default USD
    limit: str
        Number of data points to return, default 525600 (1 year in minutes)
    """

    URL = (
        "https://min-api.cryptocompare.com/data/v2/histominute?"
        + "fsym="
        + fsym
        + "&tsym="
        + tsym
        + "&limit="
        + limit
        + url_api_part
    )
    res = requests.get(URL)
    res_json = res.json()
    data = res_json["Data"]["Data"]

    # write required fields into csv
    with open(fsym.lower() + "_minute_prices.csv", mode="a") as f:
        file_writer = csv.writer(
            f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        file_writer.writerow(header)  # write the header

        for minutes in data:
            rawts = minutes["time"]
            ts = datetime.utcfromtimestamp(rawts).strftime("%Y-%m-%d %H:%M:%S")
            o = minutes["open"]
            h = minutes["high"]
            l = minutes["low"]
            c = minutes["close"]
            vfrom = minutes["volumefrom"]
            vto = minutes["volumeto"]
            symbol = fsym
            entry = [ts, symbol, o, h, l, c, vfrom, vto]
            file_writer.writerow(entry)
