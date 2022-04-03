
While ($True) {
    New-PSDrive -Name "K" -PSProvider FileSystem -Root "\\snl\Collaborative"
    Start-Sleep -s 30
    Get-PSDrive K | Remove-PSDrive
    New-PSDrive -Name "L" -PSProvider FileSystem -Root "\\snl\Collaborative\Dexter"
    Start-Sleep -s 30
    Get-PSDrive L | Remove-PSDrive
    Start-Sleep -s 30
}
       
 