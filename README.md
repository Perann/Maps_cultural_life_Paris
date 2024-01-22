# A Map of Parisian Cultural Life

Tonight, you want to enjoy the incredible cultural life of Paris, but with so many opportunities, where should you go? What should you watch? And, of course, you are curious to know how much it will cost you...

We have designed this interface to help you!

Our project aims to assist you in visualizing all the cultural activities you can attend: theatre plays, movies, shows, and concerts. It will not only help you choose your evening schedule but also discover the history of the cultural life in Paris and its districts. By the end of the day, you will know everything about the prices, the places, and the opportunities this wonderful city has to offer.

We are three passionate students from ENSAE, all lovers of Paris and its cultural life. We wanted to help you find what you love and what fits your budget to enjoy your evening.

Perann

Nicolas

Grégoire

# Description of Our Project

Our algorithm allows you to choose the type of activity you want to attend: theater, movies, or concerts. Please note that the section on Musical Bars is still under development.

Next, you choose the date and the hours you are available. In the end, it displays a map of Paris with markers on the establishments that have an event on the day and at the hours you selected. Clicking on a marker provides additional information about the place: the name, address, event details, and average price.

# Structure of This GitHub Repository

- **Main Folder:**
  Contains all the essential code and statistics. Run it to create maps and view our results.

- **Activity-Specific Folders:**
  - `Theatres`: Code that scrapes websites to find names, addresses, and schedules of theatres.
  - `Movie Theatre`: Similar code for movie theatres.
  - `Concert Hall`: Code for concert halls.
  - `Musical Bar`: (Under development) Code for musical bars. If you're only interested in viewing the map, check the `Map` folder in each of these.

- **Additional Folders:**
  - `Outputs`: Databases created after scraping and cleaning data from the internet.
  - `Resources`: Databases and images downloaded from the internet.
  - `Statistics`: Analyses providing further insights into prices and top tips.

- **Files:**
  - `interface.py`: Launches the developed interface.
  - `main.ipynb`: Allows running all our codes in a guided notebook.

# Interface

Running the file `interface.py` opens this window on your computer, enabling you to generate interactive maps of various activities.

There are three categories: "Cinema," "Theatre," and "Concert." For the "Cinema" category, the current code allows you to display movies playing today. The cinema database was last updated on January 28th, but you can update it by running the scraping programs.

For "Theatre" and "Concert," you choose the day you want to go out, and it will provide you with the possibilities for the requested day. Enjoy!



![InterfaceDemo](https://github.com/Perann/Maps_cultural_life_Paris/assets/125759494/14d2dd44-4fa5-437d-b9fe-451c56f6ff67)

By filling the entry and clicking on "Générer la carte," a map will open in your default browser. A precise format is required for the entries: YYYY-MM-DD for Theatre and HhM for Cinema.

Once you've done that, you can navigate, click, and get further details on your favorite activities!

 
![Cartedemo](https://github.com/Perann/Maps_cultural_life_Paris/assets/125759494/cd8679d4-69d3-415d-b086-ddab85bc87ec)

# How to Run Without Interface?

If you want to execute the functions without the interface, you can run the main notebook. Inside, you'll find the functions used in the interface that you can run by specifying the arguments. The generated cards will be automatically saved in the 'Output/Maps' section. To view them, open them in a web browser. JupyterLab does it automatically, while VS Code requires the 'Open in browser' extension.

The main notebook provides guidance, explanations, and project details. Additionally, it includes all the statistics we conducted about activities in Paris. We recommend running it to understand the project's development.

# Python Modules:

A file `requirements.txt` is attached, containing all the plugins you need to install to run the interface.
