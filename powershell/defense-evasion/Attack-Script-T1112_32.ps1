'*************************************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v HideSCAPower /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg  add HKCU\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging /v EnableModuleLogging /t REG_DWORD /d 0 /f'  |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg  add HKCU\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging /v EnableScriptBlockLogging /t REG_DWORD /d 0 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg  add HKCU\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableTranscripting /t REG_DWORD /d 0 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg  add HKCU\Software\Policies\Microsoft\Windows\PowerShell /v EnableScripts /t REG_DWORD /d 0 /f' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'REM do a little cleanup immediately to avoid execution issues with later tests' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKCU\Software\Policies\Microsoft\Windows\PowerShell /v EnableScripts /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'Timeout / t 5' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKCU\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging /v EnableModuleLogging /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKCU\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging /v EnableScriptBlockLogging /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg delete HKCU\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableTranscripting /f >nul 2>&1' |  Out-File -FilePath $args[0] -Append