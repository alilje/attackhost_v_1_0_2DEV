'***********T1059.002 #2-- Windows Management Instrumentation--WMI Reconnaissance Processes.**********'| Out-File -FilePath $args[0]
cmd.exe /c 'wmic process get caption,executablepath,commandline /format:csv' | Out-File -FilePath $args[0] -Append
