'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'net user art-test /add' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net user art-test Password123!' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net localgroup administrators art-test /add' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net localgroup administrators art-test /delete >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net user art-test /delete >nul 2>&1' |  Out-File -FilePath $args[0] -Append