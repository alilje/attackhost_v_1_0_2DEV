"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net user' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'dir c:\Users\' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'cmdkey.exe /list' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net localgroup "Users"' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net localgroup' | Out-File -FilePath $args[0] -Append
