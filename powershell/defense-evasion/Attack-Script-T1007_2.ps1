"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net.exe start' | Out-File -FilePath $args[0] -Append