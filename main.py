# Procedually Generated Text Based Adventure Engine
# A GUI game engine for a procedually generatated text adventure,
# which is intended to take place in a "dungeon" type enviroment.
# Author: Alex Vreimann, Licence: MIT.

# ----
# Imports
# ----
import ruamel.yaml as yaml
from appJar import gui
from random import choice

# ----
# Variables
# ----
conf_file = "info.yaml"
rooms = {}
# ----
# Functions and classes
# ----

# ----
# YAML input/output, compatible with older and newer versions of ruamel.yaml (Working with 0.15.35)
def yml_io(ser_type, istream=None):  # ser_type - "serialize" data into YAML or "deserialize" data from YAML; istream - input data
    ostream = ""

    if yaml.version_info < (0, 15): # Versions before 0.15 used a different syntax.
        if ser_type == "deserialize":
            ostream = yaml.safe_load(istream)
            return ostream
        elif ser_type == "serialize":
            yaml.safe_dump(istream, ostream)
            return ostream
    else:
        yml = yaml.YAML(typ='safe', pure=True)  # Using new syntax.
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
    if btn == "Select": # Testing.
        if app.getOptionBox("What to do next?:") == "Show Room List":
            print(rooms)
    
        
# ----
# Room class (WIP)
class Room:
    room_amount = 0
    current_room = 0
    
    def __init__(self, id, name, description):  # Data init
        self.id = id
        self.name = name
        self.description = description

    @classmethod
    def generate_room(cls):
        # Make data available from external variables
        global data
        global rooms
        # Add one to the amount of rooms, for assigning an id.
        cls.room_amount += 1
	#Room properties
        room_type = choice(data["room_type"])# To do - add chances to room types happening. random.randrange?
        room_description = choice(data["room_descriptions"])
        # Initialize object
        rooms[cls.room_amount] = Room(cls.room_amount, room_type, room_description) # 1st is room ID.
        
    def show_room(self):
        app.removeAllWidgets()
        current_room = self.id
        app.addLabel("Title", self.name+str(self.id))
        app.addLabel("Description", self.description)
        app.addLabelSpinBox("What to do next?:", ["ayy", "lmao", "testing", "Open Room List"])
        app.addButton("Select", press)
        
        

# ----
# GAME (WIP)
def game():
    Room.generate_room()
    rooms[1].show_room()
    

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

