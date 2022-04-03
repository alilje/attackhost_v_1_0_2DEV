"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net view /domain' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net view' | Out-File -FilePath $args[0] -Append
 