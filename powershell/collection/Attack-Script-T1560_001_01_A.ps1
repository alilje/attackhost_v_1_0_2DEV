'**************************************************************************************'| Out-File -FilePath $args[0] 
'** AttackHost Name: T1560_001_01' | Out-File -FilePath $args[0]  -Append
'** Red Canary Technique Name:  T1560.001' | Out-File -FilePath $args[0] -Append
'** Red Canary Technique Test Number: 1' | Out-File -FilePath $args[0] -Append
'** Red Canary Technique Test Category: collection' | Out-File -FilePath $args[0] -Append
'** Red Canary Technique Title: Archive via Utility' | Out-File -FilePath $args[0] -Append
'** Red Canary Test Title: Compress Data for Exfiltration With Rar' | Out-File -FilePath $args[0] -Append
cmd.exe /c 'powershell\collection\T1560_001_01\bin\Rar.exe a -r out1.txt powershell\collection\T1560_001_01\temp\*.txt' |  Out-File -FilePath $args[0] -Append