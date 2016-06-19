@echo off
title Backup Installer
setlocal enabledelayedexpansion

:: ================ install SuperCopier API ================

IF NOT EXIST "%userprofile%\Documents\supercopier" (
	MKDIR "%userprofile%\Documents\supercopier"
	COPY /y "T:\Team\01_RESOURCES\supercopier\supercopier2API\SC2Integration.exe" "%userprofile%\Documents\supercopier\SC2Integration.exe"
)

:: ================ Find Existing Local backups ===============

:: This part cycles throughs C:\, My Documents and Desktop to find folders containing the words "gumball", "local" and "backup".
:: The "locations" variable iterates every time a folder is found.
:: Each folder found is written to a new variable thats uses %locations% as a name: %1%, %2%, %3% etc.
:: The "count" variable stores a list of all variable used: "1 2 3".
SET /a locations=1
SET "count="

FOR /F "tokens=*" %%i IN ('DIR /b /a:d "%userprofile%\Desktop\*local*"') DO (
	SET "!locations!=%userprofile%\Desktop\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F "tokens=*" %%i IN ('DIR /b /a:d "%userprofile%\Desktop\*gumball*"') DO (
	SET "!locations!=%userprofile%\Desktop\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F "tokens=*" %%i IN ('DIR /b /a:d "%userprofile%\Desktop\*backup*"') DO (
	SET "!locations!=%userprofile%\Desktop\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F "tokens=*" %%i IN ('DIR /b /a:d "%userprofile%\Documents\*local*"') DO (
	SET "!locations!=%userprofile%\Documents\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F "tokens=*" %%i IN ('DIR /b /a:d "%userprofile%\Documents\*gumball*"') DO (
	SET "!locations!=%userprofile%\Documents\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F "tokens=*" %%i IN ('DIR /b /a:d "%userprofile%\Documents\*backup*"') DO (
	SET "!locations!=%userprofile%\Documents\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F "tokens=*" %%i IN ('DIR /b /a:d "C:\*local*"') DO (
	SET "!locations!=C:\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F "tokens=*" %%i IN ('DIR /b /a:d "C:\*gumball*"') DO (
	SET "!locations!=C:\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F "tokens=*" %%i IN ('DIR /b /a:d "C:\*backup*"') DO (
	SET "!locations!=C:\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
SET "!locations!=%userprofile%\Documents\GUMBALL_LOCAL"
SET "count=!count! !locations!"
SET "display_count=%count:~0,-2%"

:: ================= User interface =================

:overwrite
IF DEFINED GUMBALL_LOCAL (
	CLS
	echo.
	echo.
	echo.
	echo.
	echo.   Local folder already defined [%GUMBALL_LOCAL%]
	echo.   
	echo.   Do you want to keep it? y/n
	echo.
	echo.
	SET /p overwrite=...
	FOR %%A IN (y yes o oui) DO (
		IF "!overwrite!"=="%%A" (
			SET "local_path=%GUMBALL_LOCAL%"
			GOTO installation
		)
	)
	FOR %%A IN (n no non) DO (IF "!overwrite!"=="%%A" (GOTO interface))
	GOTO overwrite
)

:interface
CLS
ECHO.
ECHO.
ECHO.  Please set your local backup path.
ECHO.
ECHO.
FOR %%A IN (%display_count%) DO (
	ECHO.   %%A:  !%%A!
)
ECHO.   %locations%:  !%locations%! ... (suggestion)
ECHO.
ECHO.   Or click and drag your local backup folder on this window
ECHO.
IF DEFINED %failed_sanity% (echo. invalid input) ELSE (ECHO.)

SET /p local_path=...
IF NOT DEFINED local_path GOTO interface

FOR %%A IN (%count%) DO (
	IF "%local_path%"=="%%A" SET "local_path=!%%A!"
)

::sanity check
SET "failed_sanity="
FOR /f "tokens=1 delims=\" %%A IN ('echo.%local_path%') DO (
	IF NOT "C:"=="%%A" (
		SET "failed_sanity=1"
		GOTO interface
	)
)

SETX GUMBALL_LOCAL "%local_path%"

:: ================ installation ================

:installation
xcopy /c /q /r /y "T:\Team\01_RESOURCES\productivity\WIP\AutoSync_local_master.bat" "%local_path%\LocalSync\"
xcopy /c /q /r /y "T:\Team\01_RESOURCES\productivity\WIP\autosync_local\Episode_List.txt" "%local_path%\LocalSync\"

::create shorcut
cscript "T:\Team\01_RESOURCES\productivity\configs\shortcut_nohotkey.vbs" "%userprofile%\Desktop\LocalSync.lnk" "%local_path%\LocalSync\AutoSync_local_master.bat" "%userprofile%\Desktop\"

:: ================ End Menu ================

CLS
echo.
echo.-------------------------------------------------
echo.-------------------------------------------------
echo.
echo.
echo.
echo.
echo. Installation succesful!
echo. 
echo. Launch the sync with your desktop shortcut.
echo.
echo.
echo.
echo.
echo.-------------------------------------------------
echo.-------------------------------------------------
echo.
pause
endlocal
exit /b