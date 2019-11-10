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


# bollinger e medias moveis tem pronta no alpha vantage, coletar e fazer os graficos



class Program():
    def __init__(self,master):
        self.root = root.geometry("1280x720"), root.resizable(width=False, height=False)
        self.screen()

    def screen(self):
        global abev3,itub4,mglu3,petr4
        self.frame0 = tk.Frame(root, width=1280, height=720, bg='white')
        self.frame0.place(x=0, y=0)


        root.configure(background="white")
        self.atualizaGraficoABEV3(abev3)
        self.atualizaGraficoPETR4(itub4)
        self.atualizaGraficoITUB4(mglu3)
        self.atualizaGraficoMGLU3(petr4)


        metrABEV3 = tk.IntVar()
        metrMGLU3 = tk.IntVar()
        metrITUB4 = tk.IntVar()
        metrPETR4 = tk.IntVar()


        stocks = [("Médias Móveis", 1), ("Volume", 2), ("Banda de Bollinger", 3), ("Fechamento", 4), ("Sem indicador", 5)]

        # metricas ABEV3
        # tk.Radiobutton(root, text="Médias Móveis", padx=0,width=20, variable=metrABEV3,command=lambda: self.atualizaGraficoABEV3("sem id"),value=1, bg="white").place(x=39, y=596)
        tk.Radiobutton(root, text="Volume", padx=0,width=20, variable=metrABEV3,command=lambda: self.atualizaGraficoABEV3("volume"), value=2, bg="white").place(x=39, y=618)
        tk.Radiobutton(root, text="Abertura", padx=0,width=20, variable=metrABEV3,command=lambda: self.atualizaGraficoABEV3("abertura"), value=3, bg="white").place(x=39, y=640)
        tk.Radiobutton(root, text="Fechamento", padx=0,width=20, variable=metrABEV3,command=lambda: self.atualizaGraficoABEV3("fechamento"), value=4, bg="white").place(x=39, y=662)
        tk.Radiobutton(root, text="Metricas Juntas", padx=0,width=20, variable=metrABEV3,command=lambda: self.atualizaGraficoABEV3("sem id"), value=5,bg="white").place(x=39, y=684)

        # metricas MGLU3
        # tk.Radiobutton(root, text="Médias Móveis", padx=0,width=20, variable=metrMGLU3,command=lambda: self.atualizaGraficoMGLU3("sem id"), value=1, bg="white").place(x=250, y=596)
        tk.Radiobutton(root, text="Volume", padx=0,width=20, variable=metrMGLU3,command=lambda: self.atualizaGraficoMGLU3("volume"), value=2, bg="white").place(x=250, y=618)
        tk.Radiobutton(root, text="Abertura", padx=0,width=20, variable=metrMGLU3,command=lambda: self.atualizaGraficoMGLU3("abertura"), value=3, bg="white").place(x=250, y=640)
        tk.Radiobutton(root, text="Fechamento", padx=0,width=20, variable=metrMGLU3,command=lambda: self.atualizaGraficoMGLU3("fechamento"), value=4, bg="white").place(x=250, y=662)
        tk.Radiobutton(root, text="Metricas Juntas", padx=0,width=20, variable=metrMGLU3,command=lambda: self.atualizaGraficoMGLU3("sem id"), value=5,bg="white").place(x=250, y=684)

        # metricas PETR4
        # tk.Radiobutton(root, text="Médias Móveis", padx=0,width=20, variable=metrPETR4,command=lambda: self.atualizaGraficoPETR4("sem id"), value=1, bg="white").place(x=461,y=596)
        tk.Radiobutton(root, text="Volume", padx=0,width=20, variable=metrPETR4,command=lambda: self.atualizaGraficoPETR4("volume"), value=2, bg="white").place(x=461, y=618)
        tk.Radiobutton(root, text="Abertura", padx=0,width=20, variable=metrPETR4,command=lambda: self.atualizaGraficoPETR4("abertura"), value=3, bg="white").place(x=461,y=640)
        tk.Radiobutton(root, text="Fechamento", padx=0,width=20, variable=metrPETR4,command=lambda: self.atualizaGraficoPETR4("fechamento"), value=4, bg="white").place(x=461,y=662)
        tk.Radiobutton(root, text="Metricas Juntas", padx=0,width=20, variable=metrPETR4,command=lambda: self.atualizaGraficoPETR4("sem id"), value=5,bg="white").place(x=461, y=684)

        # metricas ITUB4
        # tk.Radiobutton(root, text="Médias Móveis", padx=0,width=20, variable=metrITUB4,command=lambda: self.atualizaGraficoITUB4("sem id"), value=1, bg="white").place(x=672,y=596)
        tk.Radiobutton(root, text="Volume", padx=0,width=20, variable=metrITUB4,command=lambda: self.atualizaGraficoITUB4("volume"), value=2, bg="white").place(x=672, y=618)
        tk.Radiobutton(root, text="Abertura", padx=0,width=20, variable=metrITUB4,command=lambda: self.atualizaGraficoITUB4("abertura"), value=3, bg="white").place(x=672,y=640)
        tk.Radiobutton(root, text="Fechamento", padx=0,width=20, variable=metrITUB4,command=lambda: self.atualizaGraficoITUB4("fechamento"), value=4, bg="white").place(x=672,y=662)
        tk.Radiobutton(root, text="Metricas Juntas", padx=0,width=20,variable=metrITUB4,command=lambda: self.atualizaGraficoITUB4("sem id"), value=5,bg="white").place(x=672, y=684)

        # buyABEV = tk.Button(root, text="COMPRAR ABEV3", width=15, height=0).place(x=870, y=566)
        # sellABEV = tk.Button(root, text="VENDER ABEV3", width=15, height=0).place(x=870, y=600)
        #
        # buyMGLU = tk.Button(root, text="COMPRAR MGLU3", width=15, height=0).place(x=870, y=650)
        # sellMGLU = tk.Button(root, text="VENDER MGLU3", width=15, height=0).place(x=870, y=684)
        #
        # buyPETR4 = tk.Button(root, text="COMPRAR PETR4", width=15, height=0).place(x=1050, y=566)
        # sellPETR4 = tk.Button(root, text="VENDER PETR4", width=15, height=0).place(x=1050, y=600)
        #
        # buyITUB4 = tk.Button(root, text="COMPRAR ITUB4", width=15, height=0).place(x=1050, y=650)
        # sellITUB4 = tk.Button(root, text="VENDER ITUB4", width=15, height=0).place(x=1050, y=684)

        # self.frame1 = tk.Frame(root, width=373, height=120, bg='light gray')
        # self.frame1.place(x=870, y=566)

        #marcacoes dos graficos
        self.labelABEV3 = tk.Label(root)
        self.labelABEV3.configure(text='ABEV3', font="Times 15 bold", fg="black", bg="white")
        self.labelABEV3.place(x=300, y=18)

        self.labelITUB4 = tk.Label(root)
        self.labelITUB4.configure(text='ITUB4', font="Times 15 bold", fg="black", bg="white")
        self.labelITUB4.place(x=910, y=18)

        self.labelMGLU3 = tk.Label(root)
        self.labelMGLU3.configure(text='MGLU3', font="Times 15 bold", fg="black", bg="white")
        self.labelMGLU3.place(x=300, y=280)

        self.labelPETR4 = tk.Label(root)
        self.labelPETR4.configure(text='PETR4', font="Times 15 bold", fg="black", bg="white")
        self.labelPETR4.place(x=910, y=280)

        #marcacoes das medias
        self.labelABEV3 = tk.Label(root)
        self.labelABEV3.configure(text='ABEV3:', font="Times 12 bold", fg="black", bg="white")
        self.labelABEV3.place(x=39, y=572)

        self.labelITUB4 = tk.Label(root)
        self.labelITUB4.configure(text='MGLU3:', font="Times 12 bold", fg="black", bg="white")
        self.labelITUB4.place(x=250, y=572)

        self.labelMGLU3 = tk.Label(root)
        self.labelMGLU3.configure(text='PETR4:', font="Times 12 bold", fg="black", bg="white")
        self.labelMGLU3.place(x=461, y=572)

        self.labelPETR4 = tk.Label(root)
        self.labelPETR4.configure(text='ITUB4:', font="Times 12 bold", fg="black", bg="white")
        self.labelPETR4.place(x=672, y=572)


    def atualizaGraficoABEV3(self,metrica):
        global abev3
        if metrica == "sem id":
            abev3 = "sem id"
            load = Image.open("images/ABEV3/ABEV3semid.png")
        elif metrica == "abertura":
            abev3 = "abertura"
            load = Image.open("images/ABEV3/ABEV3open.png")
        elif metrica == "volume":
            abev3 = "volume"
            load = Image.open("images/ABEV3/ABEV3volume.png")
        elif metrica == "fechamento":
            abev3 = "fechamento"
            load = Image.open("images/ABEV3/ABEV3close.png")
        elif metrica == "media":
            abev3 = "media"
            load = Image.open("images/ABEV3/ABEV3semid.png")

        render = ImageTk.PhotoImage(load)
        graph1 = Label(self.frame0, image=render)
        graph1.image = render
        graph1.place(x=39, y=15)

    def atualizaGraficoITUB4(self, metrica):
        global itub4
        if metrica == "sem id":
            itub4 = "sem id"
            load2 = Image.open("images/ITUB4/ITUB4semid.png")
        elif metrica == "abertura":
            itub4 = "abertura"
            load2 = Image.open("images/ITUB4/ITUB4open.png")
        elif metrica == "volume":
            itub4 = "volume"
            load2 = Image.open("images/ITUB4/ITUB4volume.png")
        elif metrica == "fechamento":
            itub4 = "fechamento"
            load2 = Image.open("images/ITUB4/ITUB4close.png")
        elif metrica == "media":
            itub4 = "media"
            load2 = Image.open("images/ITUB4/ITUB4semid.png")
        render = ImageTk.PhotoImage(load2)
        graph1 = Label(self.frame0, image=render)
        graph1.image = render
        graph1.place(x=639, y=15)

    def atualizaGraficoMGLU3(self, metrica):
        global mglu3
        if metrica == "sem id":
            mglu3 = "sem id"
            load3 = Image.open("images/MGLU3/MGLU3semid.png")
        elif metrica == "abertura":
            mglu3 = "abertura"
            load3 = Image.open("images/MGLU3/MGLU3open.png")
        elif metrica == "volume":
            mglu3 = "volume"
            load3 = Image.open("images/MGLU3/MGLU3volume.png")
        elif metrica == "fechamento":
            mglu3 = "fechamento"
            load3 = Image.open("images/MGLU3/MGLU3close.png")
        elif metrica == "media":
            mglu3 = "media"
            load3 = Image.open("images/MGLU3/MGLU3semid.png")
        render = ImageTk.PhotoImage(load3)
        graph1 = Label(self.frame0, image=render)
        graph1.image = render
        graph1.place(x=39, y=277)

    def atualizaGraficoPETR4(self, metrica):
        global petr4
        if metrica == "sem id":
            petr4 = "sem id"
            load4 = Image.open("images/PETR4/PETR4semid.png")
        elif metrica == "abertura":
            petr4 = "abertura"
            load4 = Image.open("images/PETR4/PETR4open.png")
        elif metrica == "volume":
            petr4 = "volume"
            load4 = Image.open("images/PETR4/PETR4volume.png")
        elif metrica == "fechamento":
            petr4 = "fechamento"
            load4 = Image.open("images/PETR4/PETR4close.png")
        elif metrica == "media":
            petr4 = "media"
            load4 = Image.open("images/PETR4/PETR4semid.png")
        render = ImageTk.PhotoImage(load4)
        graph1 = Label(self.frame0, image=render)
        graph1.image = render
        graph1.place(x=639, y=277)

def iniciar():
    global root
    global rootTroca
    global ABEV3, MGLU3, PETR4, ITUB4

    # time.sleep(10)

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

