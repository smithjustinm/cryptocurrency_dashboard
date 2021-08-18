from get_coin_data import get_day_coin_data

# Populate BTC prices in USD
get_day_coin_data("BTC")
print("Done getting price data for BTC. See btc_prices.csv for results")

# Populate ETH prices in USD
get_day_coin_data("ETH")
print("Done getting price data for ETH. See eth_prices.csv for results")

# Populate XRP prices in USD
get_day_coin_data("XRP")
print("Done getting price data for XRP. See xrp_prices.csv for results")

# Populate LTC Prices in USD
get_day_coin_data("LTC")
print("Done getting price data for LTC. See ltc_prices.csv for results")

# Populate DOGE prices in USD
get_day_coin_data("DOGE")
print("Done getting price data for DOGE. See doge_prices.csv for results")

# Populate ADA prices in USD
get_day_coin_data("ADA")
print("Done getting price data for ADA. See ada_prices.csv for results")

# Populate BTC prices in USD by minute
# get_min_coin_data("BTC", limit="1440")
# print("Done getting price data for BTC. See btc_minute_prices.csv for results")