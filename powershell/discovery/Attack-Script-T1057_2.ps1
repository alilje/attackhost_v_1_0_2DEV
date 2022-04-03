"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c "tasklist" | Out-File -FilePath $args[0] -Append