'*************************************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'reg  add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowInfoTip /t REG_DWORD /d 0 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg  add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowCompColor /t REG_DWORD /d 0 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowInfoTip /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowCompColor /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append