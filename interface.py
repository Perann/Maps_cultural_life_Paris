#This code launches an  Interface to enter the type of activity you want to do and sifferent information
# Sadly, SSP cloud computers don't allow us to make that run ( it uses tkinter), you can either wait until the defense for a live demo
# or make the code run on your personnal computer.
# To run the functions used through this interface, you should use the Notebook MapsPlotter of the repository

from tkinter import *  
import pandas as pd
from PIL import Image, ImageTk


from Cinema.mapping import MovieMapping
dataCinema = pd.read_csv('Outputs/DataSets/DataCinema.csv')
from TheatresOperas.mapping import TheaterMap
DataTheater = pd.read_csv('Outputs\DataSets\DataTheatre_base_finale.csv', sep = ';')


#Defining the executive functions for the buttons 

def executer_carte_cinema():
    # Récupérer les valeurs des Entry
    valeur1 = str(entry_arg1.get())
    valeur2 = str(entry_arg2.get())
    MovieMapping(dataCinema,valeur1,valeur2)

def executer_carte_theatre():
    valeur3 = str(entry_arg3.get())
    TheaterMap(DataTheater,valeur3)

def executer_carte_concert():
    valeur4 = str(entry_arg4.get())
    pass


window  = Tk()
window.title('Ou sortir à Paris ?')

image = Image.open("Ressources/Pictures/leonard-cotte-R5scocnOOdM-unsplash.jpg") 
photo = ImageTk.PhotoImage(image)
canvas = Canvas(window, width=image.width, height=image.height)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=photo)




Title = Label(window,text = 'Ou sortir à Paris ?',font=("Arial", 20))
Title.place(x = 225, y = 50)

#Buttons for Cinema
Cat1 = Label(window, text = 'Cinema', font = ("Arial",15))
Cat1.place(x = 115, y = 150)


label_arg1 = Label(window, text="Heure de début")
label_arg1.place(x = 115, y = 225)
entry_arg1 = Entry(window)
entry_arg1.place(x = 115,y = 250)

label_arg2 = Label(window, text="Heure de fin")
label_arg2.place(x = 115, y=275)
entry_arg2 = Entry(window)
entry_arg2.place(x = 115, y = 300)

button_executer = Button(window, text="Génerer la carte", command=executer_carte_cinema)
button_executer.place(x = 115, y = 325) 


#Buttons for Theater
Cat2 = Label(window, text = 'Theatre', font = ("Arial",15))
Cat2.place(x = 275, y = 150)


label_arg3 = Label(window, text="Quel Jour ?")
label_arg3.place(x = 275, y = 250)
entry_arg3 = Entry(window)
entry_arg3.place(x = 275,y = 275)


button_executer = Button(window, text="Génerer la carte", command=executer_carte_theatre)
button_executer.place(x = 275, y = 325) 

#Buttons for Concerts

Cat3 = Label(window, text = 'Concerts', font = ("Arial",15))
Cat3.place(x = 420, y = 150)

label_arg4 = Label(window, text="Quel Jour ?")
label_arg4.place(x = 420, y = 250)
entry_arg4 = Entry(window)
entry_arg4.place(x = 420,y = 275)


button_executer = Button(window, text="Génerer la carte", command=executer_carte_concert)
button_executer.place(x = 420, y = 325) 



window.mainloop()




