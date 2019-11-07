import json
import requests
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import time
import threading
from datetime import datetime

tot = 0
ABEV3 = None
MGLU3 = None
PETR4 = None
ITUB4 = None

def gerador(stocks):
    global tot
    global ABEV3
    global MGLU3
    global PETR4
    global ITUB4

    if stocks == "ABEV3":
        r = ABEV3
    elif stocks == "MGLU3":
        r = MGLU3
    elif stocks == "PETR4":
        r = PETR4
    elif stocks == "ITUB4":
        r = ITUB4

    print(stocks)
    if r != None:
        valor = []
        data = r.json()
        now = datetime.now()
        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        # print("gerador =>           " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        for i in range(len(open)):
            valor.append(i)


        plt.plot(valor, open[::-1])
        plt.savefig('images/' + stocks + str(tot) + '.png')
        plt.show()

        tot += 1

def abev3():
    global ABEV3
    while True:
        ABEV3 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ABEV3.SA&interval=5min&apikey=234234")

        data = ABEV3.json()
        now = datetime.now()

        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        print("atualizaRequest =>   " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        gerador("ABEV3")

        time.sleep(295)

def mglu3():
    global MGLU3
    while True:
        MGLU3 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MGLU3.SA&interval=5min&apikey=234234")

        data = MGLU3.json()
        now = datetime.now()

        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        print("atualizaRequest =>   " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        gerador("MGLU3")

        time.sleep(295)

def itub4():
    global ITUB4
    while True:
        ITUB4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ITUB4.SA&interval=5min&apikey=234234")

        data = ITUB4.json()
        now = datetime.now()

        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        print("atualizaRequest =>   " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        gerador("ITUB4")

        time.sleep(295)

def petr4():
    global PETR4
    while True:
        PETR4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=PETR4.SA&interval=5min&apikey=234234")

        data = PETR4.json()
        now = datetime.now()

        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        print("atualizaRequest =>   " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        gerador("PETR4")

        time.sleep(295)


thread1 = threading.Thread(target=abev3)
thread1.start()

thread2 = threading.Thread(target=mglu3)
thread2.start()

thread3 = threading.Thread(target=petr4)
thread3.start()

thread4 = threading.Thread(target=itub4)
thread4.start()