'''
getCurrentWorkDirectory()
checkingIfExists()
creatingDirectory(path,*args)
creatingSubDirectory(path,*args)
'''

import os
import shutil
    
# =============================================================================
# checkingIfExistsFile(*args)
# If checking the file at work directory, give only the name of the file with 
#    the extention (ex.: something.csv, something.doc, something.py)
# Elif checking for a file in another work directory, two options are available:
#    1) give the entire path (ex. 'C:\Users\Documents\something.doc')
#    2) give the path and the file name in two parts (ex.: 'C:\Users\Documents',
#       'something.doc') - the script will join both
# =============================================================================
def checkingIfExistsFile(*args):
    if len(args)==3:
        if os.path.isfile(os.path.join(args[0],args[1],args[2])):
            print('File "%s" exists' %os.path.join(args[0],args[1],args[2]))
            return True
        else:
            print('File "%s" DOES NOT exist' %os.path.join(args[0],args[1],args[2]))
            return False
    if len(args)==2:
        if os.path.isfile(os.path.join(args[0],args[1])):
            print('File "%s" exists' %os.path.join(args[0],args[1]))
            return True
        else:
            print('File "%s" DOES NOT exist' %os.path.join(args[0],args[1]))
            return False
    else:
        if os.path.isfile(args[0]):
            print('File "%s" exists' %args[0])
            return True
        else:
            print('File "%s" DOES NOT exist' %os.path.join(args[0]))
            return False

def deletingFile(path,*args):
    if len(args)>1: #to delete many files
        for item in args:
            os.remove(os.path.join(path,item))
            print('File %s was deleted' %item)
    elif len(args)==1: #to delete a single file
        os.remove(os.path.join(path,args[0]))
        print('File %s was deleted' %args[0])
    else: #to delete a whole path
        os.remove(path)
        print('File %s was deleted' %path)
        
def creatingFile(replace=False,*args):
    print('args',args)
# =============================================================================
# This function receives 1, 2 or 3 arguments for filePath. If one argument,
# then it is understood that the whole file path (with path, file name and 
# extention) was given. If two or three arguments were passed, than it will be 
# joined. The options could be: path and file name with extention; filePath and
# extention; or path, file name and extention.
# Also, this function receives one argument to determine if an existent file
# will be replaced by a new one.
# The file will be created, by default, as written ('w')
# =============================================================================
    if len(args)==3:
        print('args3')
        filePath=os.path.join(args[0],args[1],args[2])
    elif len(args)==2:
        print('args2')
        filePath=os.path.join(args[0],args[1])
    else:
        print('args0')
        filePath=args[0]
#    print(filePath)
    if replace==True:
        try:
            deletingFile(filePath)
            print('File %s is going to be replaced' %filePath)
        except:
            pass
    if checkingIfExistsFile(filePath)==False:
        fileNew=open(filePath,'w')
        fileNew.close()
        print('File %s was created\n' %filePath)
    else:
        print('File %s already exists\n' %filePath)
    
        
