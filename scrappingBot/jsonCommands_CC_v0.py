from scalpl import Cut
import json
import os

def fileLoad(file):
    with open(file,'r') as json_file:
        data = json.load(json_file)
        return data
        
def fileDump(file,data):
    with open(file, 'w') as outfile:
        json.dump(data, outfile)