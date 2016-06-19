#! python3.5
# the python versionis not working, need to be 3
# # C:\Users\yannb\AppData\Local\Programs\Python\Python35-32\python.exe C:/Users/yannb/Documents/GitHub/PYTHON/GSPREAD/gdocTest.py

# yannb for BG
# This script enables the user to get all the briefed task exported in an Excel
# ready to be imported on Shotgun
# The user will have to specify his current episode
# You can them update the Gdoc BG brief status

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import os
from  prompter import yesno

print("TAWOG)
print("BG BRIEF EXPORT TO SHOTGUN\n")

def searchReplace(rangeStart,rangeEnd):
    """
    update the BG brief status in the Gdoc from BRIEFED to SHOTGUN
    :return:
    """
    search = "BRIEFED"
    replace = "SHOTGUN"
    currentSheetRange = "A%s:A%s" % (rangeStart,rangeEnd)
    cell_list = wks.range(currentSheetRange)

    for cell in cell_list:
        print(cell)
        if cell.value == search:
            cell.value = replace

    # Update in batch
    wks.update_cells(cell_list)


###################################################################
# access doc

cred = r"C:\Users\yannb\Documents\GitHub\PYTHON\GSPREAD\CREDENTIAL\yannb-b92558a84296.json"     # license file, CHANGE DESTRINATION
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name( cred , scope)
gc = gspread.authorize(credentials)

# Create file to write data to be copied
# Modify if you add more item to the template
docTemplateHeader = ["id" , "Link" , "Brief" , "Priority Keyshot" , "Bid" , "Assigned To" , "Status" , "Info" , "Asset > 3D"]
sheetURL = r"https://docs.google.com/spreadsheets/d/1rqB4N-zTZsPiS-RtP4WomDlBPjTlDtpXYrrpInNhFGU/edit#gid=0"
sheet = gc.open_by_url(sheetURL)
valueForShotgun = "tmp.csv"                     # csv to get the value to paste in shotgun

###################################################################
# Ask user for which worksheet to extract info
sheetUser = input("Type your episode name as it appears in your Gdoc sheet : \n ")
wks = sheet.worksheet(sheetUser)

listFromDoc = wks.get_all_values()              # all value from doc
rowNumber = len(listFromDoc)                    # return the number of row to know until when we need to extract
separatorHeader = 12                            # where the header starts (13 - 1 as it starts at 0)  CHANGE
x =listFromDoc
listNoHeader = x[separatorHeader:rowNumber]     # ignore the freeze row, header, each row is a list in the list

###################################################################
# Create the CVS from the selected data

with open(valueForShotgun , "w") as scoreFile:                                          # open the CVS
    scoreFileWriter = csv.writer(scoreFile, lineterminator = '\n',dialect='excel')      # linedelminator avoid jumping line inbetween
    scoreFileWriter.writerow(docTemplateHeader)                                         # write the header template first
    for list in listNoHeader:
        listNumItem = len(list)
        listCut = list[4:]                                                              # Discard useless info, start the list from the ID
        taskBriefStatus = list[0]
        if taskBriefStatus == "BRIEFED":                                                # Check if the task is ready to be copied to Shotgun
            if listNumItem != 0:                                                        # just checking the list exists
                scoreFileWriter.writerow(listCut)
scoreFile.close()

os.startfile(valueForShotgun)                                                           # open the csv with the content to copy to shotgun

###################################################################
# Update the Gdoc with the SHOTGUN status
userInput = yesno('Do you want to update your Gdoc %s Brief Status from BRIEFED to SHOTGUN?'%(sheetUser))
if userInput == True:
    searchReplace(separatorHeader +1  , rowNumber )







