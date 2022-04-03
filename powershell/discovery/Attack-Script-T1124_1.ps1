"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net time \\127.0.0.1'| Out-File -FilePath $args[0] -Append
cmd.exe /c 'w32tm /tz' | Out-File -FilePath $args[0] -Append

