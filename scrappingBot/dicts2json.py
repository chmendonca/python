
import json
import timeit
from jsonCommands_CC_v0 import *
from scalpl import Cut



def wtGenericDict(file,scalplCut,dictFields,payload):
# =============================================================================
# This function was created to allow to write different levels and kinds of 
# data to a dictionary.
# In use at: calculationData.py

# This function creates a dictionary with the number of levels equal to the 
# length of the list "dictFields". The "payload" is the value to be added to the
# last key.
# If only one item is passed on the list "dictFields", this is the root key with
# only one level.
# Attention to the detail that this function already receives the whole data on
# the "scalplCut" variable and then changes it with the new information on the
# "dictFields" and "payload". This information replaces the oldest one on the 
# "file"
# =============================================================================

    for item in range(len(dictFields)):
        if item == 0:
            dictPathList = [dictFields[item]]
            dictPath = dictFields[item]
        else:
            dictPathList.append(dictFields[item])
            dictPath = '.'.join(dictPathList)

        if dictPath not in scalplCut:
            scalplCut[dictPath]={}

    print('\ndictPath: ',dictPath,'\n')

    scalplCut[dictPath]=payload

    with open(str(file),'w') as json_file:
        json.dump(scalplCut.data,json_file)
        print('\nFile Written\n')

def delGenericDict(scalplCut,dictFields):
#def delGenericDict(file,dictItems):
#    cartola=cartolaLoad(file)
#    cartola=Cut(cartola)
    if len(dictFields)>1:
        dictItems='.'.join(dictFields)
#        print(dictItems)
    else:
        dictItems=dictFields[0]
    try:
        del scalplCut[dictItems]
        print('Deleted field: "%s"' %dictItems)
    except:
        print('There was no field "%s" to be deleted' %dictItems)