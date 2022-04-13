'***********T1559_002_2--Dynamic Data Exchange--Execute PowerShell script via Word DDE**********'| Out-File -FilePath $args[0]
cmd.exe /c 'start .\static\docx\T1559_002\DDE_Document.docx' | Out-File -FilePath $args[0] -Append
