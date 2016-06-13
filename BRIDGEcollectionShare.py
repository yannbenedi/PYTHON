import Tkinter,tkFileDialog
import os
import shutil
import time
import sys
import tkMessageBox


"""
Update for Gumball server
Path Local and server
Add to the Bg team script
Make update automated every day
"""

print "\n--- GUMBALL BG ---"
print "\n--- BRIDGE SHARE / UPDATE COLLECTIONS --- \n"
print "This script will update your local Bridge Collection from the Server"
print " or enables you to export your Collections to the Server"
print " Created for Bridge 6"

#  PATHS
user = os.getenv('username')
clear = lambda: os.system('cls')
readmeInfo = "T:\\Team\\01_RESOURCES\\BRIDGE\\SharedCollection\\README.txt"
localPath= "C:\\Users\\" + user + "\\AppData\\Roaming\\Adobe\\Bridge CS6\\Collections" 
serverPath= "T:\\Team\\01_RESOURCES\\BRIDGE\\SharedCollection"
collectionList =[]


def folderUpdate():
    """
    ask user for Local or Server update
    """

    msg = '\n L :UPDATE LOCAL COLLECTIONS \n S: EXPORT LOCAL COLLECTION(S) TO THE SERVER \n I : INFO \n'
    userResult = raw_input(msg)
    userResultUpper = userResult.upper()
    print userResultUpper
    return userResultUpper


def copyServer():
    """
    Select collections from your Local folder to be exported to the Server
    """

    root = Tkinter.Tk()
    collection = tkFileDialog.askopenfilenames(parent=root,title='Pick the collection(s) your want to export to the SERVER', initialdir= localPath )
    userList = root.tk.splitlist(collection)


    for file in userList:
        shutil.copy(file,serverPath)


def copylocal():
    """
    Copy all the collections in the Server in your Local folder
    :return:
    """

    for file in os.listdir(serverPath):
        if file.endswith(".filelist") :
            collectionList.append(file)
            selectedFullFile = os.path.join(serverPath, file)
            shutil.copy(selectedFullFile,localPath)


userResult = folderUpdate()

if userResult == "S" :
    copyServer()
elif userResult == "L" :
    copylocal()
elif userResult == "I" :
    clear()
    with open(readmeInfo) as f:
       print f.read()
       time.sleep(100)
