![InterfaceDemo](https://github.com/Perann/Maps_cultural_life_Paris/assets/125759494/14d2dd44-4fa5-437d-b9fe-451c56f6ff67)
# A map of Paris cultural life

Tonight you want to enjoy the incredible cultural life of Paris but with so much opportunities where should you go ? What should you watch ? And of course, you are curious to kwon how much it will cost you...
...We have designed this interface to help you !! 

Our project aims at helping you to visualize all the cultural activities you can attend: theatre plays, movies, shows and concerts. It will not only help you choose your evening schedule, but also discover the history of the cultural life in Paris and its districts. By the end of the day, you will know everything about the prices, the places and the opportunities this wonderful city has to offer. 


We are three passionate students from ENSAE, all lovers of Paris and its cultural life. We wanted to help you find what you love, and what fits your budget to enjoy your evening. 
    Perann 
    Nicolas
    Grégoire


# Description of our project

Our algorithm lets you choose the type of activity you want to attend: theatre, movies, concert.
Next you choose the date and the hours you are aviable.
In the end it displays you a map of Paris with markers on the establishments that have an event on the day and the hours you chose. Clicking on the marker provides you additional information about the place: the name, address, event details and average price. 


# Structure of this github

4 folders are dedicated to the main kind of activities we help you to find: theatres, movie theatre, concert hall and musical bar. In each of them, you will find our code that scraps some websites to find the names of the establishments, their addresses and their schedule. If you are only interested in viewing the map, you will just have to go in the folder Map

1 folder 'Outputs' in which you will find the databases we created after scrapping and cleaning the data from internet.

# Interface
Running the file interface.py opens this window on your computer. It allows you to generate interactive Maps of activity you can do.
You have 3 categories: "Cinema", "Theatre" and "Concert". For the cagegory Cinema, the code currently only allows you to see the moovies that are played today. The Database for cinema has been last updated 28th of January but you can update it by running the scraping programs. For theater and concert, you choose the day when you want to go out and it will give you concerts and theater plays that you can see on the day you requested. Enjoy !


![InterfaceDemo](https://github.com/Perann/Maps_cultural_life_Paris/assets/125759494/14d2dd44-4fa5-437d-b9fe-451c56f6ff67)

 By filling the Entry and click on "Generer la carte", a card will open on your default browser. Thus you can navigate, click and get further details on your favorites activties ! 

 
![Cartedemo](https://github.com/Perann/Maps_cultural_life_Paris/assets/125759494/cd8679d4-69d3-415d-b086-ddab85bc87ec)

# Using the App without Interface
If you want to use the app without the interface, you can run the main notebook named 'MapsPlotter.ipynb'. You will find there all the functions used in the interface (they are a bit modified so that they don't automatically open the card on a webbrowser)  and will be able to run them specifying the arguments. The cards generated will be automatically registered in the following section: 'Output/Maps'. You need to open them in a webbrowser to see them. JupyterLab does it by itself, VS code requiered the extension 'Open in browser' to do so.
 
# Python's Modules:

A file requirements.txt is attached, it allows you to generates a functionnal environments to make the code runs

# Extra advices:
