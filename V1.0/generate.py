import json
import requests
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import time
import threading
from datetime import datetime
from PIL import ImageTk,Image,ImageDraw, ImageFont

tot = 0
ABEV3 = MGLU3 = PETR4 = ITUB4 = None
ABEV3SMA = MGLU3SMA = PETR4SMA = ITUB4SMA = None
ABEV3SMAoque = MGLU3SMAoque = PETR4SMAoque = ITUB4SMAoque = "FAZ NADA"
ABEV3SMAclose = MGLU3SMAclose = PETR4SMAclose = ITUB4SMAclose = None
ABEV3SMAultimo = MGLU3SMAultimo = PETR4SMAultimo = ITUB4SMAultimo = None

def gerador():
    while True:
        global tot, ABEV3, MGLU3, PETR4, ITUB4
        global ABEV3SMA, MGLU3SMA, PETR4SMA, ITUB4SMA
        global ABEV3SMAclose, MGLU3SMAclose, PETR4SMAclose, ITUB4SMAclose
        global ABEV3SMAultimo, MGLU3SMAultimo, PETR4SMAultimo, ITUB4SMAultimo
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
                nomeDeArquivo = data['Meta data']
                nomeDeArquivo1 = nomeDeArquivo['3. Last Refreshed']

                open = [float(dado["1. open"]) for dado in timeSeries.values()]
                high = [float(dado["2. high"]) for dado in timeSeries.values()]
                close = [float(dado["4. close"]) for dado in timeSeries.values()]
                volume = [float(dado["5. volume"]) for dado in timeSeries.values()]

                for u in range(len(open)):
                    valor.append(u)

                if lista.index(i) == 0:
                    stock = "ABEV3"
                    ABEV3SMAclose = close[0]
                elif lista.index(i) == 1:
                    stock = "MGLU3"
                    MGLU3SMAclose = close[0]
                elif lista.index(i) == 2:
                    stock = "PETR4"
                    PETR4SMAclose = close[0]
                elif lista.index(i) == 3:
                    stock = "ITUB4"
                    ITUB4SMAclose = close[0]

                plt.figure(num=None, figsize=(6, 2.6), dpi=100, facecolor='w', edgecolor='white')

                plt.plot(valor, open[::-1])
                plt.savefig('images/{}/'.format(stock) + stock + "open" + '.png')
                plt.clf()
                plt.plot(valor, high[::-1])
                plt.savefig('images/{}/'.format(stock) + stock + "high" + '.png')
                plt.clf()
                plt.plot(valor, close[::-1])
                plt.savefig('images/{}/'.format(stock) + stock + "close" + '.png')
                plt.clf()
                plt.bar(valor, volume[::-1])
                plt.savefig('images/{}/'.format(stock) + stock + "volume" + '.png')
                plt.clf()
                plt.plot(valor, open[::-1])
                plt.plot(valor, high[::-1])
                plt.plot(valor, close[::-1])
                plt.savefig('images/{}/'.format(stock) + stock + "semid" + '.png')
                plt.clf()
                plt.close()

                geradorText(data, nomeDeArquivo1, stock)
            break
        ABEV3 = MGLU3 = PETR4 = ITUB4 = None

def atualiza(stonks):
    global ABEV3, MGLU3, PETR4, ITUB4
    global ABEV3SMA, MGLU3SMA, PETR4SMA, ITUB4SMA


    if stonks == "ABEV3" or stonks == "MGLU3" or stonks == "ITUB4" or stonks == "PETR4":
        while True:
            if stonks == "ABEV3":
                if ABEV3 == None:
                    ABEV3 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ABEV3.SA&interval=5min&apikey=YCIKY149UTT1SRPOA")
            elif stonks == "MGLU3":
                if MGLU3 == None:
                    MGLU3 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MGLU3.SA&interval=5min&apikey=YCIKY193UTT1SRPOA")
            elif stonks == "ITUB4":
                if ITUB4 == None:
                    ITUB4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ITUB4.SA&interval=5min&apikey=YCIKY159UTT1SRPOA")
            elif stonks == "PETR4":
                if PETR4 == None:
                    PETR4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=PETR4.SA&interval=5min&apikey=YCIKY169UTT1SRPOA")
            if (ABEV3 != None) and (MGLU3 != None) and (PETR4 != None) and (ITUB4 != None):
                print("SUCCESS")
                time.sleep(295)
    else:
        time.sleep(70)
        while True:
            if stonks == "ABEV3SMA":
                if ABEV3SMA == None:
                    ABEV3SMA = requests.get("https://www.alphavantage.co/query?function=SMA&symbol=ABEV3.SA&interval=5min&time_period=10&series_type=open&apikey=7893846")
            elif stonks == "MGLU3SMA":
                if MGLU3SMA == None:
                    MGLU3SMA = requests.get("https://www.alphavantage.co/query?function=SMA&symbol=MGLU3.SA&interval=5min&time_period=10&series_type=open&apikey=7849846")
            elif stonks == "ITUB4SMA":
                if ITUB4SMA == None:
                    ITUB4SMA = requests.get("https://www.alphavantage.co/query?function=SMA&symbol=ITUB4.SA&interval=5min&time_period=10&series_type=open&apikey=7895846")
            elif stonks == "PETR4SMA":
                if PETR4SMA == None:
                    PETR4SMA = requests.get("https://www.alphavantage.co/query?function=SMA&symbol=PETR4.SA&interval=5min&time_period=10&series_type=open&apikey=7896846")
            if (ABEV3SMA != None) and (MGLU3SMA != None) and (PETR4SMA != None) and (ITUB4SMA != None):
                print("SUCCESS SMA")
                geradorSMA()
                time.sleep(295)

def geradorSMA():
    global tot, ABEV3, MGLU3, PETR4, ITUB4
    global ABEV3SMA, MGLU3SMA, PETR4SMA, ITUB4SMA
    global ABEV3SMAoque, MGLU3SMAoque, PETR4SMAoque, ITUB4SMAoque
    global ABEV3SMAclose, MGLU3SMAclose, PETR4SMAclose, ITUB4SMAclose
    global ABEV3SMAultimo, MGLU3SMAultimo, PETR4SMAultimo, ITUB4SMAultimo

    lista = [ABEV3SMA, MGLU3SMA, PETR4SMA, ITUB4SMA]

    for i in lista:
        valor = []
        data = i.json()
        now = datetime.now()

        timeSeries = data['Technical Analysis: SMA']

        sma = [float(dado["SMA"]) for dado in timeSeries.values()]

        if lista.index(i) == 0:
            ABEV3SMAultimo = sma[0]
        elif lista.index(i) == 1:
            MGLU3SMAultimo = sma[0]
        elif lista.index(i) == 2:
            PETR4SMAultimo = sma[0]
        else:
            ITUB4SMAultimo = sma[0]

    if ABEV3SMAclose > ABEV3SMAultimo:
        ABEV3SMAoque = "VENDE"
    elif ABEV3SMAclose < ABEV3SMAultimo:
        ABEV3SMAoque = "COMPRA"

    if MGLU3SMAclose > MGLU3SMAultimo:
        MGLU3SMAoque = "VENDE"
    elif MGLU3SMAclose < MGLU3SMAultimo:
        MGLU3SMAoque = "COMPRA"

    if PETR4SMAclose > PETR4SMAultimo:
        PETR4SMAoque = "VENDE"
    elif PETR4SMAclose < PETR4SMAultimo:
        PETR4SMAoque = "COMPRA"

    if ITUB4SMAclose > ITUB4SMAultimo:
        ITUB4SMAoque = "VENDE"
    elif ITUB4SMAclose < ITUB4SMAultimo:
        ITUB4SMAoque = "COMPRA"

    geradorAcao()

def geradorText(text,name,acao):
    a = str(name[:10]) + "_" + str(name[11:])
    a = a.replace(":", "-")
    arq = open("data/{}data/{}_".format(acao,acao) + a + ".txt", "w+")
    arq.write(str(text))
    arq.close()

def geradorAcao():
    global tot, ABEV3, MGLU3, PETR4, ITUB4
    global ABEV3SMA, MGLU3SMA, PETR4SMA, ITUB4SMA
    global ABEV3SMAoque, MGLU3SMAoque, PETR4SMAoque, ITUB4SMAoque
    global ABEV3SMAclose, MGLU3SMAclose, PETR4SMAclose, ITUB4SMAclose
    global ABEV3SMAultimo, MGLU3SMAultimo, PETR4SMAultimo, ITUB4SMAultimo

    img = Image.new('RGB', (215, 90), color=(255, 255, 255))
    fnt = ImageFont.truetype('times.ttf',20)
    d = ImageDraw.Draw(img)
    d.text((5, 0), "ABEV3.SA:  {}\nMGLU3.SA: {}\nPETR4.SA:   {}\nITUB4.SA:   {}".format(ABEV3SMAoque,MGLU3SMAoque,PETR4SMAoque,ITUB4SMAoque),font=fnt, fill=(0, 0, 0))

    img.save('images/_OqueFazer/oquefazerIMG.png')

thread1 = threading.Thread(target=atualiza,args=("ABEV3",))
thread1.start()

thread2 = threading.Thread(target=atualiza,args=("MGLU3",))
thread2.start()

thread3 = threading.Thread(target=atualiza,args=("ITUB4",))
thread3.start()

thread4 = threading.Thread(target=atualiza,args=("PETR4",))
thread4.start()


thread6 = threading.Thread(target=atualiza,args=("ABEV3SMA",))
thread6.start()

thread7 = threading.Thread(target=atualiza,args=("MGLU3SMA",))
thread7.start()

thread8 = threading.Thread(target=atualiza,args=("ITUB4SMA",))
thread8.start()

thread9 = threading.Thread(target=atualiza,args=("PETR4SMA",))
thread9.start()


thread5 = threading.Thread(target=gerador)
thread5.start()
