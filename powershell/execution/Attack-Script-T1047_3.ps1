'***********T1059.002 #2--Windows Management Instrumentation--WMI Reconnaissance Software**********'| Out-File -FilePath $args[0]
cmd.exe /c 'wmic qfe get description,installedOn /format:csv' | Out-File -FilePath $args[0] -Append
