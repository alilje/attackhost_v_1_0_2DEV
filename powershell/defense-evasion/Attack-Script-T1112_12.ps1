'***********T1112_12---Modify Registry---Disable Windows Notification Center**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg add HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer /v DisableNotificationCenter /t REG_DWORD /d 1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer /v DisableNotificationCenter /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
