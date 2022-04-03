"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'netsh.exe advfirewall  show allprofiles' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'tasklist.exe' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'tasklist.exe | findstr /i virus' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'tasklist.exe | findstr /i cb' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'tasklist.exe | findstr /i defender' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'tasklist.exe | findstr /i cylance' | Out-File -FilePath $args[0] -Append
