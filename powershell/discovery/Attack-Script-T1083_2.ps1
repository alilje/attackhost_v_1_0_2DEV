"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c "powershell ls -recurse" | Out-File -FilePath $args[0] -Append
cmd.exe /c "powershell get-childitem" -recurse | Out-File -FilePath $args[0] -Append
cmd.exe /c "powershell gci -recurse" | Out-File -FilePath $args[0] -Append
