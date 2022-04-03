'***********T1552_002_2---Enumeration for PuTTY Credentials in Registry**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg query HKCU\Software\SimonTatham\PuTTY\Sessions /t REG_SZ /s' |  Out-File -FilePath $args[0] -Append
