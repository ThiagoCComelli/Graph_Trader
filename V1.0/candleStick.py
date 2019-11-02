import json
import requests
import matplotlib.pyplot as plt
import time
import threading
from mpl_finance import candlestick_ohlc

tot = 0
r = None

def atualizaRequest():
    global r
    while True:
        r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ABEV3.SA&interval=5min&apikey=234234")
        data = r.json()
        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]
        high = [float(dado["2. high"]) for dado in timeSeries.values()]
        low = [float(dado["3. low"]) for dado in timeSeries.values()]
        close = [float(dado["4. close"]) for dado in timeSeries.values()]
        print(timeSeries)

        df = [open, high, low, close]


        ax = plt.subplot()
        candlestick_ohlc(ax, df.values, width=5, colorup='g', colordown='r')
        ax.xaxis_date()
        ax.grid(True)
        plt.show()

# thread1 = threading.Thread(target=gerador)
# thread1.start()

thread2 = threading.Thread(target=atualizaRequest)
thread2.start()
