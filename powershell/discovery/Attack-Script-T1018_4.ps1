"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c "reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" | Out-File -FilePath $args[0] -Append
cmd.exe /c "reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunServices" | Out-File -FilePath $args[0] -Append
cmd.exe /c "reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad" | Out-File -FilePath $args[0] -Append
cmd.exe /c "reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce" | Out-File -FilePath $args[0] -Append
cmd.exe /c "reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnceEx"| Out-File -FilePath $args[0] -Append
cmd.exe /c "reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run" | Out-File -FilePath $args[0] -Append
cmd.exe /c "reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce" | Out-File -FilePath $args[0] -Append
cmd.exe /c "reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run"| Out-File -FilePath $args[0] -Append
cmd.exe /c "reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run" | Out-File -FilePath $args[0] -Append