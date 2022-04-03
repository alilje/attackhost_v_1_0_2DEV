import os
import os.path
import subprocess
import sys

class Word:
    
    def __init__(self,theDir,filesDir):
        self.installationDir = theDir
        self.filesDir = filesDir
        self.runUser()

    def runUser(self):      
        aWordDir = self.filesDir
        powerShellDir = os.path.join(self.installationDir,"powershell")
        self.userScript = os.path.join(powerShellDir,"UserSim-Script-" + __class__.__name__ + ".ps1 " + " " + aWordDir)    
        p = subprocess.Popen(['powershell.exe', self.userScript])
        p.wait()
        

class PPT:
    
    def __init__(self,theDir):
        self.installationDir = theDir
        self.runUser()

    def runUser(self):
        powerShellDir = os.path.join(self.installationDir,"powershell")
        self.userScript = os.path.join(powerShellDir,"UserSim-Script-" + __class__.__name__ + ".ps1")        
        p = subprocess.Popen(['powershell.exe', self.userScript])
        p.wait()


class Excel:
    
    def __init__(self,theDir):
        self.installationDir = theDir
        self.runUser()

    def runUser(self):
        powerShellDir = os.path.join(self.installationDir,"powershell")
        self.userScript = os.path.join(powerShellDir,"UserSim-Script-" + __class__.__name__ + ".ps1")
        
        p = subprocess.Popen(['powershell.exe', self.userScript])
        p.wait()
        




