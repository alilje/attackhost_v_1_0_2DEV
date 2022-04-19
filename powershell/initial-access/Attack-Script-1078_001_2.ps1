'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'net user guest /active:yes' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net user guest /active:no' | Out-File -FilePath $args[0] -Append
