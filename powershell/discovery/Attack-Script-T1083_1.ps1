"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c "dir /s c:\\Documents and Settings" | Out-File -FilePath $args[0] -Append
cmd.exe /c "dir /s c:\\Program Files\" | Out-File -FilePath $args[0] -Append
cmd.exe /c "dir %systemdrive%\\Users\\*.*" | Out-File -FilePath $args[0] -Append
cmd.exe /c "dir %userprofile%\\AppData\\Roaming\\Microsoft\Windows\\Recent\\*.*"| Out-File -FilePath $args[0] -Append
cmd.exe /c "dir %userprofile%\\Desktop\\*.*" | Out-File -FilePath $args[0] -Append
cmd.exe /c "tree /F" | Out-File -FilePath $args[0] -Append