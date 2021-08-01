from tkinter import *

# Création de la fenêtre
window = Tk()

# Modification de la fenêtre
window.title('My Application')
window.geometry('1080x720')
window.minsize(480, 360)

# Création des boites
title_frame = Frame(window)
button_frame = Frame(title_frame)

# Accueil
title = Label(title_frame, text='Bienvenue dans My Application !', font=('Arial', 30))
title.pack(pady=40)

subtitle = Label(title_frame, text='Choisissez une option', font=('Arial', 20))
subtitle.pack()

# Création des boutons
morpion_button = Button(button_frame, text='Morpion', font=('Arial', 15)).grid(row=0, column=1)

rpg_button = Button(button_frame, text='Mini RPG', font=('Arial', 15)).grid(row=0, column=2)

# Affichage des boites
title_frame.pack()
button_frame.pack(pady=50)

# Affichage de la fenêtre
window.mainloop()
