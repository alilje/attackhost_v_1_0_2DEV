'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'net user Atomicser User2DeletePW! /add' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'net.exe user AtomicUser /del' | Out-File -FilePath $args[0] -Append
