'***********T1059.002 #2--Windows Management Instrumentation--WMI Reconnaissance List Remote Services**********'| Out-File -FilePath $args[0]
cmd.exe /c 'wmic /node:"127.0.0.1" service where (caption like "%SPOOLER%")' | Out-File -FilePath $args[0] -Append
