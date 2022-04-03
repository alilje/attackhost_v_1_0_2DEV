"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'netsh advfirewall firewall show rule name=all' | Out-File -FilePath $args[0] -Append

 