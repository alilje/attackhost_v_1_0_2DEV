$webbrowsername = "chrome"
$pages = "127.0.0.1:5000/dummy1",
                    "127.0.0.1:5000/dummy2",
                    "127.0.0.1:5000/dummy3",
                    "127.0.0.1:5000/dummy4",
                    "127.0.0.1:5000/dummy5",
                    "127.0.0.1:5000/dummy6",
                    "127.0.0.1:5000/dummy7",
                    "127.0.0.1:5000/dummy8",
                    "127.0.0.1:5000/dummy9",
                    "127.0.0.1:5000/dummy10"
 
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
 
function Get-WebPageURL{
    param($theWebPages)
    $arrayIndex = Get-Random -Minimum 0 -Maximum ($theWebPages.length-1)
    $pageResult = $theWebPages[$arrayIndex]
    return $pageResult
}
 
$num = 10
For ($i=0; $i -le $num; $i++) {
    $browseropentime = Get-OpenTime
    $browserclosedtime = Get-ClosedTime
    $browserpage = Get-WebPageURL($pages)
    sleep $browserclosedtime
    Start-Process $webbrowsername $browserpage
    sleep $browseropentime
    Stop-Process -name $webbrowsername
    }
 
