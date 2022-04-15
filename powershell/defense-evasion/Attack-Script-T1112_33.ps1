'*************************************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal\AtomicSafeMode" /VE /T REG_SZ /F /D "Service"' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete "HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal\AtomicSafeMode" /f' |  Out-File -FilePath $args[0] -Append
