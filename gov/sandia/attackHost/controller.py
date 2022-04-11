import sys
import os
import os.path

from gov.sandia.attackHost.technique import TechniqueRunner

class ControllerWindows:

    def __init__(self,technique,name,number,action,platform,powerShellDir,taggedEventsDirectory,jsonFromEventsDirectory,attackOutputDir,detectOutputDir,installationDir):
        
        self.technique=technique
        print("TECHNIQUE: " + self.technique)
        self.name=name
        self.number=number
        self.action=action
        self.platform=platform
        self.powerShellDir=powerShellDir
        self.taggedEventsDirectory=taggedEventsDirectory
        self.jsonFromEventsDirectory=jsonFromEventsDirectory
        self.attackOutputDir=attackOutputDir
        self.detectOutputDir=detectOutputDir
        self.installationDir = installationDir

        filename = ""
        print("ACTION: " + str(self.action))
        tr = TechniqueRunner(self.technique,self.name,self.number,self.action,self.platform,self.powerShellDir,self.taggedEventsDirectory,self.jsonFromEventsDirectory,self.attackOutputDir,self.detectOutputDir)

