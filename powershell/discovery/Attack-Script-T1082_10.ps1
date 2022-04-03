"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c "set" | Out-File -FilePath $args[0] -Append