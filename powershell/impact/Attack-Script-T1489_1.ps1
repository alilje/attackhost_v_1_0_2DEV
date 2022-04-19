'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'sc.exe stop spooler' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'sc.exe start spooler >nul 2>&1'  |  Out-File -FilePath $args[0] -Append