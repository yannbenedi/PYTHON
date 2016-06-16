
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# account with .json
cred = r"C:\Users\yannb\Documents\GitHub\PYTHON\GSPREAD\CREDENTIAL\yannb-b92558a84296.json"
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name( cred , scope)
gc = gspread.authorize(credentials)

# SETUP ----
# sheet
sheetURL = r"https://docs.google.com/spreadsheets/d/1rqB4N-zTZsPiS-RtP4WomDlBPjTlDtpXYrrpInNhFGU/edit#gid=0"
# open sheet
sheet = gc.open_by_url(sheetURL)
#open worksheet
wks = sheet.get_worksheet(0)


def lookFor(search,replace,range):
    """
    search and replace cell value in range
    :param search: value to search
    :param replace: new value
    :param range : 'A1:C6'
    """
    cell_list = wks.range(range)

    for cell in cell_list:
        if cell.value == search:
            cell.value = replace

    # Update in batch
    wks.update_cells(cell_list)

"""
# access range
cell_list = wks.range('A1:B7')

# acces single cell (row, Column)
val = wks.cell(1, 2).value

# update cell
wks.update_acell('B2', "updated")
"""

list_of_lists = wks.get_all_values()
x =(list_of_lists)
listNoHeader = x[1:]
print("list no header :", listNoHeader)
listTemplate = []

# extract and create a .txt ready to be copied to shotgun
for row in listNoHeader:
    if row[2] == "off":
        listTemplate.append(row[0])
        listTemplate.append(row[1])

print ("list template",listTemplate)





