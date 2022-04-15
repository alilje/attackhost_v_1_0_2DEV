'***********T1027_4---Obfuscated Files or Information---Execution from Compressed File**********'| Out-File -FilePath $args[0]
cmd.exe /c 'util\T1027\T1027.exe' |  Out-File -FilePath $args[0] -Append
timeout /t 5
taskkill /f /im calculator.exe >nul 2>nul