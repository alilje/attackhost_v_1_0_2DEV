'***********T1119_4---Recon information for export with Command Prompt**********'| Out-File -FilePath $args[0]
cmd.exe /c 'sc query type=service' |  Out-File -FilePath $args[0] -Append 
cmd.exe /c 'doskey /history' |  Out-File -FilePath $args[0] -Append 
cmd.exe /c 'wmic process list' |  Out-File -FilePath $args[0] -Append 
