'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'schtasks.exe /Change /TN "\Microsoft\Windows\SystemRestore\SR" /disable' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'schtasks.exe /Change /TN "\Microsoft\Windows\SystemRestore\SR" /enable >nul 2>&1' |  Out-File -FilePath $args[0] -Append
