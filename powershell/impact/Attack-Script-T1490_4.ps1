'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'bcdedit.exe /set {default} recoveryenabled no' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'bcdedit.exe /set {default} bootstatuspolicy DisplayAllFailures >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'bcdedit.exe /set {default} recoveryenabled yes >nul 2>&1' |  Out-File -FilePath $args[0] -Append