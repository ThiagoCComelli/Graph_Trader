import json
import requests
import matplotlib.pyplot as plt
import time
import threading
from datetime import datetime

tot = 0
r = None

def gerador():
    global tot
    global r
    if r != None:
        valor = []
        data = r.json()
        now = datetime.now()

        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        print("gerador =>           " + str(open))
        print("{} {} {}".format(now.hour,now.minute,now.second))


        for i in range(len(open)):
            valor.append(i)

        plt.plot(valor,open[::-1])
        plt.savefig('images/'+'c'+str(tot)+'books_read.jpeg')
        plt.show()

        tot += 1

def atualizaRequest():
    global r
    while True:
        r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ABEV3.SA&interval=5min&apikey=234234")
        data = r.json()
        now = datetime.now()

        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        print("atualizaRequest =>   " + str(open))
        print("{} {} {}".format(now.hour,now.minute,now.second))

        gerador()

        time.sleep(295)

# thread1 = threading.Thread(target=gerador)
# thread1.start()

thread2 = threading.Thread(target=atualizaRequest)
thread2.start()