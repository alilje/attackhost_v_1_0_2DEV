import subprocess
import os
import os.path
import uuid
import datetime
import sys


class TechniqueRunner:

    def __init__(self,name,num,action,platform,powerShellDir,taggedEventsDirectory,jsonFromEventsDirectory,attackOutputDir,detectOutputDir,discoveryCategoryScriptDir):
        
        #######################################################
        #   self.num is the number of the atomic test
        #   action is either 0 for attack or 1 for detect
        #   powerShellDir is the directory where attack powershell scripts live
        #   attackOutputDir is the directory that receives the attack 
 
        
        self.name = name
        print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK",file=sys.stderr)
        print(self.name,file=sys.stderr)
        self.num = num 
        self.action = action
        self.platform = platform
        self.powerShellDir = powerShellDir
        self.taggedEventsDirectory = taggedEventsDirectory
        self.jsonFromEventsDirectory = jsonFromEventsDirectory
        self.attackOutputDir = attackOutputDir
        self.detectOutputDir = detectOutputDir
        self.discoveryCategoryScriptDir = discoveryCategoryScriptDir
        self.attackOutputFileName = os.path.join(self.attackOutputDir, "Attack-" + self.name + "-" + str(self.num) + ".out")
        self.detectOutputFileName = os.path.join(self.detectOutputDir, "Detect-" + self.name + "-" +  str(self.num) + ".out")
        
        if self.platform =='W' and self.action == 0:
            sys.stderr.write("This is a windows platform")
            sys.stderr.write("Program is in attack mode")
            self.doAttack()
        elif self.platform =='W' and self.action==1:
            sys.stderr.write("Program is in detect mode")
            # Working to verify attack strings
        elif platform == "X":
            pass
        elif platform == "M":
            pass
        else:  
            print("Unknown option", file=sys.stderr)
            sys.exit(-999)
      
    def doAttack(self):
        self.attackScriptFileName = os.path.join(self.powerShellDir,"Attack-Script-" + self.name + ".ps1" + " " + self.attackOutputFileName)
        self.attackCommand = os.path.join(self.powerShellDir,self.attackScriptFileName).replace('\\','/')
        
       
        p = subprocess.Popen(['powershell.exe', self.attackCommand])
        p.wait()
        

    def doDetect(self):
            self.detectScriptFileName = os.path.join(self.powerShellDir,"Detect-Script-" + __class__.__name__ + "-" +  str(self.num)  + ".ps1")
pass

   