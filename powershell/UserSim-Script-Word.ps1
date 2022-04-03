param($theDir)

function Get-OpenTime{
    $minTime = 20
    $maxTime = 100
    $aTime = Get-Random -Minimum $minTime -Maximum $maxTime
 
    return $aTime
}
 
function Get-ClosedTime{
    $minTime = 10
    $maxTime = 70
    $aTime = Get-Random -Minimum $minTime -Maximum $maxTime
 
    return $aTime

}
 

 
While ($True) {
    $i=0 
    $wordopentime = Get-OpenTime
    $wordclosedtime = Get-ClosedTime
    sleep $wordclosedtime
    
    $word=New-Object –ComObject Word.Application
    $word.Visible = $false
    $doc = $word.documents.add()
    sleep $wordopentime
    $outputPath = $theDir + "\\test" + $i.ToString() + ".docx"
    $doc.SaveAs($outputPath)
    $doc.Close()
    $word.Quit()
    # Stop Winword Process
    $rc = [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word)
    $i=$i+1

}
 
