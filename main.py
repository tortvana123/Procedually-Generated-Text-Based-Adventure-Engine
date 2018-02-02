# Procedually Generated Text Based Adventure Engine
# A GUI game engine for a procedually generatated text adventure,
# which is intended to take place in a "dungeon" type enviroment.
# Author: Alex Vreimann, Licence: MIT.

# ----
# Imports
# ----
import ruamel.yaml as yaml
from appJar import gui
from random import choices
from time import sleep

# ----
# Variables
# ----
conf_file = "info.yaml"
rooms = {}
# ----
# Functions and classes
# ----

# ----
# Quit Function
def quit_program(): 
    raise SystemExit
        
# ----
# YAML input/output, compatible with older and newer versions of ruamel.yaml (Confirmed working with 0.15.35)
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
# Room class (WIP)
class Room:
    room_amount = 0
    current_room = 0
    
    def __init__(self, id, type, action):  # Data init
        self.id = id
        self.type = type
        self.action = action

    @classmethod
    def generate_room(cls):
        # Make data available from external variables
        global data
        global rooms
        # Add one to the amount of rooms, for assigning an id.
        cls.room_amount += 1
	    #Room properties
        #room_type = choice(data["room_type"])# To do - add chances to room types happening. random.randrange?
        #room_description = choice(data["room_descriptions"])
        # Pick a random number in a range from 0 to 100, for a precentage chance, and pick a room type based on that.

        room_type
        """x = randrange(0, 101)
        if x <= 55:
            room_type = "Monster"
        elif x > 55 and x <= 80 :
            room_type = "Item"
        elif x > 80 and x <= 90:
            room_type = "Store"
        elif x == 91:
            room_type = "Instant Death"
        elif x > 91:
            room_type = "Nothing"
        """
        room_actions = "Something"
        # Initialize object
        rooms[cls.room_amount] = Room(cls.room_amount, room_type, room_actions) # 1st is room ID.
        
    def show_room(self):
        app.removeAllWidgets()
        current_room = self.id
        #if self.type != "Store":
         #   if self.type == "Monster":
          #      pass
           # if self.type == "Item":
            #    pass
            #if self.type == "Instant Death":
             #   pass
            #if self.type == "Nothing":
             #   pass
        #elif self.type == "Store":
         #   app.addLabel("Store")
          #  app.addLabel("Still a WIP, please ignore.")
        app.addButton("Select", Room.action)

    @classmethod
    def action(cls, action):
        global data
        print(data)

# ----
# Button function - Rooms
def room_action(test):
    print(test)
    #elif button == "foo": # testing
        #Room.generate_room()
        #rooms[Room.room_amount].show_room()

# ----
# Button function - Start/Stop Program
def start_btn(button):
    if button == "Start Game":
        Room.generate_room()
        rooms[1].show_room()
    elif button == "Quit":
        quit_program()

# ----
# Title screen
def title_screen():
    global app
    with gui(data["title_titlebar"]) as app:
        app.addLabel("Title_Label", data["title_label"])
        app.addLabel("Message", data["title_description"])
        app.addButton("Start Game", start_btn)
        app.addButton("Quit", start_btn)


# ----
# Main
def main():
    import_data_from_file()
    title_screen()


if __name__ == "__main__":  # If the file is used as a program, not a library etc.
    main()

