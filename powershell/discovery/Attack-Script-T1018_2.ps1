"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net group "Domain Computers" /domain'| Out-File -FilePath $args[0] -Append
