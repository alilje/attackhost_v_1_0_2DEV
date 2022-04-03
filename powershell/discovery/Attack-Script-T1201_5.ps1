"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net accounts' | Out-File -FilePath $args[0] -Append