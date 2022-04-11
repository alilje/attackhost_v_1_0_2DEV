class EventIDTests:
    
    def __init__(self):

        pass

    def printSystemSectionRecords(self):
        print(self.theSystemSection,file=sys.stderr)
        #print(self.theSystemProviderFields,file=sys.stderr)
        #print(self.theSystemEventIDField,file=sys.stderr)
        #print(self.theSystemVersionField,file=sys.stderr)
        #print(self.theSystemLevelField,file=sys.stderr)
        #print(self.theSystemTaskField,file=sys.stderr)
        #print(self.theSystemOpcodeField,file=sys.stderr)
        #print(self.theSystemKeywordsField,file=sys.stderr)
        #print(self.theSystemTimeCreatedFields,file=sys.stderr)
        #print(self.theSystemEventRecordIDField,file=sys.stderr)              
        #print(self.theSystemCorrelationFields,file=sys.stderr)          
        #print(self.theSystemExecutionFields,file=sys.stderr)
        #print(self.theSystemChannelField,file=sys.stderr)
        #print(self.theSystemComputerField,file=sys.stderr)
        #print(self.theSystemSecurityFields,file=sys.stderr) 
        

    def testEventID1(self):
        print(self.ruleName,file=sys.stderr) 
        print(self.utcTime,file=sys.stderr)
        print(self.processGUID,file=sys.stderr)
        print(self.processId,file=sys.stderr)
        print(self.image,file=sys.stderr)                    
        print(self.fileVersion,file=sys.stderr)
        print(self.description,file=sys.stderr)
        print(self.product,file=sys.stderr)
        print(self.company,file=sys.stderr)
        print(self.originalFileName,file=sys.stderr)
        print(self.commandLine,file=sys.stderr)
        print(self.currentDirectory,file=sys.stderr)
        print(self.user,file=sys.stderr)
        print(self.logonGuid,file=sys.stderr)
        print(self.logonId,file=sys.stderr)
        print(self.terminalSessionId,file=sys.stderr)
        print(self.integrityLevel,file=sys.stderr)
        print(self.hashes,file=sys.stderr)
        print(self.parentProcessGuid,file=sys.stderr)
        print(self.parentProcessId,file=sys.stderr) 
        print(self.parentImage,file=sys.stderr)
        print(self.parentCommandLine,file=sys.stderr)
        print(self.parentUser,file=sys.stderr)


    def testEventID2(self):
        print(self.ruleName,file=sys.stderr)
        print(self.utcTime,file=sys.stderr)
        print(self.processGUID,file=sys.stderr)
        print(self.processId,file=sys.stderr)
        print(self.image,file=sys.stderr)
        print(self.targetFilename,file=sys.stderr)
        print(self.creationUtcTime,file=sys.stderr)
        print(self.previousCreationUtcTime,file=sys.stderr)
        print(self.user,file=sys.stderr)

    def testEventID3(self):
        print(self.ruleName,file=sys.stderr)
        print(self.utcTime,file=sys.stderr)
        print(self.processGUID,file=sys.stderr)
        print(self.processId,file=sys.stderr)
        print(self.image,file=sys.stderr) 
        print(self.user,file=sys.stderr)
        print(self.protocol,file=sys.stderr)
        print(self.initiated,file=sys.stderr) 
        print(self.sourceIsIpv6,file=sys.stderr)
        print(self.sourceIp,file=sys.stderr)
        print(self.sourceHostname,file=sys.stderr) 
        print(self.sourcePort,file=sys.stderr)
        print(self.sourcePortName,file=sys.stderr)
        print(self.destinationIsIpv6,file=sys.stderr) 
        print(self.destinationIp,file=sys.stderr)
        print(self.destinationHostname,file=sys.stderr)
        print(self.destinationPort,file=sys.stderr) 
        print(self.destinationPortName,file=sys.stderr)

    def testEventID5(self):
        print(self.ruleName,file=sys.stderr)  
        print(self.utcTime,file=sys.stderr)  
        print(self.processGUID,file=sys.stderr) 
        print(self.processId,file=sys.stderr) 
        print(self.image,file=sys.stderr) 
        print(self.user,file=sys.stderr)  
        
    def testEventID11(self):
        print(self.ruleName,file=sys.stderr) 
        print(self.utcTime,file=sys.stderr) 
        print(self.processGUID,file=sys.stderr)
        print(self.processId,file=sys.stderr)
        print(self.image,file=sys.stderr)
        print(self.targetFilename,file=sys.stderr)
        print(self.creationUtcTime,file=sys.stderr)
        print(self.user,file=sys.stderr)
  
    def testEventID13(self):    
        print(self.ruleName,file=sys.stderr) 
        print(self.eventType,file=sys.stderr) 
        print(self.utcTime,file=sys.stderr) 
        print(self.processGUID,file=sys.stderr) 
        print(self.processId,file=sys.stderr) 
        print(self.image,file=sys.stderr) 
        print(self.targetObject,file=sys.stderr) 
        print(self.details,file=sys.stderr) 
        print(self.user,file=sys.stderr) 




    def testEventID22(self):
        print(self.ruleName,file=sys.stderr) 
        print(self.utcTime,file=sys.stderr)
        print(self.processGUID,file=sys.stderr)
        print(self.processId,file=sys.stderr)
        print(self.queryName,file=sys.stderr)
        print(self.queryStatus,file=sys.stderr)
        print(self.queryResults,file=sys.stderr)
        print(self.image,file=sys.stderr)   
        print(self.user,file=sys.stderr)


