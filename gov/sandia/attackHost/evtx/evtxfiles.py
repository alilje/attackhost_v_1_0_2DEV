from gov.sandia.attackHost.evtx.jsonTest import EventIDTests
import Evtx.Evtx as evtx
import re
import sys
import os
import json

class EvtxFile:

    def __init__(self,originalEventFileName,dataDir):
        self.originalEventFileName = originalEventFileName
        self.dataDir = dataDir
        self.outputJSON = {}
        self.theString = ""
        self.inputEVTXDir = os.path.join(self.dataDir,"input\\evtx")
        self.f = None
        
        
       

    def saveXML(self):
        (head,tail) = os.path.splitext(self.originalEventFileName)
        newFileName = head + ".xml"
        
        self.outputDir = os.path.join(self.dataDir,"output\\XMLFromEVTX")

        self.outputFileName = os.path.join(self.outputDir,newFileName)
       
        self.inputFileName = os.path.join(self.inputEVTXDir,self.originalEventFileName)
        with evtx.Evtx(self.inputFileName) as log:
            self.f = open(self.inputFileName,"r")
            for inputRecord in log.records():
                rec = inputRecord.xml() 
                g = open(self.outputFileName,"w")
                g.write(rec)
                g.close()
            self.f.close()
                    
    def saveJSON(self):
        # DEFINITIONS ----------------------------------------------------------------------
        (head,tail) = os.path.splitext(self.originalEventFileName)

        newFileName = head + ".json"

        self.outputDir = os.path.join(self.dataDir,"output\\JSONFromEVTX")
        
        
        self.outputFileName = os.path.join(self.outputDir,newFileName)
        
        
        self.inputFileName = os.path.join(self.inputEVTXDir,self.originalEventFileName)
        print("************************************* " + self.inputFileName,file=sys.stderr) 


        if (self.originalEventFileName != ".gitignore"):
            with evtx.Evtx(self.inputFileName) as log:
                # FILE OPEN AND READ
                self.f = open(self.inputFileName,"r")
            
                self.recnum = 0

            # GET INDIVIDUAL RECORDS AND MAKE XML EQUIV

                for inputRecord in log.records():

                    self.recnum=(self.recnum)+1
                    self.recordVal = str(self.recnum)
                    fullRecord = inputRecord.xml() 
               
                

                    self.theSystemSection = self.getSystemSectionFields(fullRecord)
                
                    systemDataList = self.theSystemSection.split("\n")
                
                    self.theSystemEventIDField = self.getField(systemDataList[1])
                
                
                    self.theSystemVersionField= self.getField(systemDataList[2])
                
                    self.theSystemLevelField=self.getField(systemDataList[3])
                
                    self.theSystemTaskField=self.getField(systemDataList[4])
                
                    self.theSystemOpcodeField=self.getField(systemDataList[5])
                
                    self.theSystemKeywordsField=self.getField(systemDataList[6])
                
                    self.theSystemTimeCreatedField=self.getAttribute(systemDataList[7],'SystemTime="','">')               
                
                    self.theSystemEventRecordIDField=self.getField(systemDataList[8])              
                
                    self.theSystemCorrelationActivityIDField=self.getAttribute(systemDataList[9],'ActivityID="','" RelatedActivityID')       
                
                    self.theSystemCorrelationRelatedActivityIDField=self.getAttribute(systemDataList[9],'RelatedActivityID="','">')         

                    self.theSystemExecutionProcessIDField=self.getAttribute(systemDataList[10],'ProcessID="','" ThreadID')
                
                    self.theSystemExecutionThreadField=self.getAttribute(systemDataList[10],'ThreadID="','">')
                
                    self.theSystemChannelField=self.getField(systemDataList[11])
                
                    self.theSystemComputerField=self.getField(systemDataList[12])
                
                    self.theSystemSecurityFields=self.getAttribute(systemDataList[13],'UserID\="','">')

                    self.systemDict = { 
                                    "Record" : self.recordVal,
                                    "System" : {
                                        "EventID" : self.theSystemEventIDField, 
                                        "Version" : self.theSystemVersionField,
                                        "Level" : self.theSystemLevelField,
                                        "Task" : self.theSystemTaskField,
                                        "Opcode" : self.theSystemOpcodeField,
                                        "Keywords" : self.theSystemKeywordsField,
                                        "TimeCreated" : 
                                        { 
                                            "SystemTime" : self.theSystemTimeCreatedField,
                                        },
                                        "EventRecordID" : self.theSystemEventRecordIDField,
                                        "Correlation" : 
                                        {
                                            "ActivityID" : self.theSystemCorrelationActivityIDField,
                                            "RealatedActivityID" : self.theSystemCorrelationRelatedActivityIDField,
                                        },
                                        "Execution" :
                                        { 
                                            "ProcessID" : self.theSystemExecutionProcessIDField,
                                            "ThreadID" : self.theSystemExecutionThreadField,
                                        },
                                        "Channel" : self.theSystemChannelField,
                                        "Computer" : self.theSystemComputerField,
                                        "Security" :
                                        {
                                            "UserID" : self.theSystemSecurityFields
                                        },
                                       }
                            }


                    self.outJSON = open(self.outputFileName,"a")

                    # FOR EACH TYPE OF EVENT WE NEED TO READ GET THE FIELDS

                    if self.theSystemEventIDField == "1":  
                    
                        eventData = self.getEventDataSectionFields(fullRecord) 
                    
                        dataList = eventData.split("\n")  

                        self.ruleName1 = self.getEventDataRuleName(dataList[0]) 
                    
                        self.utcTime1 = self.getEventDataUTCTime(dataList[1]) 
                    
                        self.processGUID1 = self.getEventDataProcessGuid(dataList[2])

                        self.processId1 = self.getEventDataProcessId(dataList[3])

                        self.image1 = self.getEventDataImage(dataList[4]) 
                    
                        self.fileVersion1 = self.getEventDataFileVersion(dataList[5]) 

                        self.description1 = self.getEventDataDescription(dataList[6])

                        self.product1 = self.getEventDataProduct(dataList[7])

                        self.company1 = self.getEventDataCompany(dataList[8])

                        self.originalFileName1 = self.getEventDataOriginalFileName(dataList[9])

                        self.commandLine1 = self.getEventDataCommandLine(dataList[10])

                        self.currentDirectory1 = self.getEventDataCurrentDirectory(dataList[11])

                        self.user1 = self.getEventDataUser(dataList[12])

                        self.logonGuid1 = self.getEventDataLogonGuid(dataList[13])

                        self.logonId1 = self.getEventDataLogonId(dataList[14])

                        self.terminalSessionId1 = self.getEventDataTerminalSessionId(dataList[15])

                        self.integrityLevel1 = self.getEventDataIntegrityLevel(dataList[16])

                        self.hashes1 = self.getEventDataHashes(dataList[17])

                        self.parentProcessGuid1 = self.getEventDataParentProcessGuid(dataList[18])

                        self.parentProcessId1 = self.getEventDataParentProcessId(dataList[19])

                        self.parentImage1 = self.getEventDataParentImage(dataList[20])

                        self.parentCommandLine1 = self.getEventDataParentCommandLine(dataList[21])

                        self.parentUser1 = self.getEventDataParentUser(dataList[22]) 

                    

                        self.eventData = {
                                            "RuleName" : self.ruleName1,
                                            "UtcTime" : self.utcTime1,
                                            "ProcessGuid" : self.processGUID1,
                                            "ProcessId" : self.processId1,
                                            "Image" : self.image1,          
                                            "FileVersion" : self.fileVersion1,
                                            "Description" : self.description1,
                                            "Product" : self.product1, 
                                            "Company" : self.company1,
                                            "OriginalFileName" : self.originalFileName1,
                                            "CommandLine" : self.commandLine1,
                                            "CurrentDirectory" : self.currentDirectory1,
                                            "User" : self.user1,             
                                            "LogonGuid" : self.logonGuid1,
                                            "LogonId" : self.logonId1,
                                            "TerminalSessionId" : self.terminalSessionId1,
                                            "IntegrityLevel" : self.integrityLevel1,
                                            "Hashes" : self.hashes1,
                                            "ParentProcessGuid" : self.parentProcessGuid1,
                                            "ParentProcessId" : self.parentProcessId1,             
                                            "ParentImage" : self.parentImage1,
                                            "ParentCommandLine" : self.parentCommandLine1,
                                            "ParentUser" : self.parentUser1

                        }

                        self.systemDict["Event Data"] = self.eventData

                        json.dump(self.systemDict,self.outJSON)
                        self.outJSON.write("\n")
                    

                    elif self.theSystemEventIDField == "2":
                        eventData = self.getEventDataSectionFields(fullRecord)  
                        dataList = eventData.split("\n") 
                        self.ruleName2 = self.getEventDataRuleName(dataList[0])
                        self.utcTime2 = self.getEventDataUTCTime(dataList[1]) 
                        self.processGUID2= self.getEventDataProcessGuid(dataList[2])
                        self.processId2 = self.getEventDataProcessId(dataList[3])
                        self.image2 = self.getEventDataImage(dataList[4]) 
                        self.targetFilename2 = self.getEventDataTargetFilename(dataList[5])
                        self.creationUtcTime2 = self.getEventDataCreationUtcTime(dataList[6])
                        self.previousCreationUtcTime2 = self.getEventDataPreviousCreationUtcTime(dataList[7])
                        self.user2 = self.getEventDataUser(dataList[8])

                        self.eventData = {
                        
                            "RuleName" : self.ruleName2,
                            "UtcTime" : self.utcTime2,
                            "ProcessGuid" : self.processGUID2,
                            "ProcessId" : self.processId2,
                            "Image" : self.image2,             
                            "Target Filename" : self.targetFilename2,
                            "Create Utc Time" : self.creationUtcTime2,
                            "Product" : self.previousCreationUtcTime2,
                            "Company" : self.user2,
                           
                        }
                    
                        self.systemDict["Event Data"] = self.eventData

                        json.dump(self.systemDict,self.outJSON)
                        self.outJSON.write("\n")
                    

                    
                    
                    elif self.theSystemEventIDField == "3":
                        eventData = self.getEventDataSectionFields(fullRecord)
                        dataList = eventData.split("\n") 
                        self.ruleName3 = self.getEventDataRuleName(dataList[0])
                        self.utcTime3 = self.getEventDataUTCTime(dataList[1]) 
                        self.processGUID3 = self.getEventDataProcessGuid(dataList[2])
                        self.processId3 = self.getEventDataProcessId(dataList[3])
                        self.image3 = self.getEventDataImage(dataList[4]) 
                        self.user3 = self.getEventDataUser(dataList[5])
                        self.protocol3 = self.getEventDataProtocol(dataList[6])
                        self.initiated3 = self.getEventDataInitiated(dataList[7]) 
                        self.sourceIsIpv63 = self.getEventDataSourceIsIpv6(dataList[8])
                        self.sourceIp3 = self.getEventDataSourceIp(dataList[9])
                        self.sourceHostname3 = self.getEventDataSourceHostname(dataList[10]) 
                        self.sourcePort3 = self.getEventDataSourcePort(dataList[11])
                        self.sourcePortName3 = self.getEventDataSourcePortName(dataList[12])
                        self.destinationIsIpv63 = self.getEventDataDestinationIsIpv6(dataList[13]) 
                        self.destinationIp3 = self.getEventDataDestinationIp(dataList[14])
                        self.destinationHostname3 = self.getEventDataDestinationHostname(dataList[15])
                        self.destinationPort3 = self.getEventDataDestinationPort(dataList[16]) 
                        self.destinationPortName3 = self.getEventDataDestinationPortName(dataList[17]) 
                    
                        self.eventData = {
                    
                            "RuleName" : self.ruleName3,
                            "UtcTime" : self.utcTime3,
                            "ProcessGuid" : self.processGUID3,
                            "ProcessId" : self.processId3,
                            "Image" : self.image3,               
                            "User" : self.user3,
                            "Protocol" : self.protocol3,
                            "Initiated" : self.initiated3,
                            "SourceIsIpv6" : self.sourceIsIpv63,
                            "SourceIp" : self.sourceIp3,
                            "SourceHostname" : self.sourceHostname3,
                            "SourcePort" : self.sourcePort3,
                            "SourcePortName" : self.sourcePortName3,              
                            "DestinationIsIpv6" : self.destinationIsIpv63,
                            "DestinationIp" : self.destinationIp3,
                            "DestinationHostname" : self.destinationHostname3,
                            "DestinationPort" : self.destinationPort3,
                            "DestinationPortName" : self.destinationPortName3
                   
                        }

                        self.systemDict["Event Data"] = self.eventData

                        json.dump(self.systemDict,self.outJSON)
                        self.outJSON.write("\n")
                    

                    elif self.theSystemEventIDField == "5":

                        eventData = self.getEventDataSectionFields(fullRecord)
                        dataList = eventData.split("\n") 
                        self.ruleName5 = self.getEventDataRuleName(dataList[0])  
                        self.utcTime5 = self.getEventDataUTCTime(dataList[1]) 
                        self.processGUID5 = self.getEventDataProcessGuid(dataList[2])
                        self.processId5 = self.getEventDataProcessId(dataList[3])
                        self.image5 = self.getEventDataImage(dataList[4]) 
                        self.user5 = self.getEventDataUser(dataList[5])

                        self.eventData = {
                            "RuleName" : self.ruleName5,
                            "UtcTime" : self.utcTime5,
                            "ProcessGuid" : self.processGUID5,
                            "ProcessId" : self.processId5,
                            "Image" : self.image5,              
                            "User" : self.user5,       
                        }
                    
                        self.systemDict["Event Data"] = self.eventData

                        json.dump(self.systemDict,self.outJSON)
                        self.outJSON.write("\n")
                    
                    
                    elif self.theSystemEventIDField == "11":

                        eventData = self.getEventDataSectionFields(fullRecord)
                        dataList = eventData.split("\n")
                        self.ruleName3 = self.getEventDataRuleName(dataList[0])  
                        self.utcTime3 = self.getEventDataUTCTime(dataList[1]) 
                        self.processGUID3 = self.getEventDataProcessGuid(dataList[2])
                        self.processId3 = self.getEventDataProcessId(dataList[3])
                        self.image3 = self.getEventDataImage(dataList[4])
                        self.targetFilename3 = self.getEventDataTargetFilename(dataList[5])
                        self.creationUtcTime3 = self.getEventDataCreationUtcTime(dataList[6])
                        self.user3 = self.getEventDataUser(dataList[7])

                        self.eventData = {
                    
                            "RuleName" : self.ruleName3,
                            "UtcTime" : self.utcTime3,
                            "ProcessGuid" : self.processGUID3,
                            "ProcessId" : self.processId3,
                            "Image" : self.image3,
                            "TargetFilename" : self.targetFilename3,
                            "CreationUtcTime" : self.creationUtcTime3,
                            "User" : self.user3,

                        }
                    
                    
                        self.systemDict["Event Data"] = self.eventData

                        json.dump(self.systemDict,self.outJSON)
                        self.outJSON.write("\n")
                    

                    
                    elif self.theSystemEventIDField == "13":
                        eventData = self.getEventDataSectionFields(fullRecord)
                        dataList = eventData.split("\n")
                        self.ruleName13 = self.getEventDataRuleName(dataList[0])
                        self.eventType13 = self.getEventDataEventType(dataList[1])
                        self.utcTime13 = self.getEventDataUTCTime(dataList[2]) 
                        self.processGUID13 = self.getEventDataProcessGuid(dataList[3])
                        self.processId13 = self.getEventDataProcessId(dataList[4])
                        self.image13 = self.getEventDataImage(dataList[5])
                        self.targetObject13 = self.getEventDataTargetObject(dataList[6])
                        self.details13 = self.getEventDataDetails(dataList[7])

                        self.user13 = self.getEventDataUser(dataList[8])


                        self.eventData = {
                    
                        "RuleName" : self.ruleName13,
                        "EventType" : self.eventType13,
                        "UtcTime" : self.utcTime13,
                        "ProcessGuid" : self.processGUID13,
                        "ProcessId" : self.processId13,
                        "Image" : self.image13, 
                        "TargetObject" : self.targetObject13,
                        "Details" : self.details13, 
                        "User" : self.user13,
                    
                        }
                    
            
                    
                        self.systemDict["Event Data"] = self.eventData

                        json.dump(self.systemDict,self.outJSON)
                        self.outJSON.write("\n")
                    
                    
                    
                    elif self.theSystemEventIDField == "22":

                    

                        eventData = self.getEventDataSectionFields(fullRecord)
                        dataList = eventData.split("\n") 
                        self.ruleName22 = self.getEventDataRuleName(dataList[0])  
                        self.utcTime22 = self.getEventDataUTCTime(dataList[1]) 
                        self.processGUID22 = self.getEventDataProcessGuid(dataList[2])
                        self.processId22 = self.getEventDataProcessId(dataList[3])
                        self.queryName22 = self.getEventDataQueryName(dataList[4]) 
                        self.queryStatus22 = self.getEventDataQueryStatus(dataList[5]) 
                        self.queryResults22 = self.getEventDataQueryResults(dataList[6]) 
                        self.image22 = self.getEventDataImage(dataList[7]) 
                        self.user22 = self.getEventDataUser(dataList[8])
                    
                        self.eventData = {
                    
                            "RuleName" : self.ruleName22,
                            "UtcTime" : self.utcTime22,
                            "ProcessGuid" : self.processGUID22,
                            "ProcessId" : self.processId22,
                            "QueryName" : self.utcTime22,
                            "QueryStatus" : self.processGUID22,
                            "QueryResults" : self.processId22,
                            "Image" : self.image22,        
                            "User" : self.user22,
                    
                        }
                        self.systemDict["Event Data"] = self.eventData

                        json.dump(self.systemDict,self.outJSON)
                        self.outJSON.write("\n")
                    
                    
                    else:
                        pass

                    self.outJSON.close()

    def getSection(self,aString,beginTag,endTag):
            


            if beginTag==None:
                return 0
            elif endTag==None:
                return 0
            elif aString==None:
                return 0
            else:
                startTagString = re.search(str(beginTag),str(aString))


            if startTagString == None:
                    
                return " "

            else:

                startTagSpan = startTagString.span()
                    
            
            beginStartTagSpan, endStartTagSpan = startTagSpan



            self.endTagString = re.search(endTag,aString)

            if self.endTagString == None:

                return " "

            else:
        
                endTagSpan = self.endTagString.span()
        
            beginEndTagSpan, endEndTagSpan = endTagSpan       
        
            sl = aString[int(endStartTagSpan):int(beginEndTagSpan)]
            
            if sl == None:

                return " "

            else: 

                return sl

                
                

    def getField(self,strg):
        theRecord = strg[slice(1,-1,1)]
        
        c = self.getSection(theRecord,'>','<')
        
        #theF = f'"{c}"'
        return c

    def getAttribute(self,strg,b,e):
        theRecord = strg[slice(1,-1,1)]
        
        c = self.getSection(theRecord,b,e) 
        
        #theAttrib = f'"{c}"'
        return c

    def getRecJSON(self,num,systemInfo,eventDataInfo):
        
        s = '{ recnum : ' + '"(str(num))"' + ', system : ' + str(systemInfo) + ', eventDataInfo : ' + str(eventDataInfo) + ' }'
  
        return s
    def getSystemSectionFields(self,record):
        
        theSystemSection = self.getSection(record,'<System>','</System>')
        
        return theSystemSection
    
    def getEventDataSectionFields(self,record):
        theEventDataSectionRaw = self.getSection(record,"<EventData>","</EventData>")
        return theEventDataSectionRaw

    def getEventDataRuleName(self,theString):
        theRuleName = self.getSection(theString,"<Data Name=\"RuleName\">","</Data>")
        return theRuleName

    def getEventDataUTCTime(self,theString):
        utcTime = self.getSection(theString,"<Data Name=\"UtcTime\">","</Data>")
        return utcTime
    
    def getEventDataProcessGuid(self,theString):
        processGUID = self.getSection(theString,"<Data Name=\"ProcessGuid\">","</Data>")
        return processGUID

    def getEventDataProcessId(self,theString):
        ProcessId = self.getSection(theString,"<Data Name=\"ProcessId\">","</Data>")
        return ProcessId
    
    def getEventDataImage(self,theString):
        Image = self.getSection(theString,"<Data Name=\"Image\">","</Data>")
        return Image

    def getEventDataFileVersion(self,theString):
        FileVersion = self.getSection(theString,"<Data Name=\"FileVersion\">","</Data>")
        return FileVersion

    def getEventDataDescription(self,theString):
        Description = self.getSection(theString,"<Data Name=\"Description\">","</Data>")
        return Description

    def getEventDataProduct(self,theString):
        Product = self.getSection(theString,"<Data Name=\"Product\">","</Data>")
        return Product

    def getEventDataCompany(self,theString):
        Company = self.getSection(theString,"<Data Name=\"Company\">","</Data>")
        return Company

    def getEventDataOriginalFileName(self,theString):
        OriginalFileName = self.getSection(theString,"<Data Name=\"OriginalFileName\">","</Data>")
        return OriginalFileName

    def getEventDataCommandLine(self,theString):
        CommandLine = self.getSection(theString,"<Data Name=\"CommandLine\">","</Data>")
        return CommandLine

    def getEventDataCurrentDirectory(self,theString):
        CurrentDirectory = self.getSection(theString,"<Data Name=\"CurrentDirectory\">","</Data>")
        return CurrentDirectory

    def getEventDataUser(self,theString):
        User = self.getSection(theString,"<Data Name=\"User\">","</Data>")
        return User

    def getEventDataLogonGuid(self,theString):
        LogonGuid = self.getSection(theString,"<Data Name=\"LogonGuid\">","</Data>")
        return LogonGuid

    def getEventDataLogonId(self,theString):
        LogonId = self.getSection(theString,"<Data Name=\"LogonId\">","</Data>")
        return LogonId

    def getEventDataTerminalSessionId(self,theString):
        TerminalSessionId = self.getSection(theString,"<Data Name=\"TerminalSessionId\">","</Data>")
        return TerminalSessionId

    def getEventDataIntegrityLevel(self,theString):
        IntegrityLevel = self.getSection(theString,"<Data Name=\"IntegrityLevel\">","</Data>")
        return IntegrityLevel

    def getEventDataHashes(self,theString):
        Hashes = self.getSection(theString,"<Data Name=\"Hashes\">","</Data>")
        return Hashes

    def getEventDataParentProcessGuid(self,theString):
        ParentProcessGuid = self.getSection(theString,"<Data Name=\"ParentProcessGuid\">","</Data>")
        return ParentProcessGuid

    def getEventDataParentProcessId(self,theString):
        ParentProcessId = self.getSection(theString,"<Data Name=\"ParentProcessId\">","</Data>")
        return ParentProcessId

    def getEventDataParentImage(self,theString):
        ParentImage = self.getSection(theString,"<Data Name=\"ParentImage\">","</Data>")
        return ParentImage

    def getEventDataParentCommandLine(self,theString):
        ParentCommandLine = self.getSection(theString,"<Data Name=\"ParentCommandLine\">","</Data>")
        return ParentCommandLine

    def getEventDataParentUser(self,theString):
        ParentUser = self.getSection(theString,"<Data Name=\"ParentUser\">","</Data>")
        return ParentUser

    def getEventDataQueryName(self,theString):
        QueryName = self.getSection(theString,"<Data Name=\"QueryName\">","</Data>")
        return QueryName

    def getEventDataQueryStatus(self,theString):
        QueryStatus = self.getSection(theString,"<Data Name=\"QueryStatus\">","</Data>")
        return QueryStatus

    def getEventDataQueryResults(self,theString):
        QueryResults = self.getSection(theString,"<Data Name=\"QueryResults\">","</Data>")
        return QueryResults

    def getEventDataTargetFilename(self,theString):
        TargetFilename = self.getSection(theString,"<Data Name=\"TargetFilename\">","</Data>")
        return TargetFilename
    
    def getEventDataCreationUtcTime(self,theString):
        CreationUtcTime = self.getSection(theString,"<Data Name=\"CreationUtcTime\">","</Data>")
        return CreationUtcTime

    def getEventDataPreviousCreationUtcTime(self,theString):
        PreviousCreationUtcTime = self.getSection(theString,"<Data Name=\"PreviousCreationUtcTime\">","</Data>")
        return PreviousCreationUtcTime
  
    def getEventDataProtocol(self,theString):
        Protocol = self.getSection(theString,"<Data Name=\"Protocol\">","</Data>")
        return Protocol

    def getEventDataInitiated(self,theString):
        Initiated = self.getSection(theString,"<Data Name=\"Initiated\">","</Data>")
        return Initiated

    def getEventDataSourceIsIpv6(self,theString):
        SourceIsIpv6 = self.getSection(theString,"<Data Name=\"SourceIsIpv6\">","</Data>")
        return SourceIsIpv6

    def getEventDataSourceIp(self,theString):
        SourceIp = self.getSection(theString,"<Data Name=\"SourceIp\">","</Data>")
        return SourceIp

    def getEventDataSourceHostname(self,theString):
        SourceHostname = self.getSection(theString,"<Data Name=\"SourceHostname\">","</Data>")
        return SourceHostname

    def getEventDataSourcePort(self,theString):
        SourcePort = self.getSection(theString,"<Data Name=\"SourcePort\">","</Data>")
        return SourcePort

    def getEventDataSourcePortName(self,theString):
        SourcePortName = self.getSection(theString,"<Data Name=\"SourcePortName\">","</Data>")
        return SourcePortName

    def getEventDataDestinationIsIpv6(self,theString):
        DestinationIsIpv6 = self.getSection(theString,"<Data Name=\"DestinationIsIpv6\">","</Data>")
        return DestinationIsIpv6

    def getEventDataDestinationIp(self,theString):
        DestinationIp = self.getSection(theString,"<Data Name=\"DestinationIp\">","</Data>")
        return DestinationIp

    def getEventDataDestinationHostname(self,theString):
        DestinationHostname = self.getSection(theString,"<Data Name=\"DestinationHostname\">","</Data>")
        return DestinationHostname

    def getEventDataDestinationPort(self,theString):
        DestinationPort = self.getSection(theString,"<Data Name=\"DestinationPort\">","</Data>")
        return DestinationPort

    def getEventDataDestinationPortName(self,theString):
        DestinationPortName = self.getSection(theString,"<Data Name=\"DestinationPortName\">","</Data>")
        return DestinationPortName
    
    def getEventDataEventType(self,theString):
        EventType = self.getSection(theString,"<Data Name=\"EventType\">","</Data>")
        return EventType

    def getEventDataTargetObject(self,theString):
        TargetObject = self.getSection(theString,"<Data Name=\"TargetObject\">","</Data>")
        return TargetObject

    def getEventDataDetails(self,theString):
        Details = self.getSection(theString,"<Data Name=\"Details\">","</Data>")
        return Details
 

    def getSystemProviderName(self,theString):
        provider = self.getSection(theString,"<Provider Name=","/>")
        providerName = self.getSection(provider,"<Provider Name=","Guid=")
        #providerGUID = self.getSection(provider,'Guid="','">')
        return providerName

    def getSystemProviderGUID(self,theString):
        provider = self.getSection(theString,"\<Provider Name\=","\/>")
        #providerName = self.getSection(provider,'Name="','" Guid=')
        providerGUID = self.getSection(provider,"Guid=","\">")
        return providerGUID
    
    def getSystemEventIDField(self,theString):

        #<EventID Qualifiers="">
        startS = '<EventID Qualifiers=??'
        endS = '</EventID>'
        eventID = self.getSection(theString,startS,endS)
        
        return eventID

    def getSystemVersionField(self,theString):
        version = self.getSection(theString,'<Version>','</Version>')
        return version

    def getSystemLevelField(self,theString):
        level = self.getSection(theString,'<Level>','</Level>')
        return level

    def getSystemTaskField(self,theString):
        task = self.getSection(theString,'<Task>','</Task>')
        return task 

    def getSystemOpcodeField(self,theString):
        opcode = self.getSection(theString,'<Opcode>','</Opcode>')
        return opcode

    def getSystemKeywordsField(self,theString):
        keywords = self.getSection(theString,'<Keywords>','</Keywords>')
        return keywords

    def getSystemTimeCreatedFields(self,theString):                
        timeCreated = self.getSection(theString,'<TimeCreated','</TimeCreated>')
        timeCreatedSystemTime = self.getSection(timeCreated,' SystemTime=\"','">')
        return timeCreatedSystemTime

    #def getSystemEventRecordIDField(self,theString):               
        #eventRecordID = self.getSection(theString,'<EventRecordID>','</EventRecordID>')
        #return eventRecordID

    def getSystemEventRecordIDField(self,theString):               
        eventRecordID = self.getSection(theString,'<EventRecordID>','</EventRecordID>')
        return eventRecordID


    def getSystemCorrelationActivityIDField(self,theString):               
        correlation = self.getSection(theString,'<Correlation ','</Correlation>')
        #print("THE CORRELATION2 STRING: " + theString,file=sys.stderr)
        correlationActivityID = self.getSection(correlation,'ActivityID="','\" RelatedActivityID')
        #correlationRelatedActivityID = self.getSection(correlation,' RelatedActivityID=\"','">')
        return correlationActivityID

    def getSystemCorrelationRelatedActivityIDField(self,theString):               
        correlation = self.getSection(theString,'<Correlation ','</Correlation>')
        #print("THE CORRELATION STRING: " + theString,file=sys.stderr)
        #correlationActivityID = self.getSection(correlation,'ActivityID="','\" RelatedActivityID')
        correlationRelatedActivityID = self.getSection(correlation,' RelatedActivityID=\"','">')
        return correlationRelatedActivityID
    
    def getSystemExecutionProcessIDField(self,theString):
        execution = self.getSection(theString,'<Execution ','</Execution>')
        executionProcessID = self.getSection(execution,'ProcessID=\"','\" ThreadID')
        #executionThreadID = self.getSection(execution,'ThreadID="','\">')
        return executionProcessID

    def getSystemExecutionThreadField(self,theString):
        execution = self.getSection(theString,'<Execution ','</Execution>')
        #executionProcessID = self.getSection(execution,'ProcessID=\"','\" ThreadID')
        executionThreadID = self.getSection(execution,'ThreadID="','\">')
        return executionThreadID

    def getSystemChannelField(self,theString):
        channel = self.getSection(theString,'<Channel>','</Channel>')
        return channel

    def getSystemComputerField(self,theString):
        computer = self.getSection(theString,'<Computer>','</Computer>')
        return computer


    def getSystemSecurityFields(self,theString):               
        security = self.getSection(theString,'<Security ','</Security>')
        securityUserID = self.getSection(security,'UserID=\"','\">')
        return securityUserID 
    
    def readEvents(self):
        pass
    '''
    def getSection(self,aString,beginTag,endTag):
       

           
            


            if beginTag==None:
                return 0
            elif endTag==None:
                return 0
            elif aString==None:
                return 0
            else:
                startTagString = re.search(str(beginTag),str(aString))


            if startTagString == None:
                    
                return '""'

            else:

                startTagSpan = startTagString.span()
                    
            
            beginStartTagSpan, endStartTagSpan = startTagSpan



            self.endTagString = re.search(endTag,aString)

            if self.endTagString == None:

                return '""'

            else:
        
                endTagSpan = self.endTagString.span()
        
            beginEndTagSpan, endEndTagSpan = endTagSpan       
        
            sl = aString[int(endStartTagSpan):int(beginEndTagSpan)]
            
            if sl == None:

                return " "

            else: 

                return sl'''
