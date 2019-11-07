from tkinter import *
import tkinter as tk
import time
import threading
from PIL import Image, ImageTk
from PIL import ImageTk,Image
import request_http_multiThread3_WORKING_COMPACT
from request_http_multiThread3_WORKING_COMPACT import *

root = None
rootTroca = None

abev3 = itub4 = mglu3 = petr4 = "sem id"

class Program():
    def __init__(self,master):
        self.root = root.geometry("1280x720"), root.resizable(width=False, height=False)
        self.screen()

    def screen(self):
        global abev3,itub4,mglu3,petr4
        # frame 0 = top-left
        # frame 1 = top-right
        # frame 2 = botton-left
        # frame 3 = botton-right

        root.configure(background="white")
        self.atualizaGraficoABEV3(abev3)
        self.atualizaGraficoPETR4(itub4)
        self.atualizaGraficoITUB4(mglu3)
        self.atualizaGraficoMGLU3(petr4)
        # load1 = Image.open("images/ABEV3.png")
        # load2 = Image.open("images/ITUB4.png")
        # load3 = Image.open("images/MGLU3.png")
        # load4 = Image.open("images/PETR4.png")
        #
        # render = ImageTk.PhotoImage(load1)
        # graph1 = Label(root, image=render)
        # graph1.image = render
        # graph1.place(x=39, y=-25)
        #
        # # load2 = Image.open("images/ITUB4.png")
        # render = ImageTk.PhotoImage(load2)
        # graph1 = Label(root, image=render)
        # graph1.image = render
        # graph1.place(x=639, y=-25)
        #
        # # load3 = Image.open("images/MGLU3.png")
        # render = ImageTk.PhotoImage(load3)
        # graph1 = Label(root, image=render)
        # graph1.image = render
        # graph1.place(x=39, y=261)
        #
        # # load4 = Image.open("images/PETR4.png")
        # render = ImageTk.PhotoImage(load4)
        # graph1 = Label(root, image=render)
        # graph1.image = render
        # graph1.place(x=639, y=261)

            # time.sleep(15)

        metrABEV3 = tk.IntVar()
        metrMGLU3 = tk.IntVar()
        metrITUB4 = tk.IntVar()
        metrPETR4 = tk.IntVar()


        stocks = [("Médias Móveis", 1), ("Volume", 2), ("Banda de Bollinger", 3), ("Fechamento", 4), ("Sem indicador", 5)]
        # self.photo = PhotoImage(file="images/ITUB4.png")
        # self.backlabel = Label(root, image=self.photo).place(x=-1, y=-1)
        # self.photo = PhotoImage(file="images/c0books_read.jpeg")
        # self.backlabel = Label(self.frame0, image=self.photo).place(x=-1, y=-1)

        # metricas ABEV3
        tk.Radiobutton(root, text="Médias Móveis             ", padx=0, variable=metrABEV3, value=1, bg="white").place(x=39, y=596)
        tk.Radiobutton(root, text="Volume                         ", padx=0, variable=metrABEV3, value=2, bg="white").place(x=39, y=618)
        tk.Radiobutton(root, text="Banda de Bollinger       ", padx=0, variable=metrABEV3, value=3, bg="white").place(x=39, y=640)
        tk.Radiobutton(root, text="Fechamento                  ", padx=0, variable=metrABEV3, value=4, bg="white").place(x=39, y=662)
        tk.Radiobutton(root, text="Sem indicador               ", padx=0, variable=metrABEV3, value=5,bg="white").place(x=39, y=684)

        # metricas MGLU3
        tk.Radiobutton(root, text="Médias Móveis             ", padx=0, variable=metrMGLU3, value=1, bg="white").place(x=250, y=596)
        tk.Radiobutton(root, text="Volume                         ", padx=0, variable=metrMGLU3, value=2, bg="white").place(x=250, y=618)
        tk.Radiobutton(root, text="Banda de Bollinger       ", padx=0, variable=metrMGLU3, value=3, bg="white").place(x=250, y=640)
        tk.Radiobutton(root, text="Fechamento                  ", padx=0, variable=metrMGLU3, value=4, bg="white").place(x=250, y=662)
        tk.Radiobutton(root, text="Sem indicador               ", padx=0, variable=metrMGLU3, value=5,bg="white").place(x=250, y=684)

        # metricas PETR4
        tk.Radiobutton(root, text="Médias Móveis             ", padx=0, variable=metrPETR4, value=1, bg="white").place(x=461,y=596)
        tk.Radiobutton(root, text="Volume                         ", padx=0, variable=metrPETR4, value=2, bg="white").place(x=461, y=618)
        tk.Radiobutton(root, text="Banda de Bollinger       ", padx=0, variable=metrPETR4, value=3, bg="white").place(x=461,y=640)
        tk.Radiobutton(root, text="Fechamento                  ", padx=0, variable=metrPETR4, value=4, bg="white").place(x=461,y=662)
        tk.Radiobutton(root, text="Sem indicador               ", padx=0, variable=metrPETR4, value=5,bg="white").place(x=461, y=684)

        # metricas ITUB4
        tk.Radiobutton(root, text="Médias Móveis             ", padx=0, variable=metrITUB4, value=1, bg="white").place(x=672,y=596)
        tk.Radiobutton(root, text="Volume                         ", padx=0, variable=metrITUB4, value=2, bg="white").place(x=672, y=618)
        tk.Radiobutton(root, text="Banda de Bollinger       ", padx=0, variable=metrITUB4, value=3, bg="white").place(x=672,y=640)
        tk.Radiobutton(root, text="Fechamento                  ", padx=0, variable=metrITUB4, value=4, bg="white").place(x=672,y=662)
        tk.Radiobutton(root, text="Sem indicador               ", padx=0,variable=metrITUB4, value=5,bg="white").place(x=672, y=684)

        buyABEV = tk.Button(root, text="COMPRAR ABEV3", width=15, height=0).place(x=870, y=566)
        sellABEV = tk.Button(root, text="VENDER ABEV3", width=15, height=0).place(x=870, y=600)

        buyMGLU = tk.Button(root, text="COMPRAR MGLU3", width=15, height=0).place(x=870, y=650)
        sellMGLU = tk.Button(root, text="VENDER MGLU3", width=15, height=0).place(x=870, y=684)

        buyPETR4 = tk.Button(root, text="COMPRAR PETR4", width=15, height=0).place(x=1050, y=566)
        sellPETR4 = tk.Button(root, text="VENDER PETR4", width=15, height=0).place(x=1050, y=600)

        buyITUB4 = tk.Button(root, text="COMPRAR ITUB4", width=15, height=0).place(x=1050, y=650)
        sellITUB4 = tk.Button(root, text="VENDER ITUB4", width=15, height=0).place(x=1050, y=684)


    def atualizaGraficoABEV3(self,metrica):
        global abev3
        if metrica == "sem id":
            abev3 = "sem id"
            load = Image.open("images/ABEV3.png")
        elif metrica == "boolinger":
            abev3 = "boolinger"
            load = Image.open("images/ABEV3.png")
        elif metrica == "volume":
            abev3 = "volume"
            load = Image.open("images/ABEV3.png")
        elif metrica == "fechamento":
            abev3 = "fechamento"
            load = Image.open("images/ABEV3.png")
        elif metrica == "media":
            abev3 = "media"
            load = Image.open("images/ABEV3.png")

        render = ImageTk.PhotoImage(load)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=39, y=-25)

    def atualizaGraficoITUB4(self, metrica):
        global itub4
        if metrica == "sem id":
            itub4 = "sem id"
            load2 = Image.open("images/ITUB4.png")
        elif metrica == "boolinger":
            itub4 = "boolinger"
            load2 = Image.open("images/ITUB4.png")
        elif metrica == "volume":
            itub4 = "volume"
            load2 = Image.open("images/ITUB4.png")
        elif metrica == "fechamento":
            itub4 = "fechamento"
            load2 = Image.open("images/ITUB4.png")
        elif metrica == "media":
            itub4 = "media"
            load2 = Image.open("images/ITUB4.png")
        render = ImageTk.PhotoImage(load2)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=639, y=-25)

    def atualizaGraficoMGLU3(self, metrica):
        global mglu3
        if metrica == "sem id":
            mglu3 = "sem id"
            load3 = Image.open("images/MGLU3.png")
        elif metrica == "boolinger":
            mglu3 = "boolinger"
            load3 = Image.open("images/MGLU3.png")
        elif metrica == "volume":
            mglu3 = "volume"
            load3 = Image.open("images/MGLU3.png")
        elif metrica == "fechamento":
            mglu3 = "fechamento"
            load3 = Image.open("images/MGLU3.png")
        elif metrica == "media":
            mglu3 = "media"
            load3 = Image.open("images/MGLU3.png")
        render = ImageTk.PhotoImage(load3)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=39, y=261)

    def atualizaGraficoPETR4(self, metrica):
        global petr4
        if metrica == "sem id":
            petr4 = "sem id"
            load4 = Image.open("images/PETR4.png")
        elif metrica == "bb":
            petr4 = "boolinger"
            load4 = Image.open("images/PETR4.png")
        elif metrica == "volume":
            petr4 = "volume"
            load4 = Image.open("images/PETR4.png")
        elif metrica == "fechamento":
            petr4 = "fechamento"
            load4 = Image.open("images/PETR4.png")
        elif metrica == "media":
            petr4 = "media"
            load4 = Image.open("images/PETR4.png")
        render = ImageTk.PhotoImage(load4)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=639, y=261)

def iniciar():
    global root
    global rootTroca
    global ABEV3, MGLU3, PETR4, ITUB4

    time.sleep(10)

    root = tk.Tk()
    Program(root)
    rootTroca = Program(root)
    root.mainloop()


def atualizaOsTreco():
    global rootTroca
    global abev3, itub4, mglu3, petr4

    while True:
        if rootTroca != None:
            rootTroca.atualizaGraficoABEV3(abev3)
            rootTroca.atualizaGraficoMGLU3(mglu3)
            rootTroca.atualizaGraficoPETR4(petr4)
            rootTroca.atualizaGraficoITUB4(itub4)
            time.sleep(300)


thread1 = threading.Thread(target=iniciar)
thread1.start()

thread2 = threading.Thread(target=atualizaOsTreco)
thread2.start()

