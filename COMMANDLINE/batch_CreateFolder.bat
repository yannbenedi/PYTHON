@echo off
:: Yann Benedi 2015
title Create new BG3D prop folder template
color 81

:: Paths
SET "BG3DpropFolder=T:\Team\00_ASSETS\02_PROPS_LIBRARY\3D_PROPS\BG\"
SET "BG3DfolderTemplate=T:\Team\00_ASSETS\02_PROPS_LIBRARY\3D_PROPS\BG\_ReadMe\CreateFolderTemplate\"

:: Ask for the name of the asset
echo.
echo.  ---------
echo.  Create new BG3D prop folder template
echo.  This script will create a new folder for your asset ready to use
echo.  ---------
echo.
SET /p AssetName="Type the name of your 3D asset you want to create?:"

SET "BG3DpropFolder= %BG3DpropFolder%%AssetName%"

:: Check if props already exist
if not exist %BG3DpropFolder% (
    CALL :StartTemplateCreation
    echo.     Template for %AssetName% created

) else (call:abort "%AssetName% BG3D prop already exist !!" )


:StartTemplateCreation
:: Create folder and template BROKEN
mkdir %BG3DpropFolder%

echo.%BG3DfolderTemplate%
echo.%BG3DpropFolder%

COPY "T:\Team\00_ASSETS\02_PROPS_LIBRARY\3D_PROPS\BG\_ReadMe\CreateFolderTemplate" "%BG3DpropFolder%"

echo.     Script files copied

pause

:abort
echo.
echo.  !
echo.  %1
echo.  !
echo.
pause >nul
exit /b



