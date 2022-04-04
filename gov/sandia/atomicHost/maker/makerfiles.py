from gov.sandia.atomicHost.util.powershell import AttackHostFile
from gov.sandia.atomicHost.util.consts import AhConst
import sys
import os
import os.path
from gov.sandia.atomicHost.filesystem.helpers import Touch

class DatDoc:
    
    def __init__(self,afile):
        self.attackHostDirectory = os.getcwd()
        self.powershellDir = os.path.join(self.attackHostDirectory,"powershell")
        self.theFile = afile
        self.attackInformation = self.theFile
        self.catCollectionDir = os.path.join(self.powershellDir,"collection")
        self.catCredentialAccess = os.path.join(self.powershellDir,"credential-access")
        self.catDefenseEvasion = os.path.join(self.powershellDir,"defense-evasion")
        self.catDiscovery = os.path.join(self.powershellDir,"discovery")
        self.catExternal = os.path.join(self.powershellDir,"external")
        self.catPrivilegeEscalation = os.path.join(self.powershellDir,"privilege-escalation")
        self.catCommandAndControl = os.path.join(self.powershellDir, "command-and-control")
        self.catExecution = os.path.join(self.powershellDir, "execution")
        self.catExfiltration = os.path.join(self.powershellDir, "exfiltration")
        self.catImpact = os.path.join(self.powershellDir, "impact")
        self.catInitialAccess = os.path.join(self.powershellDir, "initial-access")
        self.catLateralMovement = os.path.join(self.powershellDir, "lateral-movement")
        self.catPersistence = os.path.join(self.powershellDir, "persistence") 
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
        self.numAttackStatements = self.inFH.readline().replace("\n","")
        self.numCleanupStatements = self.inFH.readline().replace("\n","")
        self.attackStatements = []
        self.cleanupStatements = []
        for i in range(1,int(self.numAttackStatements)+1):
            self.attackStatements.append(self.inFH.readline().replace("\n",""))
        for i in range(1,int(self.numCleanupStatements)+1):
            self.cleanupStatements.append(self.inFH.readline().replace("\n",""))
        self.inFH.close()
        
class SupportingDirs:
    
    def __init__(self,aDatDoc):
        self.theDatDoc = aDatDoc
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
    
    def __init__(self,aDatDoc):
        self.aDatDoc = aDatDoc
        self.theAttackScriptFileName = "Attack-Script-" + self.aDatDoc.name + ".ps1"
        self.attackScriptFile = os.path.join(self.aDatDoc.catCollectionDir,self.theAttackScriptFileName)
        self.outFH = open(self.attackScriptFile,"w")
        self.header1 = "'" + "** AttackHost Name: " + self.aDatDoc.name + "***********" + "'"
        self.header2 = "'" + "** Red Canary Technique Name: " + self.aDatDoc.redCanaryTechniqueName + "***********" + "'"
        self.header3 = "'" + "** Red Canary Technique Test Number: " + self.aDatDoc.redCanaryTechniqueNumber + "**********" + "'"
        self.header4 = "'" + "** Red Canary Technique Test Category: " + self.aDatDoc.redCanaryTechniqueCategory + "**********" + "'"
        
        
        
        
        FH.readline().replace("\n","")
                #self.outLine = 'cmd.exe /c ' + "'" + cm + "'" + ' |  Out-File -FilePath $args[0] -Append' + "\n"

        
        
        #self.inFH.close()

    
    
class CleanUpScript:
    
    def __init__(self):
        pass
    
    #self.attackFileName = "Attack-Script-" + self.name + ".ps1"
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
class InfoDatDoc:
    
    def __init__(self,theDatDoc):
        self.theDatDoc = theDatDoc
        
    def printall(self):
        
        print("Name: " + str(self.theDatDoc.name))
        print("Red Canary Technique Name: " + str(self.theDatDoc.redCanaryTechniqueName))
        print("Red Canary Test Number: " + str(self.theDatDoc.redCanaryTechniqueNumber))
        print("Red Canary Technique Category: " + str(self.theDatDoc.redCanaryTechniqueCategory ))
        print("Red Canary Technique Title: " + str(self.theDatDoc.techniqueTitle)) 
        print("Red Canary Test Name: " + str(self.theDatDoc.attackTitle)) 
        
        print("Number of Attack Statements: " + str(self.theDatDoc.numAttackStatements ))
        print("Number of Cleanup Statements: " + str(self.theDatDoc.numCleanupStatements ))
        print("Attack Statements: " + str(self.theDatDoc.attackStatements ))
        print("Cleanup Statements: " + str(self.theDatDoc.cleanupStatements))        
        