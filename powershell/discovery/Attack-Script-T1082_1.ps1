"**********************************************************************************************" | Out-File -FilePath $args[0]
cmd.exe /c 'systeminfo' |  Out-File -FilePath $args[0] -Append
"                                                               " | Out-File -FilePath $args[0] -Append
"**********************************************************************************************" | Out-File -FilePath $args[0] -Append
cmd.exe /c 'reg query HKLM\SYSTEM\CurrentControlSet\Services\Disk\Enum'  |  Out-File -FilePath $args[0] -Append

