'***********T1112_13---Modify Registry---Disable Windows Shutdown Button**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v shutdownwithoutlogon /t REG_DWORD /d 0 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v shutdownwithoutlogon /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
