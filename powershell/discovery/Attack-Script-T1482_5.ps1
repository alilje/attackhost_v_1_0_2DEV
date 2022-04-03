"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c '.\powershell\external\AdFind.exe -gcb -sc trustdmp' | Out-File -FilePath $args[0] -Append
