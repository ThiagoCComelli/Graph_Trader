import json
import requests
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import time
import threading
from datetime import datetime

tot = 0

escolhido = None
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
    global escolhido

    if stocks == "ABEV3":
        a = ABEV3
    elif stocks == "MGLU3":
        m = MGLU3
    elif stocks == "PETR4":
        p = PETR4
    elif stocks == "ITUB4":
        i = ITUB4

    def socorro(pelamor):
        global escolhido

        if pelamor == "ABEV3":
            while escolhido == None:
                escolhido = a
            return a
        elif pelamor == "MGLU3":
            while escolhido == None:
                escolhido = m
            return m
        elif pelamor == "PETR4":
            while escolhido == None:
                escolhido = p
            return p
        elif pelamor == "ITUB4":
            while escolhido == None:
                escolhido = i
            return i

    if socorro(stocks) != None:
        valor = []
        data = escolhido.json()
        now = datetime.now()
        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        # print("gerador =>           " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        plt.plot(valor, open[::-1])
        plt.savefig('images/' + stocks + '.png')
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