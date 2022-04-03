"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net localgroup' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net localgroup "Administrators' | Out-File -FilePath $args[0] -Append