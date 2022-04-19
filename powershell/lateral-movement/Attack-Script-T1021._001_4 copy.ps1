'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'nreg add "HKLM\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber /t REG_DWORD /d 4389 -f'  |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'netsh advfirewall firewall add rule name="RDPPORTLatest-TCP-In" dir=in action=allow protocol=TCP localport=4389'  |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg add "HKLM\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber /t REG_DWORD /d 3389 -f >nul 2>&1'  |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'netsh advfirewall firewall delete rule name="RDPPORTLatest-TCP-In" >nul 2>&1'  |  Out-File -FilePath $args[0] -Append