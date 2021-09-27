import socket
import os
from tkinter import *

# Variables

hostname = socket.gethostname()

userName = os.getenv("USERNAME")

ip = socket.gethostbyname(hostname)

# Création fenêtre

window = Tk()

# Personnalisatoin fenêtre

window.title("Informations Ordinateur")

window.geometry("800x400")

window.minsize(700, 400)

window.iconbitmap("Votre icone en .ico")

# création de la frame

frame = Frame(window)

# Image

img = PhotoImage(file="Votre logo en .png/.jpeg/.jpg")

labelImg = Label(window, image=img)

labelImg.place(x=10, y=10)

# Informations

label_title = Label(frame, text="Bienvenue " + userName, font=("Georgia", 30))

label_title.pack(pady=50)

hostInfo = Label(frame, text="Le nom de votre machine est : " + hostname, font=("Georgia", 15))

hostInfo.pack(pady=30)

ipInfo = Label(frame, text="Votre adresse IP est : " + ip, font=("Georgia", 15))

ipInfo.pack(pady=10)

frame.pack()

# Affichage de la fenêtre

window.mainloop()
