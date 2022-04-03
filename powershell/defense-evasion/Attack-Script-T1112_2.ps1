'***********T1112_2---Modify Registry---Modify Registry of Local Machine - cmd**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run /t REG_EXPAND_SZ /v SecurityHealth /d calc.exe /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run /v SecurityHealth /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
