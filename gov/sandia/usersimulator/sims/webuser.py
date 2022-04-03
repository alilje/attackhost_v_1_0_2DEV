import subprocess
import os
import os.path
import uuid
import datetime
import sys


class Firefox:

    def __init__(self):
        
        self.webbrowsername = "firefox"
        print("Here",file=sys.stderr)
        


'''

       param($webbrowsername)
$pages = "google.com",
                    "microsoft.com",
                    "apple.com",
                    "inside.sandia.gov",
                    "gihub.com",
                    "hr.sandia.gov",
                    "www.sandia.gov",
                    "amazon.com",
                    "pixabay.com",
                    "wiki.sandia.gov",
                    "htmlcolorcodes.com",
                    "esri.com",
                    "usda.gov",
                    "usgs.gov",
                    "qgis.org",
                    "chase.com",
                    "openei.org",
                    "earthdata.nasa.gov",
                    "scihub.copernicus.eu",
                    "yahoo.com",
                    "dell.com",
                    "hp.com",
                    "zenkit.com",
                    "geoserver.org",
                    "wayfair.com",
                    "jcpenny.com",
                    "zoho.com",
                    "unm.edu",
                    "koat.com",
                    "ford.com",
                    "reddit.com",
                    "ebay.com",
                    "www.youtube.com",
                    "facebook.com",
                    "wikipedia.org",
                    "twitter.com",
                    "live.com",
                    "bing.com",
                    "instagram.com",
                    "linkedin.com",
                    "msn.com",
                    "pinterest.com",
                    "netflix.com",
                    "wordpress.com",
                    "tumblr.com",
                    "paypal.com",
                    "blogspot.com",
                    "stackoverflow.com",
                    "imdb.com",
                    "blogger.com",
                    "craigslist.org",
                    "dropbox.com",
                    "cnn.com",
                    "accuweather.com"
 
function Get-OpenTime{
    $minTime = 20
    $maxTime = 100
    $aTime = Get-Random -Minimum $minTime -Maximum $maxTime
 
    return $aTime
}
 
function Get-ClosedTime{
    $minTime = 10
    $maxTime = 80
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
 
  
       
      
    def simUser(self):
        self.attackScriptFileName = os.path.join(self.powerShellDir,"Attack-Script-" + __class__.__name__ + ".ps1" + " " + self.attackOutputFileName)
        self.attackCommand = os.path.join(self.powerShellDir,self.attackScriptFileName).replace('\\','/')
        sys.stderr.write("We are attacking-------------------------------")
        p = subprocess.Popen(['powershell.exe', self.attackCommand])
        p.wait()
        sys.stderr.write("We are done attacking----------------------------")


   '''      
        
