"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'type C:\Windows\Panther\unattend.xml' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'type C:\Windows\Panther\Unattend\unattend.xml' |  Out-File -FilePath $args[0] -Append

