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

def gerador():
    global tot
    global ABEV3
    global MGLU3
    global PETR4
    global ITUB4

    while True:
        if (ABEV3 != None) and (MGLU3 != None) and (PETR4 != None) and (ITUB4 != None):
            lista = [ABEV3,MGLU3,PETR4,ITUB4]
            break

    while True:
        for i in lista:
            valor = []
            data = i.json()
            now = datetime.now()

            # POR ALGUM KRL DE MOTIVOS ELE DA ERRO AQUI ALGUMAS VEZES, É ALEATORIO

            # START OF DANGER ZONE - WARNING
            timeSeries = data["Time Series (5min)"]
            # END OF DANGER ZONE - WARNING

            open = [float(dado["1. open"]) for dado in timeSeries.values()]

            for u in range(len(open)):
                valor.append(u)

            if lista.index(i) == 0:
                krl = "ABEV3"
            elif lista.index(i) == 1:
                krl = "MGLU3"
            elif lista.index(i) == 2:
                krl = "PETR4"
            else:
                krl = "ITUB4"

            print("gerador {} =>           ".format(krl) + str(open))



            plt.plot(valor, open[::-1])
            plt.savefig('images/' + krl + '.png')
            plt.show()

            tot += 1
        break

    time.sleep(300)

def abev3():
    global ABEV3

    while True:
        ABEV3 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ABEV3.SA&interval=5min&apikey=234234")

        # data = ABEV3.json()
        # now = datetime.now()
        #
        # timeSeries = data["Time Series (5min)"]
        # open = [float(dado["1. open"]) for dado in timeSeries.values()]

        # print("atualizaRequest =>   " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        time.sleep(295)

def mglu3():
    global MGLU3
    while True:
        MGLU3 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MGLU3.SA&interval=5min&apikey=234234")

        # data = MGLU3.json()
        # now = datetime.now()
        #
        # timeSeries = data["Time Series (5min)"]
        # open = [float(dado["1. open"]) for dado in timeSeries.values()]

        # print("atualizaRequest =>   " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        time.sleep(295)

def itub4():
    global ITUB4
    while True:
        ITUB4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ITUB4.SA&interval=5min&apikey=234234")
        #
        # data = ITUB4.json()
        # now = datetime.now()
        #
        # timeSeries = data["Time Series (5min)"]
        # open = [float(dado["1. open"]) for dado in timeSeries.values()]
        #
        # print("atualizaRequest =>   " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        time.sleep(295)

def petr4():
    global PETR4
    while True:
        PETR4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=PETR4.SA&interval=5min&apikey=234234")
        #
        # data = PETR4.json()
        # now = datetime.now()
        #
        # timeSeries = data["Time Series (5min)"]
        # open = [float(dado["1. open"]) for dado in timeSeries.values()]
        #
        # print("atualizaRequest =>   " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        time.sleep(295)

thread5 = threading.Thread(target=gerador)
thread5.start()

thread1 = threading.Thread(target=abev3)
thread1.start()

thread2 = threading.Thread(target=mglu3)
thread2.start()

thread3 = threading.Thread(target=petr4)
thread3.start()

thread4 = threading.Thread(target=itub4)
thread4.start()


