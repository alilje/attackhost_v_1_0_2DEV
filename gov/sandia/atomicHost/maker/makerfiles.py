from gov.sandia.atomicHost.util.powershell import AttackHostFile
from gov.sandia.atomicHost.util.consts import AhConst
import sys
import os
import os.path
from gov.sandia.atomicHost.filesystem.helpers import Touch

class DatDoc:
    
    def __init__(self,afile):
        self.theFile = afile
        self.attackInformation = self.theFile
        self.readAttackInformation()
        
    
        #includes both attack and clean-up
        
    def readAttackInformation(self):       
        self.inFH = open(self.attackInformation,"r")
        self.name = self.inFH.readline().replace("\n","")
        self.redCanaryTechniqueName = self.inFH.readline().replace("\n","")
        self.redCanaryTechniqueNumber  = self.inFH.readline().replace("\n","")
        self.redCanaryTechniqueCategory = self.inFH.readline().replace("\n","")
        self.techniqueTitle = self.inFH.readline().replace("\n","")
        self.attackTitle = self.inFH.readline().replace("\n","")
        #self.attackFileName = "Attack-Script-" + self.name + ".ps1"
        self.numAttackStatements = self.inFH.readline().replace("\n","")
        self.numCleanupStatements = self.inFH.readline().replace("\n","")
        self.attackStatements = []
        self.cleanupStatements = []
        for i in range(1,int(self.numAttackStatements)+1):
            self.attackStatements.append(self.inFH.readline().replace("\n",""))
        for i in range(1,int(self.numCleanupStatements)+1):
            self.cleanupStatements.append(self.inFH.readline().replace("\n",""))
        self.inFH.close()
        
        print("Name: " + str(self.name))
        print("Red Canary Technique Name: " + str(self.redCanaryTechniqueName))
        print("Red Canary Test Number: " + str(self.redCanaryTechniqueNumber))
        print("Red Canary Technique Category: " + str(self.redCanaryTechniqueCategory ))
        print("Red Canary Technique Title: " + str(self.techniqueTitle)) 
        print("Red Canary Test Name: " + str(self.attackTitle)) 
        #self.attackFileName = "Attack-Script-" + self.name + ".ps1"
        print("Number of Attack Statements: " + str(self.numAttackStatements ))
        print("Number of Cleanup Statements: " + str(self.numCleanupStatements ))
        print("Attack Statements: " + str(self.attackStatements ))
        print("Cleanup Statements: " + str(self.cleanupStatements))

class SupportingDirs:
    
    def __init__(self,aDatDoc):
        self.theDatDoc = aDatDoc
        self.categories = ["collection", 
                           "credential-access",
                           "defense-evasion",
                           "discovery",
                           "external",
                           "privilege-escalation",
                           "command-and-control",
                           "execution",
                           "exfiltration",
                           "impact",
                           "initial-access",
                           "lateral-movement"
                           "persistence"
                           ]
        
        dirName = self.theDatDoc.name    
        category = self.theDatDoc.redCanaryTechniqueCategory
        self.originalDir = os.getcwd()
        os.chdir(os.path.join(self.originalDir,"powershell"))
        self.powershellDir = os.getcwd()
        os.chdir(os.path.join(self.powershellDir,category))
        self.categoryDir = os.getcwd()
        isADir = os.path.isdir(os.path.join(self.categoryDir, self.theDatDoc.name))
        if isADir==False:
           self.setUpDirs()
        os.chdir(self.originalDir)
            
        
    def setUpDirs(self):
        os.chdir(self.categoryDir)
        os.mkdir(self.theDatDoc.name)
        self.theTechniqueNameDir = os.path.join(self.categoryDir,self.theDatDoc.name)
        os.chdir(self.theTechniqueNameDir)
        Touch(".gitkeep")
        os.mkdir("temp")
        os.mkdir("bin")
        os.mkdir("in")
        os.mkdir("out")
        pathOut = os.path.join(self.theTechniqueNameDir,"out")
        pathIn = os.path.join(self.theTechniqueNameDir,"in")
        pathTemp = os.path.join(self.theTechniqueNameDir,"temp")
        pathBin = os.path.join(self.theTechniqueNameDir,"bin")
        os.chdir(pathOut)
        Touch(".gitkeep")
        os.chdir(pathIn)
        Touch(".gitkeep")
        os.chdir(pathTemp)
        Touch(".gitkeep")
        os.chdir(pathBin)
        Touch(".gitkeep")
        
        
        
        
        
class AttackScript:
    
    def __init__(self):
        pass
    
    
class CleanUpScript:
    
    def __init__(self):
        pass
    
    
        #self.outLine = 'cmd.exe /c ' + "'" + cm + "'" + ' |  Out-File -FilePath $args[0] -Append' + "\n"
            #self.outFH.write(outLine)
            #for i in range(1,self.commands+1):
            #self.attackStatements.append = self.inFH.readline().replace("\n","")
        #for i in range(1,self.)    
            
        #self.outLine = 'cmd.exe /c ' + "'" + cm + "'" + ' |  Out-File -FilePath $args[0] -Append' + "\n"
        #self.outFH.write(outLine)
        #self.header = "'" + "***********" + self.name + "---" + self.techniqueTitle + "---" + self.attackTitle + "**********" + "'" + '| Out-File -FilePath $args[0]' + "\n"
#self.outLine = 'cmd.exe /c ' + "'" + cm + "'" + ' |  Out-File -FilePath $args[0] -Append' + "\n"
            #self.outFH.write(outLine)
        #self.inFH.close()
        #self.attackFileName = "Attack-Script-" + self.name + ".ps1"
        #self.cleanupFileName = "Cleanup-Script-" + self.name + ".ps1"
        #self.outAttackFH = open(self.attackFileName,"w")
        #self.outCleanupFH = open(self.cleanupFileName,"w")
        
        