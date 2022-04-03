"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'arp -a' | Out-File -FilePath $args[0] -Append