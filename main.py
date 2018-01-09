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
def init_data():
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
    def show_room(self):
        app.removeAllWidgets()
        app.addLabel("Title", self.name)
        app.addLabel("Description", self.description)

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
    init_data()
    title_screen()


if __name__ == "__main__":  # If the file is used as a game, not a library
    main()
# This is a test.
