'***********T1552_004_1---Private Keys---Private Keys**********'| Out-File -FilePath $args[0]
cmd.exe /c 'dir c:\ /b /s .key | findstr /e .key' |  Out-File -FilePath $args[0] -Append
