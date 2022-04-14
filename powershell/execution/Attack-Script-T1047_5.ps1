'***********T1059.002 #2--T1059.002 #2--Windows Management Instrumentation--WMI Execute Local Process**********'| Out-File -FilePath $args[0]
cmd.exe /c 'wmic process call create cmd.exe' | Out-File -FilePath $args[0] -Append
