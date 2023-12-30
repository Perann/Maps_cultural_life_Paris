# A map of Paris cultural life

Tonight you want to enjoy the incredible cultural life of Paris but with so much opportunities where should you go ? What should you watch ? And of course, you are curious to kwon how much it will cost you...
...We have designed this interface to help you !! 

Our project aims at helping you to visualize all the cultural activities you can attend: theatre plays, movies, shows and concerts. It will not only help you choose your evening schedule, but also discover the history of the cultural life in Paris and its districts. By the end of the day, you will know everything about the prices, the places and the opportunities this wonderful city has to offer. 


We are three passionate students from ENSAE, all lovers of Paris and its cultural life. We wanted to help you find what you love, and what fits your budget to enjoy your evening. 

Perann 
Nicolas
Grégoire


# Description of our project

Our algorithm lets you choose the type of activity you want to attend: theatre, movies, concert. The part on Musical bar is not finished yet.
Next you choose the date and the hours you are aviable.
In the end it displays you a map of Paris with markers on the establishments that have an event on the day and the hours you chose. Clicking on the marker provides you additional information about the place: the name, address, event details and average price. 


# Structure of this github

4 folders are dedicated to the main kind of activities we help you to find: theatres, movie theatre, concert hall and musical bar. In each of them, you will find our code that scraps some websites to find the names of the establishments, their addresses and their schedule. If you are only interested in viewing the map, you will just have to go in the folder Map.

Some folders are added to the previous:

1 folder 'Outputs' in which you will find the databases we created after scrapping and cleaning the data from internet.

1 folder 'Ressources' in which you'll find databases and images we donwloaded on the internet 

1 folder 'Statistics' in which you will find some analyses providing further ideas about prices and top tip !

Moreover, one file interface.py lauches the interface we developped and a file main.ipynb allows to run all our codes in guided notebook.

# Interface
Running the file interface.py opens this window on your computer. It allows you to generate interactive maps of activities you can do.
You have 3 categories: "Cinema", "Theatre" and "Concert". For the cagegory Cinema, the code currently only allows you to display the moovies that are played today. The Database for cinema has been last updated 28th of January but you can update it by running the scraping programs. For theater and concert, you choose the day when you want to go out and it will give you the possibilities for the day you requested. Enjoy !


![InterfaceDemo](https://github.com/Perann/Maps_cultural_life_Paris/assets/125759494/14d2dd44-4fa5-437d-b9fe-451c56f6ff67)

 By filling the Entry and click on "Génerer la carte", a card will open on your default browser. 
 A precise format is requiered for the entries: YYYY-MM-DD for Théâtre and HhM for Cinema.
Once you've done that, you can navigate, click and get further details on your favorites activties ! 

 
![Cartedemo](https://github.com/Perann/Maps_cultural_life_Paris/assets/125759494/cd8679d4-69d3-415d-b086-ddab85bc87ec)

# What to run ?

If you want to run the functions without the interface you can run the main notebook. There you'll find functions we used in the interface and will be able to run them by specifying the arguments. The cards generated will be automatically registered in the following section: 'Output/Maps', you'll have to open them in a webbrowser to see them. JupyterLab does it by itself, VS code requiers the extension 'Open in browser' to do so. You'll be guided through your use of it and explanatations and details o the project are given in it. Moreover the main notebook entails all the statistics we did about activities in Paris. We recommend you to run it if you wanna know how the project has been developped. 

# Python's Modules:

A file requirements.txt is attached containing all the pluggs in you need to install to run the interface.
