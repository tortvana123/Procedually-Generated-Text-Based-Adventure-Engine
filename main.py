import appJar # learn more: https://python.org/pypi/appJar
#-----------------------------------------------------------------------------------------------------------------------------------------
# Imports

from ruamel import yaml
from appJar import gui

#-----------------------------------------------------------------------------------------------------------------------------------------
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

def init_data():
    pass
def title_screen():
    pass

def main():
    init_data()
    title_screen()


main()
#-----------------------------------------------------------------------------------------------------------------------------------------
# GUI TESTING
def press(btn):
    print(btn)


with gui("TESTING GAME", "400x200") as app:
    app.addLabel("Game_Title", "WELCOME!")
    app.addMessage("msg1", """You can put a lot of text in this widget.
The text will be wrapped over multiple lines.
It's not possible to apply different styles to different words.""")
    app.addButton("One", press)
    app.addButton("Two", press)
    app.addButton("Three", press)
    app.go()
#-----------------------------------------------------------------------------------------------------------------------------------------
# TEST CODE
#with open("info.yaml") as f:
    #print(yml_io("deserialize", f))