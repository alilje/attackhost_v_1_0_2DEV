'***********T1112_7---Modify Registry---BlackByte Ransomware Registry Changes - CMD**********'| Out-File -FilePath $args[0]
cmd.exe /c 'cmd.exe /c reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'cmd.exe /c reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLinkedConnections /t REG_DWORD /d 1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'cmd.exe /c reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ /v LocalAccountTokenFilterPolicy /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ /v EnableLinkedConnections /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKLM\SYSTEM\CurrentControlSet\Control\FileSystem\ /v LongPathsEnabled /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
