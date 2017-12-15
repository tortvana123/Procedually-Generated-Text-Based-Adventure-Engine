#-----------------------------------------------------------------------------------------------------------------------------------------
# Imports

from ruamel import yaml
from appJar import gui
#-----------------------------------------------------------------------------------------------------------------------------------------
# Variables
conf_file = "info.yaml"
#-----------------------------------------------------------------------------------------------------------------------------------------
#Functions

#YAML input/output, compatible with old and new versions of ruamel.yaml
def yml_io(ser_type, istream=None): # ser_type - "serialize" data into YAML or "deserialize" data from YAML; istream - input data  
    
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

# Intialize data from an info file
def init_data(): 
    global data
    with open(conf_file) as yaml_data:
        data = yml_io("deserialize", yaml_data)

#Button function
def press(btn):
    if btn == "Quit":
        raise SystemExit
# Title screen  
def title_screen():
    with gui(data["title_titlebar"]) as app:
        app.addLabel("Title_Label", data["title_label"])
        app.addLabel("msg1", data["title_description"])
        app.addButton("Start Game", press)
        app.addButton("Quit", press)
        app.go()

# Main
def main():
    init_data()
    title_screen()

if __name__ == "__main__": # If the file is used as a game, not a library
    main()