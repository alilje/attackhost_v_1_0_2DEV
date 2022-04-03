"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net localgroup' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net group /domain' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net group "domain admins" /domain' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net group "enterprise admins" /domain' | Out-File -FilePath $args[0] -Append





