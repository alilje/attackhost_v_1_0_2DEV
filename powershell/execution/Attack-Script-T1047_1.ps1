'***********T1047 #1-- Windows Management Instrumentation--WMI Reconsissance Users.**********'| Out-File -FilePath $args[0]
cmd.exe /c 'wmic useraccount get /ALL /format:csv' | Out-File -FilePath $args[0] -Append
