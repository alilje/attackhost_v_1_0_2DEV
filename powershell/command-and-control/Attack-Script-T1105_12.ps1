'***********T1105_12--Ingress Tool Transfer--svchost writing a file to a UNC path**********'| Out-File -FilePath $args[0]
cmd.exe /c 'copy C:\Windows\System32\cmd.exe C:\svhost.exe'
cmd.exe /c 'C:\svchost.exe /c echo T1105 > \\localhost\c$\T1105.txt'