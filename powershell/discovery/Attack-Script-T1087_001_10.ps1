"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'query user' | Out-File -FilePath $args[0] -Append
