'***********T1053.002 #1-- At (Windows)--At.exe Scheduled task**********'| Out-File -FilePath $args[0]
cmd.exe /c 'at 13:20 /interactive cmd' | Out-File -FilePath $args[0] -Append
