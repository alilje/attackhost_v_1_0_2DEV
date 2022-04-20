'***********T1059.002 #2-- Windows Command Shell--Writes text to a file and displays it.**********'| Out-File -FilePath $args[0]
cmd.exe /c 'echo "Test-T1059.003 2" > static\bin\testT1059_003_2.bin & type static\bin\testT1059_003_2.bin' | Out-File -FilePath $args[0] -Append
