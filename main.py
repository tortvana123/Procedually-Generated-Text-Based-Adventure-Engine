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
# -----------------------------------------------------------------------
# Functions and classes
# -----------------------------------------------------------------------

# ----
# YAML input/output, compatible with old and new versions of ruamel.yaml
def yml_io(ser_type,istream=None):  # ser_type - "serialize" data into YAML or "deserialize" data from YAML; istream - input data
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

    def __init__(self, name):  # Data init
        self.name = name

    def enter_room(self):
        print("")


# ----
# GAME (WIP)
def game():
    pass

    # app.setLabel("Title_Label", choice(data["room_names"]))
    # app.setLabel("Message", choice(data["room_descriptions"]))


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
