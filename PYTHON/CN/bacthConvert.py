# BrowseFile.py

import os, webbrowser

# Set Local Path

localPath= "D:\\yannb\\WORK\\2014\\SCRIPT\\python\\GB"
filterGumballFolder= "GB"


# User Input

gumballFolders =[]

for folders in os.listdir(localPath):
        if folders.count(filterGumballFolder)== 1:
            gumballFolders.append(folders)
print "gumballFolders: %s" % (gumballFolders)

# User select shot

while True:
    userEpisode = raw_input("Select Episode ")
    userEpisode= userEpisode.upper()
    selectedEpisode = "none"
    for n in gumballFolders:
        fullEpisodeName = n
        EpisodeFound= n[5:]
        condCheckEpisode = n[5:8]
        if len(userEpisode) >= 3 and fullEpisodeName.count(userEpisode)==1:
            selectedEpisode = fullEpisodeName
            print "Selected Episode is %s"% (selectedEpisode)
    if selectedEpisode != "none":
        break
    else:
        print "Type the first three letters of the show or any direct link"


# User select shot
userShot = raw_input("Select Shot ")
shotPrefix = "Sc"
selectedShot = "none"

if len(userShot) == 3:
    selectedShot = shotPrefix + userShot
elif len(userShot) == 2:
    selectedShot = shotPrefix + "0" + userShot
elif len(userShot) == 1:
    selectedShot = shotPrefix + "00" + userShot
else:
    print "Type the number of the shot"
print selectedShot

# Show Actual selection

print "--%s----%s--" %(selectedEpisode,selectedShot)

# Path from Inputs

UserPath = localPath + "\\" + selectedEpisode + "\\" + selectedShot
print UserPath

if os.path.isdir(UserPath):
    print localPath
    os.startfile(UserPath)
else:
    os.makedirs(UserPath)
    os.startfile(UserPath)
