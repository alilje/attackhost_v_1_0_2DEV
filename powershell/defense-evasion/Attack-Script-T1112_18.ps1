'***********T1112_18---Modify Registry---Activate Windows NoRun Group Policy Feature**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoRun /t REG_DWORD /d 1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoRun /f' |  Out-File -FilePath $args[0] -Append
