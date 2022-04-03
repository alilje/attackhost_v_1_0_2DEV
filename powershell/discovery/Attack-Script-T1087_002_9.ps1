"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net user administrator /domain'	|  Out-File -FilePath $args[0] -Append
