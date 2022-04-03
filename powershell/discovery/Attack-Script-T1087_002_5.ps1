"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c ".\powershell\external\AdFind.exe -default -s base lockoutduration lockoutthreshold lockoutobservationwindow maxpwdage minpwdage minpwdlength pwdhistorylength pwdproperties" 	|  Out-File -FilePath $args[0] -Append
