'***********T1569.002 #1-- Service Execution--Execute a Command as a Service**********'| Out-File -FilePath $args[0]
cmd.exe /c 'sc.exe create ARTService binPath= "%COMSPEC% /c powershell.exe -nop -w hidden -command New-Item -ItemType File C:\art-marker.txt"' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'sc.exe start ARTService' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'c.exe delete ARTService' | Out-File -FilePath $args[0] -Append