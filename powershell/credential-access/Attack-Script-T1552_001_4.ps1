'***********T1552_001_4---Credentials In Files**********'| Out-File -FilePath $args[0]
cmd.exe /c 'type C:\Windows\Panther\unattend.xml' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'type C:\Windows\Panther\Unattend\unattend.xml' |  Out-File -FilePath $args[0] -Append
