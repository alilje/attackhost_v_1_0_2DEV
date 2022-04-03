"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c "net user /domain"	|  Out-File -FilePath $args[0] -Append
cmd.exe /c "net group /domain"   |  Out-File -FilePath $args[0] -Append
