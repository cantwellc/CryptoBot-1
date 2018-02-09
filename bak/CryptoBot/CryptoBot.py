import json
import datetime
import time
import tkinter
import discord

from binance.client import Client

binance_client = Client("","")
discord_client = discord.Client()

tickers = binance_client.get_all_tickers()
btc_tickers = [t for t in tickers if "BTC" in t['symbol']]

# Kline return data format
#[
#1499040000000, # Open time
#"0.01634790", # Open
#"0.80000000", # High
#"0.01575800", # Low
#"0.01577100", # Close
#"148976.11427815", # Volume
#1499644799999, # Close time
#"2434.19055334", # Quote asset volume
#308, # Number of trades
#"1756.87402397", # Taker buy base asset volume
#"28.46694368", # Taker buy quote asset volume
#"17928899.62484339" # Can be ignored
#]

interval_t = Client.KLINE_INTERVAL_5MINUTE
limit_t = 12
min_volume_t = 300
output = []

while True:
    new_output_t = []
    for ticker in btc_tickers:
        symbol_t = ticker['symbol']
        klines_t = binance_client.get_klines(symbol=symbol_t,interval=interval_t,limit=limit_t)
        price_high_t = float(klines_t[0][2])
        price_low_t = float(klines_t[0][3])
        volume_first_half_t = float(0.0)
        volume_second_half_t = float(0.0)
        idx = 0
        total_volume_t = float(0.0)

        # accumulate data for all klines returned
        for kline_t in klines_t:
            kline_high_t = float(kline_t[2])
            if kline_high_t > price_high_t:
                price_high_t = kline_high_t

            kline_low_t = float(kline_t[3])
            if kline_low_t < price_low_t:
                price_low_t = kline_low_t

            volume_t = float(kline_t[5])
            total_volume_t += volume_t

            if idx < limit_t / 2:
                volume_first_half_t += volume_t
            else:
                volume_second_half_t += volume_t

            idx += 1

        # calculate relevant data from accumulated statistics

        diff_t = price_high_t - price_low_t
        percent_change_t = diff_t / price_low_t
    
        avg_volume_t = total_volume_t / limit_t

        percent_volume_change_t = (volume_second_half_t - volume_first_half_t) / volume_first_half_t

        if(avg_volume_t >= min_volume_t and percent_change_t > 0.05):
            
            new_output_t.append([symbol_t,percent_change_t,percent_volume_change_t,avg_volume_t])

    #find new output that isn't already in the output list
    print_output_t = [t for t in new_output_t if t[0] not in output]
    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    
    for t in print_output_t:
        print('{}    {: <10} Price Change: {: <10.2%} Average Volume: {: <10.0f}'.format(ts,t[0],t[1],t[3]))

    output = [t[0] for t in new_output_t]

    # time.sleep(60)