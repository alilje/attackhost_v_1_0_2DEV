import sys
import os
import os.path

from gov.sandia.atomicHost.ah.discovery.technique import TechniqueRunner

class ControllerWindows:

    def __init__(self,technique,name,number,action,platform,powerShellDir,taggedEventsDirectory,jsonFromEventsDirectory,attackOutputDir,detectOutputDir,discoveryCategoryScriptDir,installationDir):
        
        self.technique=technique
        self.name=name
        self.number=number
        self.action=action
        self.platform=platform
        self.powerShellDir=powerShellDir
        self.taggedEventsDirectory=taggedEventsDirectory
        self.jsonFromEventsDirectory=jsonFromEventsDirectory
        self.attackOutputDir=attackOutputDir
        self.detectOutputDir=detectOutputDir
        self.discoveryCategoryScriptDir=discoveryCategoryScriptDir

        filename = ""
        
        tr = TechniqueRunner(self.name,self.number,self.action,self.platform,self.powerShellDir,self.taggedEventsDirectory,self.jsonFromEventsDirectory,self.attackOutputDir,self.detectOutputDir,self.discoveryCategoryScriptDir)

