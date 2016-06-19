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


FOR /F %%i IN ('DIR /b /a:d "%userprofile%\Desktop\*local*"') DO (
	SET "!locations!=%userprofile%\Desktop\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F %%i IN ('DIR /b /a:d "%userprofile%\Desktop\*gumball*"') DO (
	SET "!locations!=%userprofile%\Desktop\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F %%i IN ('DIR /b /a:d "%userprofile%\Desktop\*backup*"') DO (
	SET "!locations!=%userprofile%\Desktop\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F %%i IN ('DIR /b /a:d "%userprofile%\Documents\*local*"') DO (
	SET "!locations!=%userprofile%\Documents\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F %%i IN ('DIR /b /a:d "%userprofile%\Documents\*gumball*"') DO (
	SET "!locations!=%userprofile%\Documents\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F %%i IN ('DIR /b /a:d "%userprofile%\Documents\*backup*"') DO (
	SET "!locations!=%userprofile%\Documents\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F %%i IN ('DIR /b /a:d "C:\*local*"') DO (
	SET "!locations!=C:\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F %%i IN ('DIR /b /a:d "C:\*gumball*"') DO (
	SET "!locations!=C:\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
FOR /F %%i IN ('DIR /b /a:d "C:\*backup*"') DO (
	SET "!locations!=C:\%%i"
	SET "count=!count! !locations!"
	SET /a locations+=1
)
SET "!locations!=%userprofile%\Documents\GUMBALL_LOCAL"
SET "count=%count% %locations%"

:: ================= User interface =================

:interface
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

SET /p local_path=...
IF NOT DEFINED local_path GOTO interface

:: ================ write env variable ================

FOR %%A IN (%count%) DO (
	IF "%local_path%"=="%%A" SET "local_path=!%%A!"
)
SETX GUMBALL_LOCAL %local_path%

:: ================ End Menu ================

echo.
echo.-------------------------------------------------
echo.-------------------------------------------------
echo.
echo. Installation finished!
echo.
pause
endlocal
exit /b