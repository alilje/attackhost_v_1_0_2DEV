'***********T1112_3---Modify Registry---Modify registry to store logon credentials**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 0 /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
