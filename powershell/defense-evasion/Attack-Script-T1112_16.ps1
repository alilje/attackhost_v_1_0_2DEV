'***********T1112_16---Modify Registry---Disable Windows Lock Workstation Feature**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableLockWorkstation /t REG_DWORD /d 1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableLockWorkstation /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
