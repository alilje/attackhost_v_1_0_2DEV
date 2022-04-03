"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c '.\powershell\external\AdFind.exe -f (objectcategory=computer)' | Out-File -FilePath $args[0] -Append
