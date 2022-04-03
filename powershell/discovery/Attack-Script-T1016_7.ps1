"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c '.\powershell\external\T1016_7\qakbot.bat' | Out-File -FilePath $args[0] -Append

 
