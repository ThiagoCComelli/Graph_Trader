from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

class Program():
    def __init__(self,master):
        self.root = root.geometry("1280x720"), root.resizable(width=False, height=False)
        self.screen()

    def screen(self):
        #frame 0 = top-left
        #frame 1 = top-right
        #frame 2 = botton-left
        #frame 3 = botton-right

        self.frame0 = tk.Frame(root, width = 640, height = 360,bg = 'black')
        self.frame0.place(x=0,y=0)

        self.frame1 = tk.Frame(root, width=640, height=360, bg='yellow')
        self.frame1.place(x=640, y=0)

        self.frame2 = tk.Frame(root, width=640, height=360, bg='blue')
        self.frame2.place(x=0, y=360)

        self.frame3 = tk.Frame(root, width=640, height=360, bg='red')
        self.frame3.place(x=640, y=360)

        self.photo = PhotoImage(file="images/c0books_read.jpeg")
        self.backlabel = Label(self.frame0, image=self.photo).place(x=-1, y=-1)




root = tk.Tk()
Program(root)
root.mainloop()