from gov.sandia.atomicHost.util.powershell import AttackHostFile
from gov.sandia.atomicHost.util.consts import AhConst
import sys

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
        self.attackFileName = "Attack-Script-" + self.name + ".ps1"
        self.numAttackStatements = self.inFH.readline().replace("\n","")
        self.numCleanupStatements = self.inFH.readline().replace("\n","")
        print(self.numAttackStatements)
        print(self.numCleanupStatements)
        self.attackStatements = []
        self.cleanupStatements = []
        for i in range(1,int(self.numAttackStatements)+1):
            self.attackStatements.append(self.inFH.readline().replace("\n",""))
            #self.outLine = 'cmd.exe /c ' + "'" + cm + "'" + ' |  Out-File -FilePath $args[0] -Append' + "\n"
            #self.outFH.write(outLine)
        for i in range(1,int(self.numCleanupStatements)+1):
            self.cleanupStatements.append(self.inFH.readline().replace("\n",""))
            #self.outLine = 'cmd.exe /c ' + "'" + cm + "'" + ' |  Out-File -FilePath $args[0] -Append' + "\n"
            #self.outFH.write(outLine)
        #self.inFH.close()
        #self.attackFileName = "Attack-Script-" + self.name + ".ps1"
        #self.cleanupFileName = "Cleanup-Script-" + self.name + ".ps1"
        #self.outAttackFH = open(self.attackFileName,"w")
        #self.outCleanupFH = open(self.cleanupFileName,"w")

        print(self.attackStatements)
        print(self.cleanupStatements)
        #for i in range(1,self.commands+1):
            #self.attackStatements.append = self.inFH.readline().replace("\n","")
        #for i in range(1,self.)    
            
        #self.outLine = 'cmd.exe /c ' + "'" + cm + "'" + ' |  Out-File -FilePath $args[0] -Append' + "\n"
        #self.outFH.write(outLine)
        #self.header = "'" + "***********" + self.name + "---" + self.techniqueTitle + "---" + self.attackTitle + "**********" + "'" + '| Out-File -FilePath $args[0]' + "\n"

        #self.outFH.close()
        #self.inFH.close()

class SupportingDirs:
    
    def __init__(self,aDatDoc):
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