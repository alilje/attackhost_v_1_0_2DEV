"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c '.\powershell\external\AdFind.exe -sc dclist' | Out-File -FilePath $args[0] -Append
