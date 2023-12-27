#This code launches an  Interface to enter the type of activity you want to do and sifferent information
# Sadly, SSP cloud computers don't allow us to make that run ( it uses tkinter), you can either wait until the defense for a live demo
# or make the code run on your personnal computer.
# To run the functions used through this interface, you should use the Notebook MapsPlotter of the repository

from tkinter import *  
import pandas as pd
from PIL import Image, ImageTk


from Cinema.mapping import MovieMapping
data = pd.read_csv('Maps_cultural_life_Paris/Outputs/DataSets/DataCinema.csv')


def executer_carte():
    # Récupérer les valeurs des Entry
    valeur1 = str(entry_arg1.get())
    valeur2 = str(entry_arg2.get())
    MovieMapping(data,valeur1,valeur2)

window  = Tk()
window.title('Ou sortir à Paris ?')

image = Image.open("Maps_cultural_life_Paris/Ressources/Pictures/leonard-cotte-R5scocnOOdM-unsplash.jpg") 
photo = ImageTk.PhotoImage(image)
canvas = Canvas(window, width=image.width, height=image.height)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=photo)


Title = Label(window,text = 'Ou sortir à Paris ?',font=("Arial", 20))
Title.place(x = 225, y = 50)

label_arg1 = Label(window, text="Heure de début")
label_arg1.place(x = 275, y = 175)
entry_arg1 = Entry(window)
entry_arg1.place(x = 275,y = 200)


label_arg2 = Label(window, text="Heure de fin")
label_arg2.place(x = 275, y=245)
entry_arg2 = Entry(window)
entry_arg2.place(x = 275, y = 270)

button_executer = Button(window, text="Génerer la carte", command=executer_carte)
button_executer.place(x = 290, y = 325) 

window.mainloop()




