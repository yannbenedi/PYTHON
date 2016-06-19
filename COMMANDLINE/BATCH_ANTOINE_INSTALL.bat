@echo off
title Folders Installer &color 81
setlocal enabledelayedexpansion

:: ================= folders installer v03 =================

REM delete old bat file
FOR /F "delims=" %%i IN ('DIR /b /a:-d "%userprofile%\Desktop\Folders*.bat"') DO (
	del /q "%userprofile%\Desktop\%%i"
)
REM delete old shortcut
FOR /F "delims=" %%i IN ('DIR /b /a:-d "%userprofile%\Desktop\Folders*.lnk"') DO (
	REM unset shortcut before deleting to prevent windows bug
	cscript "T:\Team\01_RESOURCES\productivity\configs\remove_shortcut.vbs" "%userprofile%\Desktop\%%i"
	del /q "%userprofile%\Desktop\%%i"
)

REM copy new client from server
xcopy /y /Q "T:\Team\01_RESOURCES\productivity\WIP\FoldersClient_master.bat" "%userprofile%\desktop\" &ECHO. working
:wait
IF EXIST %userprofile%\desktop\FoldersClient_master.bat (RENAME "%userprofile%\desktop\FoldersClient_master.bat" "Folders_client.bat") ELSE (GOTO wait)
REM run vbs script to create a shorcut with a hotkey
cscript "T:\Team\01_RESOURCES\productivity\configs\shortcut.vbs" "%userprofile%\Desktop\Folders_client.lnk" "%userprofile%\Desktop\Folders_client.bat" "%userprofile%\Desktop\"

:: ================ Find Local backup ===============

:: This part cycles throughs C:\, My Documents and Desktop to find folders containing the words "gumball", "local" and "backup".
:: The "locations" variable iterates every time a folder is found.
:: Each folder found is written to a new variable thats uses %locations% as a name: %1%, %2%, %3% etc.
:: The "count" variable stores a list of all variable used: "1 2 3".
SET /a locations=1
SET "count="
FOR %%a IN (%userprofile%\Desktop\ %userprofile%\Documents\ C:\) DO (
	FOR %%b IN (local gumball backup %username%) DO (
		FOR /F %%i IN ('DIR /b /a:d "%%a*%%b*"') DO (
			SET "!locations!=%%a%%i"
			SET "count=!count! !locations!"
			SET /a locations+=1
		)
	)
)
SET "!locations!=%userprofile%\Documents\GUMBALL_LOCAL"
SET "count=%count% %locations%"

:: ================= User interface =================

CLS
ECHO.
ECHO.
ECHO.  Please set your local backup path.
ECHO.
ECHO.
FOR %%A IN (%count%) DO (
	ECHO.    %%A:  !%%A!
)
ECHO.
ECHO.    Or just type the adress instead
ECHO.
ECHO.

SET /p Override=...
IF NOT DEFINED Override GOTO launch

:: ================= Extra operations =================

:overrideLocal
REM use listed folder if a number has been input, otherwise treat input as a path itself.
FOR %%A IN (%count%) DO (
	IF "%Override%"=="%%A" SET "Override=!%%A!"
)
REM create temp txt file to write the modified client
SET "tempFile=%userprofile%\Desktop\tempFile.txt"
REM make sure an old one hasn't stayed behind
IF EXIST "%tempFile%" del "%tempFile%"

setlocal enabledelayedexpansion
REM read each line of the default client, replace one line if found, output to temp text file.
FOR /F "tokens=*" %%i IN ('TYPE "%userprofile%\Desktop\Folders_client.bat"') DO (
		SET tempvar=%%i
		SET "comparator=SET override=false"
		SET "newline=SET override=%Override%"
		IF !tempvar!==!comparator! ECHO.!newline!>> "%tempFile%"
		IF NOT !tempvar!==!comparator! ECHO.%%i>> "%tempFile%"
)
endlocal

REM overwrite the default client with the new updated one
copy /y "%tempFile%" "%userprofile%\Desktop\Folders_client.bat"
del "%TempFile%"

:: ================= START PROGRAM =================

:launch
endlocal
CALL "%userprofile%\Desktop\Folders_client.bat"