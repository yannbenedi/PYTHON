@echo off
:setUser
FOR /F "delims== tokens=2" %%i IN ('SET user') DO (
SET "user=%%i"
)
SET override=C:\YANNB_Local\GUMBALL
IF NOT %override%==false (SET localPath=%Override%) ELSE (SET localPath=%user%\Documents\GUMBALL_LOCAL)
CALL "T:\Team\01_RESOURCES\productivity\WIP\Folders_master.bat"
EXIT