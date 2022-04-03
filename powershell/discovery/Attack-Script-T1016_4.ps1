"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'ipconfig /all'| Out-File -FilePath $args[0] -Append
cmd.exe /c 'net config workstation'| Out-File -FilePath $args[0] -Append
cmd.exe /c 'net view /all /domain'| Out-File -FilePath $args[0] -Append
cmd.exe /c 'nltest /domain_trusts' | Out-File -FilePath $args[0] -Append

 