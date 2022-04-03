'***********T1040_4---Network-Sniffing---Windows-Internal-Packet-Capture**********'| Out-File -FilePath $args[0]
cmd.exe /c 'netsh trace start capture=yes tracefile=trace.etl maxsize=10' |  Out-File -FilePath $args[0] -Append
