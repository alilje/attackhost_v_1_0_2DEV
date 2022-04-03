'***********T1112_14---Modify Registry---Disable Windows LogOff Button**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoLogOff /t REG_DWORD /d 1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v StartMenuLogOff /t REG_DWORD /d 1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
