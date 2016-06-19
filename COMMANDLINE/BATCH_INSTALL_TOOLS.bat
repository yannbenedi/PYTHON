@echo off
title RED9
color 81

ECHO.  -- INSTALL RED9 --
ECHO.  !! Check if you already have a "userSetup.py" in your scripts folder !!
explorer %UserProfile%\Documents\maya\2012-x64\scripts

cls
set /p UserSetup= Do you already have a "userSetup.py"? Yes or No :...
IF %UserSetup%== Y GOTO YES
IF %UserSetup%== N GOTO No

:YES
cls

ECHO. COPY ALL THE CONTENT OF THAT FILE AND CLOSE IT
notepad T:\Team\03_STAFF\YannB_sever\INSTALL_TMP\APPEND_userSetup.txt
cls
ECHO. PASTE IN AT THE END OF YOUR "userSetup.py"
notepad %UserProfile%\Documents\maya\2012-x64\scripts\userSetup.py
GOTO Copy

:No
cls

ECHO. COPY userSetup.py
XCOPY T:\Team\03_STAFF\YannB_sever\RED9\Red9_Release1.40\installer\userSetup.py %UserProfile%\Documents\maya\2012-x64\scripts /e /i /y

:Copy
cls

ECHO. --- COPY RED9 ---
XCOPY T:\Team\03_STAFF\YannB_sever\RED9\Red9_Release1.40\Red9\* %UserProfile%\Documents\maya\2012-x64\scripts\Red9 /e /i /y
cls
ECHO. You'll have to append the userSetup.py
ECHO. Look for that line :
ECHO. sys.path.append('O:\Animation\Red9_Release')
ECHO. And change it so that it correspond to your path
ECHO. example on my computer
ECHO. sys.path.append('C:\Users\ybenedi.TURNER\Documents\maya\2012-x64\scripts\Red9')
ECHO. Save the file
notepad %UserProfile%\Documents\maya\2012-x64\scripts\userSetup.py
cls
ECHO. UPDATE THE BG SHELF
CALL T:\Team\01_RESOURCES\MAYA\__INSTALL_MAYA_ENV_AND_SHELFS_background.bat
cls
ECHO. THE INSTALLATION IS DONE
ECHO. THE SCENE NOTE WILL BE IN YOUR BACKGROUND SELF
pause

