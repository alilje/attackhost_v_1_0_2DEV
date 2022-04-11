from gov.sandia.attackHost.filesystem.directories import Folder
import sys
import os
import os.path
import glob


class Config:
    
    def __init__(self):
        self.installationDir = '.'
        self.absInstallationDir = os.path.abspath(self.installationDir)
        print(self.absInstallationDir,file=sys.stderr)
        self.dataDir = os.path.join(self.absInstallationDir,"data")
        self.powerShellDir = os.path.normpath(os.path.join(self.absInstallationDir,"powershell"))
        self.outputDir = os.path.normpath(os.path.join(self.dataDir,"output"))         
        self.inputDir = os.path.normpath(os.path.join(self.dataDir,"input")) 
        self.taggedEventsDirectory = os.path.normpath(os.path.join(self.outputDir,'TaggedEvents'))
        self.jsonFromEventsDirectory = os.path.normpath(os.path.join(self.outputDir, "JsonFromEvtx"))
        self.events2jsonOutputFile = os.path.normpath(os.path.join(self.jsonFromEventsDirectory, "events2json.json"))
        self.attackOutputDir = os.path.normpath(os.path.join(self.outputDir, "AttackResults"))
        self.detectOutputDir = os.path.normpath(os.path.join(self.outputDir, "DetectResults"))
        self.evtxToJsonPowerShell = os.path.normpath(os.path.join(self.powerShellDir, "getEventsInFile.ps1"))
        #self.discoveryCategoryScriptDir = os.path.normpath(os.path.join(self.absInstallationDir,"gov/sandia/attackHost/ah/discovery"))


    def checkFolders(self):
        folder = Folder()
        folder.checkDirs(self.outputDir)
        folder.checkDirs(self.inputDir)
        folder.checkDirs(self.dataDir)
        folder.checkDirs(self.powerShellDir)
        folder.checkDirs(self.taggedEventsDirectory)
        folder.checkDirs(self.jsonFromEventsDirectory)
        folder.checkDirs(self.attackOutputDir)
        folder.checkDirs(self.detectOutputDir)
        #folder.checkDirs(self.discoveryCategoryScriptDir)

    def clearResults(self):     
        pattern = os.path.join(self.attackOutputDir,"*")
        print(pattern)
        files = glob.glob(pattern)
        for f in files:
            os.remove(f)
            

