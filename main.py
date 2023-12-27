from tkinter import *
import pandas as pd
from PIL import Image, ImageTk

#Plotting the map of Cinema with an GUI

from Cinema.mapping import MovieMapping
data = pd.read_csv('Outputs\DataSets\DataCinema.csv')


def executer_carte():
    # Récupérer les valeurs des Entry
    valeur1 = str(entry_arg1.get())
    valeur2 = str(entry_arg2.get())
    MovieMapping(data,valeur1,valeur2)

window  = Tk()
window.title('Ou sortir à Paris ?')
window.geometry('1920x1280')

image = Image.open("Ressources\Pictures\john-towner-UO02gAW3c0c-unsplash.jpg")  
photo = ImageTk.PhotoImage(image)
canvas = Canvas(window, width=1920, height=1280)
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=photo)

Title = Label(window,text = 'Ou sortir à Paris ?',font=("Arial", 20))
Title.pack(padx = 100, pady = 100)
label_arg1 = Label(window, text="Heure de début")
label_arg1.pack()
entry_arg1 = Entry(window)
entry_arg1.pack()

label_arg2 = Label(window, text="Heure de fin")
label_arg2.pack()
entry_arg2 = Entry(window)
entry_arg2.pack()

button_executer = Button(window, text="Génerer la carte", command=executer_carte)
button_executer.pack()

window.mainloop()




#Plotting the map of Theater
