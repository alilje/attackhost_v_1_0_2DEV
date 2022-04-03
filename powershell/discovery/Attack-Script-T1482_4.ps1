"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c '.\powershell\external\AdFind.exe -f (objectcategory=organizationalUnit)' | Out-File -FilePath $args[0] -Append
