
While ($True) {
    New-PSDrive -Name "K" -PSProvider FileSystem -Root "\\localhost\c$"
    Start-Sleep -s 30
    Get-PSDrive K | Remove-PSDrive
    New-PSDrive -Name "L" -PSProvider FileSystem -Root "\\localhost\c$\Windows"
    Start-Sleep -s 30
    Get-PSDrive L | Remove-PSDrive
    Start-Sleep -s 30
}
       
 