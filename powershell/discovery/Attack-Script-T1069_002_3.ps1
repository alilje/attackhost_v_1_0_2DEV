"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'net group /domai "Domain Admins"' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net groups "Account Operators" /doma' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net groups "Exchange Organization Management" /doma' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net group "BUILTIN\Backup Operators" /doma' | Out-File -FilePath $args[0] -Append