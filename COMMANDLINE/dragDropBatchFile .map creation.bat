:convertfile
@IF %1 == "" goto END
imf_copy -r -p %1 "%~d1%~p1%~n1.map"
@SHIFT
@GOTO convertfile
:end
@ECHO.
@ECHO Done !
@pause