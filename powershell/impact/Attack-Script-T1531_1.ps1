'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'net user AtomicAdministrator User2ChangePW! /add' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net.exe user AtomicAdministrator HuHuHUHoHo283283@dJD' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net user AtomicAdministrator /del' | Out-File -FilePath $args[0] -Append
