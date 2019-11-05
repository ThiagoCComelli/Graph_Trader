from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class Program():
    def __init__(self,master):
        self.root = root.geometry("1280x720"), root.resizable(width=False, height=False)
        self.screen()

    def screen(self):
        # frame 0 = top-left
        # frame 1 = top-right
        # frame 2 = botton-left
        # frame 3 = botton-right

        root.configure(background="white")

        load = Image.open("images/ABEV3.png")
        render = ImageTk.PhotoImage(load)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=39, y=-25)

        load = Image.open("images/ITUB4.png")
        render = ImageTk.PhotoImage(load)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=639, y=-25)

        load = Image.open("images/MGLU3.png")
        render = ImageTk.PhotoImage(load)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=39, y=261)

        load = Image.open("images/PETR4.png")
        render = ImageTk.PhotoImage(load)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=639, y=261)

        metrABEV3 = tk.IntVar()
        metrMGLU3 = tk.IntVar()
        metrITUB4 = tk.IntVar()
        metrPETR4 = tk.IntVar()


        stocks = [("Médias Móveis", 1), ("Volume", 2), ("Banda de Bollinger", 3), ("Fechamento", 4), ("Sem indicador", 5)]

        # metricas ABEV3
        tk.Radiobutton(root, text="Médias Móveis             ", padx=0, variable=metrABEV3, value=1, bg="white").place(x=39, y=596)
        tk.Radiobutton(root, text="Volume                         ", padx=0, variable=metrABEV3, value=2, bg="white").place(x=39, y=618)
        tk.Radiobutton(root, text="Banda de Bollinger       ", padx=0, variable=metrABEV3, value=3, bg="white").place(x=39, y=640)
        tk.Radiobutton(root, text="Fechamento                  ", padx=0, variable=metrABEV3, value=4, bg="white").place(x=39, y=662)
        tk.Radiobutton(root, text="Sem indicador               ", padx=0, variable=metrABEV3, value=5,bg="white").place(x=39, y=684)


        tk.Radiobutton(root, text="Médias Móveis             ", padx=0, variable=metrMGLU3, value=1, bg="white").place(x=250, y=596)
        tk.Radiobutton(root, text="Volume                         ", padx=0, variable=metrMGLU3, value=2, bg="white").place(x=250, y=618)
        tk.Radiobutton(root, text="Banda de Bollinger       ", padx=0, variable=metrMGLU3, value=3, bg="white").place(x=250, y=640)
        tk.Radiobutton(root, text="Fechamento                  ", padx=0, variable=metrMGLU3, value=4, bg="white").place(x=250, y=662)
        tk.Radiobutton(root, text="Sem indicador               ", padx=0, variable=metrMGLU3, value=5,bg="white").place(x=250, y=684)


        tk.Radiobutton(root, text="Médias Móveis             ", padx=0, variable=metrPETR4, value=1, bg="white").place(x=461,y=596)
        tk.Radiobutton(root, text="Volume                         ", padx=0, variable=metrPETR4, value=2, bg="white").place(x=461, y=618)
        tk.Radiobutton(root, text="Banda de Bollinger       ", padx=0, variable=metrPETR4, value=3, bg="white").place(x=461,y=640)
        tk.Radiobutton(root, text="Fechamento                  ", padx=0, variable=metrPETR4, value=4, bg="white").place(x=461,y=662)
        tk.Radiobutton(root, text="Sem indicador               ", padx=0, variable=metrPETR4, value=5,bg="white").place(x=461, y=684)


        tk.Radiobutton(root, text="Médias Móveis             ", padx=0, variable=metrITUB4, value=1, bg="white").place(x=672,y=596)
        tk.Radiobutton(root, text="Volume                         ", padx=0, variable=metrITUB4, value=2, bg="white").place(x=672, y=618)
        tk.Radiobutton(root, text="Banda de Bollinger       ", padx=0, variable=metrITUB4, value=3, bg="white").place(x=672,y=640)
        tk.Radiobutton(root, text="Fechamento                  ", padx=0, variable=metrITUB4, value=4, bg="white").place(x=672,y=662)
        tk.Radiobutton(root, text="Sem indicador               ", padx=0, variable=metrITUB4, value=5,bg="white").place(x=672, y=684)

        buyABEV = tk.Button(root, text="COMPRAR ABEV3", width=15, height=0).place(x=870, y=566)
        sellABEV = tk.Button(root, text="VENDER ABEV3", width=15, height=0).place(x=870, y=600)

        buyMGLU = tk.Button(root, text="COMPRAR MGLU3", width=15, height=0).place(x=870, y=650)
        sellMGLU = tk.Button(root, text="VENDER MGLU3", width=15, height=0).place(x=870, y=684)

        buyPETR4 = tk.Button(root, text="COMPRAR PETR4", width=15, height=0).place(x=1050, y=566)
        sellPETR4 = tk.Button(root, text="VENDER PETR4", width=15, height=0).place(x=1050, y=600)

        buyITUB4 = tk.Button(root, text="COMPRAR ITUB4", width=15, height=0).place(x=1050, y=650)
        sellITUB4 = tk.Button(root, text="VENDER ITUB4", width=15, height=0).place(x=1050, y=684)

        # self.photo = PhotoImage(file="images/c0books_read.jpeg")
        # self.backlabel = Label(self.frame0, image=self.photo).place(x=-1, y=-1)




root = tk.Tk()
Program(root)
root.mainloop()