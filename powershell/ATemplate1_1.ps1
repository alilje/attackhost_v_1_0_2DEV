"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'hostname' |  Out-File -FilePath $args[0] -Append


