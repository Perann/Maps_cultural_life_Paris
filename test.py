import tkinter as tk
from PIL import Image, ImageTk

fenetre = tk.Tk()
fenetre.title("Fenêtre avec image de fond")

# Charger l'image
image = Image.open("Ressources\Pictures\leonard-cotte-R5scocnOOdM-unsplash.jpg")  # Remplacez "chemin/vers/votre/image.jpg" par le chemin de votre image
photo = ImageTk.PhotoImage(image)

# Créer un Canvas pour afficher l'image de fond
canvas = tk.Canvas(fenetre, width=image.width, height=image.height)
canvas.pack()

# Afficher l'image de fond
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
button = tk.Button(fenetre, text="Cliquez-moi")
# Utiliser place() pour spécifier les coordonnées du bouton par rapport au Canvas
button.place(x=50, y=50)

# Ajouter du texte
text_label = tk.Label(fenetre, text="Hello, Tkinter!")
# Utiliser place() pour spécifier les coordonnées du label par rapport au Canvas
text_label.place(x=100, y=100)

fenetre.mainloop()