"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net accounts /domain' | Out-File -FilePath $args[0] -Append