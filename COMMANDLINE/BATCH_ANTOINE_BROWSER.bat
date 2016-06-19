@echo off
:: Antoine Perez 2013
SET version=18
title Folders &color 81
setlocal enabledelayedexpansion enableextensions
SET "sga=start Chrome https://turneruk.shotgunstudio.com/page/"
IF NOT DEFINED localpath SET "localpath=%userprofile%\desktop\local"

:: sub-routines are declared at the end of the file

:: ---- EPISODE SELECTION ----------------------------------------------------------------

:setEpisode
SET "shotindex=0" &SET "userEpisode=0" &SET "IntentIndex=0" &SET "userIntent=unset" &CALL :EpisodeMenu
SET /p userEpisode=...

:: if more than one words has been entered, use the first as episode, all the rest as intents.
FOR /f "tokens=1,*" %%i IN ("%userEpisode%") DO (
	SET "userEpisode=%%i"
	IF NOT "%%j"=="" (
		SET "userIntent=%%j"
		CALL:formatIntent
	)
)

:: start by looking for these shortcuts
IF "%userEpisode%"=="sg" (%sga%1505 &EXIT)
IF "%userEpisode%"=="ss" (%sga%search &EXIT)
IF "%userEpisode%"=="wk" (start "Chrome" "http://gumballwiki.turner.com/index.php?title=Main_Page" &EXIT)
IF "%userEpisode%"=="tmp" (explorer "%localPath%\000_TRANSFER" &EXIT)
IF "%userEpisode%"=="help" (CALL:HelpMenu&PAUSE&GOTO setEpisode)
IF "%userEpisode%"=="t" (explorer "%userprofile%\documents\gumball_color_pipeline\user_tools" &EXIT)

:: find user extra-shortcuts.
SET "extraCMD=T:\Team\01_RESOURCES\productivity\configs\user_shorcuts\%username%.bat"
IF EXIST "%extraCMD%" CALL "%extraCMD%"

:: try to match the episode name to season 3 directory list.
FOR /F %%i IN ('dir /a:d /b "T:\Team\Season 3\*%userEpisode%*"') DO (SET "Episode=%%i"&GOTO setIntent)

:: if passed through, try matching to season 1 and 2 reference quicktimes.
FOR %%I IN (1 2) DO (
	SET "refs=T:\Team\01_RESOURCES\03_REFERENCES\Season %%I References Quicktime"
	FOR /F %%i IN ('dir /b "!refs!\*%userEpisode%*"') DO (explorer "!refs!\%%i"&EXIT)
)

:: if the script reaches here: no shortcut, season 3 episode, or reference quicktime has been found with a matching name.
GOTO setEpisode

:: ---- USER INTENT SELECTION -----------------------------------------------------------

:setIntent
:: Erase the intent-list if userIntent has been reset to 'unset'
IF "%userIntent%"=="unset" SET IntentIndex=0

:: Only prompt if valid intent-list doesn't exist.
IF "%IntentIndex%"=="0" (
	CALL :IntentMenu
	SET /p userIntent=...
	CALL:formatIntent
)

:: Start by looking for these shortcuts:
IF "%userIntent%"=="unset" explorer "T:\Team\Season 3\%Episode%\" &EXIT
IF /i "%userIntent%"=="z" GOTO setEpisode
IF /i "%userIntent%"=="x" SET "shotIndex=0"

:: Is shot number hasn't been declared yet, check if any intents requires it.
SET "needshot=0"
IF "%shotIndex%"=="0" (
	FOR /L %%I IN (1,1,%intentIndex%) DO (
		FOR %%b IN (lr la bw 2w 2a 3r 3w lo ss) DO (IF "!intent%%I!"=="%%b" SET needshot=1)
	)
)

:: Intent is required to go further
IF %intentIndex%==0 GOTO setIntent

:: ---- SHOT SELECTION -----------------------------------------------------------

:: If needed, ask for shot number.
:: pass through only if: valid shot number is found OR if input is left blank (open root option).
IF "%needshot%"=="1" (
	SET "userShot=unset"
	CALL :ShotMenu &SET /p userShot=...
	IF "!userShot!"=="z" (SET "userIntent=unset"&GOTO setIntent)
	FOR %%O IN (!userShot!) DO (
		CALL:formatShot %%O,uShot,vcheck2
		IF NOT DEFINED vcheck2 SET /A shotIndex+=1&SET "shot!shotIndex!=!uShot!"
	)
	IF "!shotIndex!"=="0" (IF NOT "!userShot!"=="unset" GOTO setIntent)
)

:: if no shot has been input, force at least one value in the shot array (it's a workaround to get the rest of the script to work)
IF "%shotIndex%"=="0" (SET shotIndex=1&SET shot1=unset)

:: ---- MAIN ACTION LOOP -----------------------------------------------------------

:: launch actions now. returns an error array, and an array for folders that can be created.
CLS
FOR /L %%A IN (1,1,%shotIndex%) DO (
	FOR /L %%I IN (1,1,%intentIndex%) DO (
		SET "error="&CALL:launchAction !Intent%%I!,!shot%%A!,%Episode%
		IF DEFINED error (
			SET /A errorcount+=1&SET "error!errorcount!=!error!"
			IF !intent%%I!==lo (SET /A makecount+=1&SET "make!makecount!=!error!")
		)
	)
)

:: error dialog 
IF %errorcount% GTR 0 (
	echo. &echo. Problems have occured:&echo.
	FOR /L %%a IN (1,1,%errorcount%) DO (echo. &echo. missing .. !error%%a!)
	IF DEFINED make1 (
		echo.&echo. Write anything to confirm the creation of local folders&echo.
		set /p write=...
		IF DEFINED write (	
			FOR /L %%a IN (1,1,%makecount%) DO (mkdir "!make%%a!"&explorer "!make%%a!")
		)
	) ELSE (echo.&echo.&pause)
)

:: if script reaches here, either all actions have been launched or none were entered.
IF "%IntentIndex%"=="0" (GOTO SetIntent) ELSE (endlocal&EXIT /b)

:: ---- ACTION SUB-ROUTINES ----------------------------------------------------------------

:launchAction
:: syntax: %1 is the intent, %2 is the shot number, %3 is the episode
setlocal

:: If shot number has been omitted, format the path to open the root folder instead.
IF "%~2"=="unset" (SET "shotPath=") ELSE (SET "shotPath=Sc%~2")

:: Add file extensions to certain intents (declared in table, intent:extension)
IF NOT "%~2"=="unset" (
	FOR %%i IN (lr:.mov 3r:.mp4 ss:) DO (
		FOR /f "tokens=1,2 delims=:" %%I IN ("%%i") DO (IF "%~1"=="%%I" SET "shotPath=%~2%%J")
	)
)

:: All pathes have to end with a variable only. This opens the root folder when the variable is empty.
SET "ep=T:\Team\Season 3\%~3" &SET "an3d=\08_3D_ANIMATION\01_WIP\" &SET "lo=\05_LAYOUT\"
IF %~1==a (CALL:open "%ep%\00_ANIMATICS\")
IF %~1==l (CALL:findLatest "%ep%%lo%03_REVIEW_EDITS\",mp4)
IF %~1==lr (CALL:open "%ep%%lo%01_WIP\02_RUSHES\%shotPath%")
IF %~1==lw (CALL:open "%ep%%lo%01_WIP\01_SCENES\")
IF %~1==la (CALL:open "%ep%%lo%02_APPROVED\%shotPath%")
IF %~1==lt (CALL:open "%ep%%lo%00_TEMP\")
IF %~1==br (CALL:openBridge "%ep%\06_BACKGROUND\01_WIP\02_REVIEW_JPGS")
IF %~1==bw (CALL:open "%ep%\06_BACKGROUND\01_WIP\01_SCENES\%shotPath%")
IF %~1==2 (CALL:findLatest "%ep%\00_ANIMATICS\",mov,"*2D")
IF %~1==2w (CALL:open "%ep%\07_2D_ANIMATION\00_KEY\01_WIP\01_SCENES\%shotPath%")
IF %~1==2a (CALL:open "%ep%\07_2D_ANIMATION\00_KEY\02_APPROVED\%shotPath%")
IF %~1==3 (CALL:findLatest "%ep%%an3d%03_EDIT\",mov)
IF %~1==3r (CALL:open "%ep%%an3d%02_RUSHES\%shotPath%")
IF %~1==3w (CALL:open "%ep%%an3d%01_SCENES\%shotPath%")
IF %~1==ss (%sga%search?q=%userEpisode%%%20%shotPath%)
IF %~1==lo  (CALL:open "%localPath%\%~3\%shotPath%")
IF %username%==tvburkersroda (
	IF %~1==rushes (START "" "C:/Python27/python.exe" "T:\Team\02_MISC\DEVELOPEMENT\3d_rushes_migration.py" -e %3)
)

:: pass the errors back to the main environement
endlocal&SET "error=%error%"
Exit /b

:: ---- FORMATING SUB-ROUTINES ---------------------------------------------------------------

:formatIntent
:: syntax: CALL:formatIntent
:: Global function: input is always userIntent, output is always %intent#%,%shot#%
:: It slices a string into two arrays of variables (arrays: intents and shots, delimiters: space and dot)
:: the IntentIndex and ShotIndex variables are counts of the number of created variables for each array.
SET IntentIndex=0
SET "userIntent=%userIntent:.= %"
FOR %%a IN (%userIntent%) DO (
	SET "intentisreal=0"&SET "vcheck1=1"	
	FOR %%Q IN (a l lr lw la lt br bw 2 2w 2a 3 3r 3w ss lo loc rushes) DO (IF "%%a"=="%%Q" SET intentisreal=1)
	IF "!intentisreal!"=="0" (
		CALL:formatShot %%a,xxx,vcheck1
		IF NOT DEFINED vcheck1 (
			SET "shot=!xxx!"
			SET /A shotindex+=1
			SET "shot!shotindex!=!xxx!"
		)
	) ELSE (
		SET /A "IntentIndex+=1"
		SET "intent!IntentIndex!=%%a"
		IF "%%a"=="loc" SET "intent!IntentIndex!=lo"
	)
)
EXIT /b

:formatShot
:: Localised function to format numbers and also check their validity.
:: Formating to "000" + optional letter suffix (one letter only).
:: The validity check fills a parameter if result is not a valid shot number. (If vcheck=="" entry is a shot)
:: syntax: CALL:formatShot %input%,output,validity
setlocal
	SET "var=%1"&SET "suffix="
	FOR %%i IN (a b c d e f g h i j k l m o p q r s t u v w x y z) DO (
		IF /i %var:~-1%==%%i (SET "var=%var:~0,-1%" &SET "suffix=%%i")
	)
	IF "%var%"=="" (SET "var=failed") ELSE (SET "var=000%var%")
	SET "nmbr="&for /f "delims=0123456789" %%i in ("%var:~-3%") do set "nmbr=%%i"
	SET "var=%var:~-3%%suffix%"
(endlocal
	SET "%2=%var%"
	SET "%3=%nmbr%"
)&EXIT /b

:: ---- OTHER SUB-ROUTINES ---------------------------------------------------------------

:open
IF EXIST "%~1" (explorer "%~1") ELSE (SET "error=%~1")
EXIT /b

:findLatest
:: syntax: %1 is full path; %2 is file extension, %3 is optional modifier
FOR /F "delims=" %%I IN ('DIR /B /O:-D "%~1%~3*.%~2"') DO (
	START "" "C:\Program Files (x86)\QuickTime\QuickTimePlayer.exe" "%~1%%I"
)&EXIT /b

:openBridge
IF EXIST "%~1" START "" "C:\Program Files\Adobe\Adobe Bridge CS6 (64 Bit)\Bridge.exe" "%~1"
EXIT /b

:: ----- Menu sub-routines ---------------------------------------------------------------

:EpisodeMenu
CLS
ECHO. ----- SELECT AN EPISODE ----- [Folders v%version%]
ECHO.
ECHO. Type at least three letters of an episode name
ECHO.
ECHO. Or one of the following:
ECHO.  . sg : Shotgun home
ECHO.  . ss : Shotgun search
ECHO.  . wk : Gumball Wiki
ECHO.  . A season 1 or 2 full episode name
ECHO.  . help : help
ECHO.
EXIT /b
:IntentMenu
CLS
SET "printshots="
FOR /L %%I IN (1,1,%shotIndex%) DO (SET "printshots=!printShots! Sc!shot%%I!")
ECHO. ----- SELECT AN OPTION ----- ^(The %Episode:~6%%printShots%^)
ECHO.
ECHO. a  : Animatics
ECHO. l  : Layout animatic
ECHO. lr : Layout Rushes
ECHO. lw : Layout WIP
ECHO. la : Layout Approved
ECHO. lt : Layout Temp
ECHO. br : BG Review
ECHO. bw : BG WIP
ECHO. 2  : 2D Key animatic
ECHO. 2w : 2D Key WIP
ECHO. 2a : 2D Key Approved
ECHO. 3  : 3D Animatic
ECHO. 3r : 3D rushes
ECHO. 3w : 3D anm WIP
ECHO. ss : Shotgun search
ECHO.
ECHO. lo : local backup
IF "%shotIndex%"=="0" (ECHO. ###: any shot number) ELSE (ECHO. x  : Clear shot selection)
ECHO.
ECHO. z : Go back 
ECHO.
EXIT /b
:ShotMenu
CLS
SET "printintents="
FOR /L %%I IN (1,1,%IntentIndex%) DO (SET "printintents=!printintents! !intent%%I!")
ECHO. ----- SELECT A SHOT ----- (%Episode:~6% - intents:%printintents%)
ECHO. 
ECHO. Enter one or more shot numbers
ECHO. If empty the root folder will be opened
ECHO. z : Go back
ECHO.
EXIT /b
:HelpMenu
CLS
ECHO. This tool helps you open folders faster, more conveniently.
ECHO.
ECHO. - You can open the script by pressing CTRL + NUMPAD 0.
ECHO. - Leave the intent or shot number empty to open the root folder.
ECHO. - Before episode selection, press tmp to open your local tmp (transfers)
ECHO. - The script can create local folders if they do not already exist.
ECHO.
ECHO. - You can open a quicktime movie of an archived episode by typing it's name.
ECHO.	You need to type it's full name (not just the three first letters)
ECHO.
ECHO. - You can add customized shortcuts by creating a .bat in:
ECHO.   (...) 01_RESOURCES\productivity\configs\user_shortcuts
ECHO.
ECHO. - You can queue intents and shot numbers as you wish.
ECHO.   It will open all intents for all shots specified.
ECHO.   example: fan lr l 3w 103 24 2w
ECHO. 
EXIT /b