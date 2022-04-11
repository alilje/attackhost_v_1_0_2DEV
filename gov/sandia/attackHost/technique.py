import subprocess
import os
import os.path
import uuid
import datetime
import sys


class TechniqueRunner:

    def __init__(self,technique,name,num,action,platform,powerShellDir,taggedEventsDirectory,jsonFromEventsDirectory,attackOutputDir,detectOutputDir):
        
        #######################################################
        #   self.num is the number of the atomic test
        #   action is either 0 for attack or 1 for detect
        #   powerShellDir is the directory where attack powershell scripts live
        #   attackOutputDir is the directory that receives the attack 
 
        self.technique = technique
        self.name = name
        print(self.name,file=sys.stderr)
        self.num = num 
        self.action = action
        self.platform = platform
        self.powerShellDir = powerShellDir
        self.taggedEventsDirectory = taggedEventsDirectory
        self.jsonFromEventsDirectory = jsonFromEventsDirectory
        self.attackOutputDir = attackOutputDir
        self.detectOutputDir = detectOutputDir
        #self.discoveryCategoryScriptDir = discoveryCategoryScriptDir
        self.attackOutputFileName = os.path.join(self.attackOutputDir, "Attack-" + self.name + "-" + str(self.num) + ".out")
        self.detectOutputFileName = os.path.join(self.detectOutputDir, "Detect-" + self.name + "-" +  str(self.num) + ".out")
        print("*********************" + str(self.platform) + " " + str(self.action))
        if (self.platform =='W' and self.action == 0):
            sys.stderr.write("This is a windows platform")
            sys.stderr.write("Program is in attack mode")
            self.doAttack()
        if self.platform =='W' and self.action == 1:
            sys.stderr.write("This is a windows platform")
            sys.stderr.write("Program is in cleanup mode")
            self.doCleanup()
        
        elif platform == "X":
            pass
        elif platform == "M":
            pass
        else:  
            print("Unknown option", file=sys.stderr)
            sys.exit(-999)
      
    def doAttack(self):
        if self.technique == "collection":
            self.attackCommand = self.makeAttackCommand("collection")
            print("ATTACK COMMAND: " + self.attackCommand)
        p = subprocess.Popen(['powershell.exe', self.attackCommand])
        print("AFTER SUBPROCESS")
        p.wait()
        print("DO ATTACK COMPLETE")
     
    def makeAttackCommand(self,aStr):
        print("####################### " + os.getcwd())
        theDir = os.path.join(self.powerShellDir,aStr)
        self.attackScriptFileName = os.path.join(theDir,"Attack-Script-" + self.name + ".ps1")
        self.attackScriptCommand = self.attackScriptFileName + " " + self.attackOutputFileName
        print("THE COMMAND: " + self.attackScriptCommand)
        return self.attackScriptCommand
    
    def doCleanup(self):
        if self.technique == "collection":
            self.attackCommand = self.makeCleanupCommand("collection")
            print("ATTACK COMMAND: " + self.attackCommand)
        p = subprocess.Popen(['powershell.exe', self.attackCommand])
        p.wait()
     
    def makeCleanupCommand(self,aStr):
        theDir = os.path.join(self.powerShellDir,aStr)
        self.attackScriptFileName = os.path.join(theDir,"Cleanup-Script-" + self.name + ".ps1" + " " + self.attackOutputFileName)
        return self.attackScriptFileName 