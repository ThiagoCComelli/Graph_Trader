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

                # POR ALGUM KRL DE MOTIVOS ELE DA ERRO AQUI ALGUMAS VEZES, É ALEATORIO

                # START OF DANGER ZONE - WARNING
                timeSeries = data['Time Series (5min)']
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
                plt.savefig('images/' + krl + "_" + str(tot) + '_' + str(tot) + '.png')
                plt.show()

                tot += 1
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
            if ITUB4 == None:
                PETR4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=PETR4.SA&interval=5min&apikey=234234")
        if (ABEV3 != None) and (MGLU3 != None) and (PETR4 != None) and (ITUB4 != None):
            time.sleep(295)

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

