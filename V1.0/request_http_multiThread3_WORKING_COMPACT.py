import json
import requests
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import time
import threading
from datetime import datetime

tot = 0
ABEV3 = MGLU3 = PETR4 = ITUB4 = None

def gerador():
    while True:
        global tot, ABEV3, MGLU3, PETR4, ITUB4
        lista = []

        while True:
            if (ABEV3 != None) and (MGLU3 != None) and (PETR4 != None) and (ITUB4 != None):
                lista = [ABEV3,MGLU3,PETR4,ITUB4]
                break

        while True:
            for i in lista:
                valor = []
                data = i.json()
                now = datetime.now()

                timeSeries = data['Time Series (5min)']

                open = [float(dado["1. open"]) for dado in timeSeries.values()]
                high = [float(dado["2. high"]) for dado in timeSeries.values()]
                close = [float(dado["4. close"]) for dado in timeSeries.values()]
                volume = [float(dado["5. volume"]) for dado in timeSeries.values()]

                for u in range(len(open)):
                    valor.append(u)

                plt.figure(num=None, figsize=(6, 2.6), dpi=100, facecolor='w', edgecolor='white')

                if lista.index(i) == 0:
                    stock = "ABEV3"
                    plt.plot(valor, open[::-1])
                    plt.savefig('images/ABEV3/' + stock + "open" + '.png')
                    plt.clf()
                    plt.plot(valor, high[::-1])
                    plt.savefig('images/ABEV3/' + stock + "high" + '.png')
                    plt.clf()
                    plt.plot(valor, close[::-1])
                    plt.savefig('images/ABEV3/' + stock + "close" + '.png')
                    plt.clf()
                    plt.plot(valor, volume[::-1])
                    plt.savefig('images/ABEV3/' + stock + "volume" + '.png')
                    plt.clf()
                elif lista.index(i) == 1:
                    stock = "MGLU3"
                    plt.plot(valor, open[::-1])
                    plt.savefig('images/MGLU3/' + stock + "open" + '.png')
                    plt.clf()
                    plt.plot(valor, high[::-1])
                    plt.savefig('images/MGLU3/' + stock + "high" + '.png')
                    plt.clf()
                    plt.plot(valor, close[::-1])
                    plt.savefig('images/MGLU3/' + stock + "close" + '.png')
                    plt.clf()
                    plt.plot(valor, volume[::-1])
                    plt.savefig('images/MGLU3/' + stock + "volume" + '.png')
                    plt.clf()
                elif lista.index(i) == 2:
                    stock = "PETR4"
                    plt.plot(valor, open[::-1])
                    plt.savefig('images/PETR4/' + stock + "open" + '.png')
                    plt.clf()
                    plt.plot(valor, high[::-1])
                    plt.savefig('images/PETR4/' + stock + "high" + '.png')
                    plt.clf()
                    plt.plot(valor, close[::-1])
                    plt.savefig('images/PETR4/' + stock + "close" + '.png')
                    plt.clf()
                    plt.plot(valor, volume[::-1])
                    plt.savefig('images/PETR4/' + stock + "volume" + '.png')
                    plt.clf()
                else:
                    stock = "ITUB4"
                    plt.plot(valor, open[::-1])
                    plt.savefig('images/ITUB4/' + stock + "open" + '.png')
                    plt.clf()
                    plt.plot(valor, high[::-1])
                    plt.savefig('images/ITUB4/' + stock + "high" + '.png')
                    plt.clf()
                    plt.plot(valor, close[::-1])
                    plt.savefig('images/ITUB4/' + stock + "close" + '.png')
                    plt.clf()
                    plt.plot(valor, volume[::-1])
                    plt.savefig('images/ITUB4/' + stock + "volume" + '.png')
                    plt.clf()
                plt.close()
            break
        ABEV3 = MGLU3 = PETR4 = ITUB4 = None

def atualiza(stonks):
    global ABEV3, MGLU3, PETR4, ITUB4

    while True:
        if stonks == "ABEV3":
            if ABEV3 == None:
                ABEV3 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ABEV3.SA&interval=5min&apikey=234234")
        elif stonks == "MGLU3":
            if MGLU3 == None:
                MGLU3 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MGLU3.SA&interval=5min&apikey=234234")
        elif stonks == "ITUB4":
            if ITUB4 == None:
                ITUB4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ITUB4.SA&interval=5min&apikey=234234")
        elif stonks == "PETR4":
            if PETR4 == None:
                PETR4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=PETR4.SA&interval=5min&apikey=234234")
        if (ABEV3 != None) and (MGLU3 != None) and (PETR4 != None) and (ITUB4 != None):
            print("SUCCESS")
            time.sleep(295)

# def queroDormir():
#     global ABEV3T, MGLU3T, PETR4T, ITUB4T
#     global ABEV3, MGLU3, PETR4, ITUB4
#
#     while True:
#         print(ITUB4)
#         print(ITUB4T)
#         time.sleep(1)

thread1 = threading.Thread(target=atualiza,args=("ABEV3",))
thread1.start()

thread2 = threading.Thread(target=atualiza,args=("MGLU3",))
thread2.start()

thread3 = threading.Thread(target=atualiza,args=("ITUB4",))
thread3.start()

thread4 = threading.Thread(target=atualiza,args=("PETR4",))
thread4.start()

thread5 = threading.Thread(target=gerador)
thread5.start()

# thread6 = threading.Thread(target=queroDormir)
# thread6.start()

