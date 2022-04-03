"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net share' | Out-File -FilePath $args[0] -Append