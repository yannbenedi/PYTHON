@echo off
title COPY Local BG to Server BG
color 81
:: >> %logfile%   add to log file
set backupcmd=xcopy /s /c /d /e /i /r /y /z /v /f /EXCLUDE:T:\Team\03_STAFF\YannB_sever\Script\LocalToServer\Exclusion_List.txt
:: create a Exclusion list with the name of the folder you want to exclude (eg "wip\")
set logfile=C:\Users\ybenedi.TURNER\Desktop\Log.txt
echo. 
echo. 
echo.    
echo. 
echo. GUMBALL BACKGROUND 
echo. 
echo. COPY Local BG to Server BG 
echo.
echo. --------------------------
echo.

:: -----------    BACKUP EACH EPISODES    ----------------------
%backupcmd% "C:\YANNB_Local\GUMBALL\GB311_Recipe" "T:\Team\Season 3\GB311_Recipe\06_BACKGROUND\01_WIP\01_SCENES" 
echo.     GB311_Recipe DONE! 
echo. 
%backupcmd% "C:\YANNB_Local\GUMBALL\GB312_People" "T:\Team\Season 3\GB312_People\06_BACKGROUND\01_WIP\01_SCENES"
echo. 	  GB312_People DONE! 
echo. 
%backupcmd% "C:\YANNB_Local\GUMBALL\GB310_Vacation" "T:\Team\Season 3\GB310_Vacation\06_BACKGROUND\01_WIP\01_SCENES" 
echo. 	  GB310_Vacation DONE! 
echo. 
%backupcmd% "C:\YANNB_Local\GUMBALL\GB308_Gripes" "T:\Team\Season 3\GB308_Gripes\06_BACKGROUND\01_WIP\01_SCENES" 
echo. 	  GB308_Gripes DONE! 
echo. 
%backupcmd% "C:\YANNB_Local\GUMBALL\GB309_Hole" "T:\Team\Season 3\GB309_Hole\06_BACKGROUND\01_WIP\01_SCENES" 
echo. 	  GB309_Hole DONE! 
echo. 
echo. 
echo. 
echo. Backup completed ! 


echo. --------------------------
pause

