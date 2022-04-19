'*******************************************************************************'| Out-File -FilePath $args[0]
cmd.exe /c 'taskkill.exe /f /im spoolsv.exe' |  Out-File -FilePath $args[0] -Append