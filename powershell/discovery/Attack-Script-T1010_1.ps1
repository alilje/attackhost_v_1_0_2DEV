"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c .\powershell\external\T1010_1\csc1.exe | Out-File -FilePath $args[0] -Append

