@echo off
setlocal enabledelayedexpansion enableextensions

:: --- Diplay ---

:setShortcut
SET "newShortcut=unset"
CLS
ECHO.--- CHANGE KEYBOARD SHORTCUT ---  
ECHO.
ECHO. Enter your new shortcut
ECHO.
ECHO. The following codes are available:
ECHO.  . CTRL
ECHO.  . ALT
ECHO.  . SHIFT
ECHO.  . F1,F2 - F12
ECHO.  . NUMPAD0,NUMPAD1 - NUMPAD9
ECHO.  . 0,1 - 9 (Requires to also have CTRL+ALT)
ECHO.  . A,B - Z (Requires to also have CTRL+ALT)
ECHO. 
ECHO. Enter a "+" character between each code:
ECHO. Example: CTRL+ALT+P or CTRL+NUMPAD0
ECHO.
ECHO. z : go back
ECHO.
SET /p newShortcut=...

:: --- Sanitize user entry ---

SET compareOp="%newShortcut:"=%"
Set newShortcut="%newShortcut:"=%"
Setlocal EnableDelayedExpansion
For %%I In (^| ^& ^< ^> ^^ + ^( ^) \ / . @ # $ { } [ ] ' : ` ^%% ^") Do Set newShortcut=!newShortcut:%%I=!
:: Now remove any !
SetLocal DisableDelayedExpansion
Set newShortcut="%newShortcut:!=%"
EndLocal&Set newShortcut=%newShortcut:~1,-1%
:_parse
Set _Flag1=
For /F "Tokens=1* Delims=~=*;,?" %%J In ('Echo !newShortcut!') Do (
	Set newShortcut=%%J%%K
	Set _Flag1=%%J
	Set _Flag2=%%K
)
If NOT "%_Flag2%"=="" Goto _parse
If Not Defined _Flag1 GOTO deny
EndLocal&Set newShortcut=%newShortcut%
IF NOT %compareOp%=="%newShortcut%" echo. deny
echo. "%compareOp%"
echo. "%newShortcut%"
IF "%newShortcut%"==z GOTO :eof
IF NOT "%newShortcut%"==unset GOTO checkShortcut
GOTO setShortcut


:checkShortcut

echo. var: %newShortcut%
FOR /F "tokens=1,2,3,4 delims=+" %%i IN (%newShortcut%) DO (
	IF NOT DEFINED %%i GOTO deny 
	FOR %%a IN (%%i %%j %%k %%l) DO (
		SET "test="
		FOR %%I IN (CTRL ALT SHIFT F1 F2 F3 F4 F5 F6 F7 F8 F9 F0 NUMPAD1 NUMPAD2 NUMPAD3 NUMPAD4 NUMPAD5 NUMPAD6 NUMPAD7 NUMPAD8 NUMPAD9 NUMPAD0 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z) DO (
			IF %%a==%%I SET "test=1"
		)
		IF DEFINED test (ECHO. success) ELSE (GOTO deny)
	)
)
PAUSE
GOTO setShortcut

:deny
ECHO. Invalid combination
ECHO.
PAUSE
GOTO setShortcut
	