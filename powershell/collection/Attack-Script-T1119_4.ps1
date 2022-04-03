'***********T1119_4---Automated Collection---Recon information for export with Command Prompt**********'| Out-File -FilePath $args[0]
cmd.exe /c 'sc query type=service > T1119_1.txt' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'doskey /history > T1119_2.txt' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'wmic process list > T1119_3.txt' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'tree C:\AtomicRedTeam\atomics > T1119_4.txt' |  Out-File -FilePath $args[0] -Append
