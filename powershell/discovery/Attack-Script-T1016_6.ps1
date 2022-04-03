"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c '.\powershell\external\AdFind.exe -subnets -f (objectcategory=subnet)' | Out-File -FilePath $args[0] -Append

 
