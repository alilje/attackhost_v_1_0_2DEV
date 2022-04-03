'*********** Cleanup T1112_1---Modify Registry---Modify Registry of Current User Profile - cmd**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v HideFileExt /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
