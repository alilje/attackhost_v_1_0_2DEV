"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'netstat' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net use' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net sessions' | Out-File -FilePath $args[0] -Append
