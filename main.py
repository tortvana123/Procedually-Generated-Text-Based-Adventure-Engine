# Procedually Generated Text Based Adventure Engine
# A GUI game engine for a procedually generatated text adventure,
# which is intended to take place in a "dungeon" type enviroment.
# Author: Alex Vreimann, Licence: MIT.

# -----------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------
import ruamel.yaml as yaml
from appJar import gui
from random import choice

# -----------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------
conf_file = "info.yaml"
rooms = {}
room_amount = 0
# -----------------------------------------------------------------------
# Functions and classes
# -----------------------------------------------------------------------

# ----
# YAML input/output, compatible with old and new versions of ruamel.yaml
def yml_io(ser_type, istream=None):  # ser_type - "serialize" data into YAML or "deserialize" data from YAML; istream - input data
    ostream = ""

    if yaml.version_info < (0, 15):
        if ser_type == "deserialize":
            ostream = yaml.safe_load(istream)
            return ostream
        elif ser_type == "serialize":
            yaml.safe_dump(istream, ostream)
            return ostream
    else:
        yml = yaml.YAML(typ='safe', pure=True)  # 'safe' load and dump
        if ser_type == "deserialize":
            ostream = yml.load(istream)
            return ostream
        elif ser_type == "serialize":
            yml.dump(istream, ostream)
            return ostream


# ----
# Intialize data from the data file.
def import_data_from_file():
    global data
    with open(conf_file) as yaml_data:
        data = yml_io("deserialize", yaml_data)


# ----
# Button function
def press(btn):
    if btn == "Start Game":
        game()
        
# ----
# Room class (WIP)
class Room:
    def __init__(self, name, description):  # Data init
        self.name = name
        self.description = description

    @classmethod
    def start_room_gui(cls): # WIP
        app.startSubWindow("Rooms")
        app.addLabel("Title11", "Rooms")
        app.stopSubWindow()
        app.showSubWindow("Rooms")
        
    def show(self):
        app.removeAllWidgets()
        app.addLabel("Title", self.name)
        app.addLabel("Description", self.description)

class Rooms_Window: # WIP
    def __init__(self, rooms):
        self.rooms = rooms

    def show(self):
        pass

# ----
# Room Generator
def generate_room():
    global data
    global rooms
    global room_amount
    room_amount += 1
	
    room_type = choice(data["room_type"])# To do - add chances to room types happening. random.randrange?
    room_description = choice(data["room_descriptions"])
    rooms[room_amount] = Room(room_type, room_description)
	
	
# ----
# GAME (WIP)
def game():
    generate_room()
    rooms[1].show()
    Room.start_room_gui()
    
    

# ----
# Title screen
def title_screen():
    global app
    with gui(data["title_titlebar"]) as app:
        app.addLabel("Title_Label", data["title_label"])
        app.addLabel("Message", data["title_description"])
        app.addButton("Start Game", press)


# ----
# Main
def main():
    import_data_from_file()
    title_screen()


if __name__ == "__main__":  # If the file is used as a game, not a library
    main()

