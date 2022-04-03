"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c ".\powershell\external\AdFind.exe -sc admincountdmp" |  Out-File -FilePath $args[0] -Append

