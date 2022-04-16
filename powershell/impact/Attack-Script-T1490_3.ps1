'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'wbadmin delete catalog -quiet' | Out-File -FilePath $args[0] -Append
