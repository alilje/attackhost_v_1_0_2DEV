import re
import sys
from gov.sandia.atomicHost.util.consts import AhConst


class AttackHostFile:
    
    def __init__(self,atomicHostCommand,techniqueName):
        self.a = AhConst()
        
        self.atomicHostCommand = atomicHostCommand
        #print("self.atomicHostCommand: " + self.atomicHostCommand)
        self.techniqueName = techniqueName
        #print("self.techniqueName: " + self.techniqueName)
        self.leftHeader = self.a.headerLeft
        #print("self.leftHeader: " + self.leftHeader)
        self.rightHeader = self.a.headerRight
        #print("self.rightHeader: " + self.rightHeader)
        self.cmdCom = self.a.prefix
        #print("self.cmdCom: " + self.cmdCom)
        self.remainder = self.a.suffix
        #print("self.remainder: " + self.remainder)
        #self.header = self.constructHeader()
        #self.leftOfPipe = self.constructCommand()
        #self.constructedHeader = self.constructHeader()
        #self.k = k
    
        
    def constructHeader(self):
        tmpHeader = self.a.headerLeft + self.techniqueName + self.a.headerRight
        return tmpHeader
        
    def constructCommand(self):
        tmpLeftCommand = self.cmdCom + " '" + self.atomicHostCommand + "'"
        fullCommand = tmpLeftCommand + " " + self.remainder
        
        
    def constructNoHeader(self):
        print(self.constructCommand())
        
    def constructWithHeader(self):
        aHeader = self.constructHeader()
        aCommand = self.constructCommand()
        out = aHeader + "\n" + aCommand
        print(out)
        
        
        
   
    def assemble(self):
        
        
        fh = open(self.name,"w")
        fh.write(self.constants.header)
        fh.close()
        
        
        
