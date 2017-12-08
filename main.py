#-------------------------------------------------------------------------------------------------------------------------------------------

# Imports
from ruamel import yaml

#-------------------------------------------------------------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------------------------------------------------------------
with open("info.yaml") as f:
    print(yml_io("deserialize", f))