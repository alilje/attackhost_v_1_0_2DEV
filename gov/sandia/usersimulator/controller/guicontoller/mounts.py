import os
import os.path
import subprocess

class Mounts:
       
    def __init__(self,theDir):
        self.installationDir = theDir
        self.runUser()

    def runUser(self):
        powerShellDir = os.path.join(self.installationDir,"powershell")
        self.userScript = os.path.join(powerShellDir,"UserSim-Script-" + __class__.__name__ + ".ps1")
        
        p = subprocess.Popen(['powershell.exe', self.userScript])
        p.wait()
        

