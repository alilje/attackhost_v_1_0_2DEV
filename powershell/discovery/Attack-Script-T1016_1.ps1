"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'ipconfig /all' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'netsh interface show interface'| Out-File -FilePath $args[0] -Append
cmd.exe /c 'arp -a' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'nbtstat -n' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net config' | Out-File -FilePath $args[0] -Append

 