"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net view \\127.0.0.1' | Out-File -FilePath $args[0] -Append
