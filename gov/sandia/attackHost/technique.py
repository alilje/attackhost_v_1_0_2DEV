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
        print(self.technique)
        self.name = name
        self.num = num 
        self.action = action
        self.platform = platform
        self.powerShellDir = powerShellDir
        self.taggedEventsDirectory = taggedEventsDirectory
        self.jsonFromEventsDirectory = jsonFromEventsDirectory
        self.attackOutputDir = attackOutputDir
        #self.discoveryCategoryScriptDir = discoveryCategoryScriptDir
        self.attackOutputFileName = os.path.join(self.attackOutputDir, "Attack-" + self.name + "-" + str(self.num) + ".out")
        if (self.platform =='W'):
            sys.stderr.write("MADE IT")
            sys.stderr.write("This is a windows platform")
            sys.stderr.write("Program is in attack mode")
            self.doAttack()
        
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
            print("COLLECTION-----: " + str(self.attackCommand))
            p = subprocess.Popen(['powershell.exe', self.attackCommand])
            p.wait()
        if self.technique == "discovery":
            self.attackCommand = self.makeAttackCommand("discovery")
            print("DISCOVERY----: " + str(self.attackCommand))
            p = subprocess.Popen(['powershell.exe', self.attackCommand])
            p.wait()
        if self.technique == "execution":
            self.attackCommand = self.makeAttackCommand("execution")
            print("EXECUTION-----: " + str(self.attackCommand))
            p = subprocess.Popen(['powershell.exe', self.attackCommand])
            p.wait()
        if self.technique == "command-and-control":
            self.attackCommand = self.makeAttackCommand("command-and-control")
            print("COMMAND AND CONTROL-----: " + str(self.attackCommand))
            p = subprocess.Popen(['powershell.exe', self.attackCommand])
            p.wait()
        if self.technique == "defense-evasion":
            self.attackCommand = self.makeAttackCommand("defense-evasion")
            print("DEFENSE EVASION-----: " + str(self.attackCommand))
            p = subprocess.Popen(['powershell.exe', self.attackCommand])
            p.wait()
        if self.technique == "impact":
            self.attackCommand = self.makeAttackCommand("impact")
            print("IMPACT-----: " + str(self.attackCommand))
            p = subprocess.Popen(['powershell.exe', self.attackCommand])
            p.wait()
        if self.technique == "exfiltration":
            self.attackCommand = self.makeAttackCommand("exfiltration")
            print("EXFILTRATION-----: " + str(self.attackCommand))
            p = subprocess.Popen(['powershell.exe', self.attackCommand])
            p.wait()
        if self.technique == "persistence":
            self.attackCommand = self.makeAttackCommand("persistence")
            print("PERSISTENCE-----: " + str(self.attackCommand))
            p = subprocess.Popen(['powershell.exe', self.attackCommand])
            p.wait()
        if self.technique == "initial-access":
            self.attackCommand = self.makeAttackCommand("initial-access")
            print("INITIAL-ACCESS-----: " + str(self.attackCommand))
            p = subprocess.Popen(['powershell.exe', self.attackCommand])
            p.wait()             
     
    def makeAttackCommand(self,aStr):
        theDir = os.path.join(self.powerShellDir,aStr)
        self.attackScriptFileName = os.path.join(theDir,"Attack-Script-" + self.name + ".ps1")
        self.attackScriptCommand = self.attackScriptFileName + " " + self.attackOutputFileName
        print("ATTACK COMMAND: " + self.attackScriptCommand)
        return self.attackScriptCommand
    
    