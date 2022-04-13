'***********T1053.005 #1-- Scheduled Task--Scheduled Task Startup Script**********'| Out-File -FilePath $args[0]
cmd.exe /c 'schtasks /create /tn "T1053_005_OnLogon" /sc onlogon /tr "cmd.exe /c calc.exe"' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'schtasks /create /tn "T1053_005_OnStartup" /sc onstart /ru system /tr "cmd.exe /c calc.exe"' | Out-File -FilePath $args[0] -Append