'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'net user guest /active:yes' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net user guest Password123!' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net localgroup Administrators guest /add' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net localgroup "Remote Desktop Users" guest /add' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg add "hklm\system\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg add "hklm\system\CurrentControlSet\Control\Terminal Server" /v "AllowTSConnections" /t REG_DWORD /d 0x1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net user guest /active:no >nul 2>&1' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net localgroup Administrators guest /delete >nul 2>&1' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net localgroup "Remote Desktop Users" guest /delete >nul 2>&1' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'if 0 NEQ 1 (echo Note: set remove_rdp_access_during_cleanup input argument to disable RDP access during cleanup)' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'if 0 EQU 1 (reg delete "hklm\system\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /f >nul 2>&1)' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'if 0 EQU 1 (reg delete "hklm\system\CurrentControlSet\Control\Terminal Server" /v "AllowTSConnections" /f >nul 2>&1)' | Out-File -FilePath $args[0] -Append