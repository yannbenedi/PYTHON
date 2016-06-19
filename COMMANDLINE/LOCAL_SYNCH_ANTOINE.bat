@echo off
title LocalSync - copying local BG files to the server
setlocal enabledelayedexpansion
color 81

:: --------------------------------------------------------------------------
IF NOT DEFINED GUMBALL_LOCAL GOTO abort
SET "exclusionList=T:\Team\01_RESOURCES\productivity\WIP\autosync_local\Exclusion_List.txt"

echo. 
echo. --------------------------------------------
echo.
echo.

:: only lists episodes that come after the Oracle
FOR /F %%i IN ('dir /a:d /b "%GUMBALL_LOCAL%\GB3*"') DO (
	FOR /F %%a IN ('TYPE "%GUMBALL_LOCAL%\LocalSync\Episode_list.txt"') DO (
		IF "%%a"=="%%i" (
			echo. %%i
			echo.
			IF EXIST "T:\Team\Season 3\%%i" (
				xcopy /s /c /d /e /i /r /y /z /v /EXCLUDE:%exclusionList% "%GUMBALL_LOCAL%\%%i" "T:\Team\Season 3\%%i\06_BACKGROUND\01_WIP\01_SCENES"
			) ELSE (echo. invalide episode name)
			echo.
			echo.
		)
	)
) 

echo. --------------------------------------------
echo. --------------------------------------------
echo.
echo.
echo.
echo. Finished copying %date%
echo.
echo.
echo.

pause
endlocal
exit /b

:: --------------------------------------------------------------------------

:abort
CLS
echo.
echo.
echo. Could not find local folder, please re-install script.
echo. 
echo.
pause
endlocal
exit /b
