from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import*
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Previsão do Tempo")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)


##icone
image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file="images/rounded-rectangle-xxl.png")
Label(root,image=Round_box, bg="#57adff").place(x=30,y=110)

#Label
Label_1 = Label(root,text="Temperatura", font=("Helvetica",11),fg="white", bg="#203243")












root.mainloop()

