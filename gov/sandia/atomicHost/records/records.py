import os
import os.path

class AHEventRecords:

	def __init__(self,jsonFromEvtxFile):
		self.jsonFileFromEvtx = jsonFromEvtxFile

	def makeAHEventRecords(self):
		pass
	
	def createAHEventRecordsDict(self,jsonFromEvtxFile):
		#print(jsonFromEvtxFile)
		f = open(jsonFromEvtxFile,"r")
		rawRecords = f.read()
		return rawRecords

	def createDictFromList(self,theList,firstKey):
		aDict = {}
		s = '{ "' + firstKey + '" : ' + theList + ' }'
		aDict = eval(s)
		return aDict

	def addUniqueIDToDictsInList(self,aList,prefix):
		aDict = {}
		count = 0
		newListAsString = ""
		#print(aList)
		outList = []
		for rec in aList:
			count = count + 1
			#print(rec)
			newRec = '{ "' + prefix + '_' + str(count) + '" : ' + str(rec) + '}'
			outList.append(newRec)
		return outList

	def getAmendedDict(self):
		rawRecords = self.createAHEventRecordsDict(self.jsonFileFromEvtx)
		dataDict = self.createDictFromList(rawRecords,"data")
		theListOfRecords = dataDict["data"]
		amendedListOfRecords = self.addUniqueIDToDictsInList(theListOfRecords,"event")

		return amendedListOfRecords

class AHEventRecord:

	def __init__(self,rec):
		self.aRecord_Dict = {}
		self.recordAsDict = eval(rec)
		self.recordPrimaryKey = list(self.recordAsDict)[0]
		self.coreDataInRecordAsDict = self.recordAsDict[self.recordPrimaryKey]
		self._modUTCInCore()

	def _modUTCInCore(self):
		utc = self.coreDataInRecordAsDict["UtcTime"]
		iso = utc.replace(" ","T")
		self.coreDataInRecordAsDict["IsoTime"] = iso
		del self.coreDataInRecordAsDict["UtcTime"]


		'''
		if data['EventId']==1:

			self.detectInfo = self.ah1082SubTechniqueInfo["detect"]
			infoLabels = list(self.detectInfo)
			for g in infoLabels:
				print(str(g))

			for i in infoLabels:
				recGuidID = uuid.uuid4()
				detectLabels = self.detectInfo[str(i)]
				originalFileName = detectLabels["originalFileName"]
				commandLine = detectLabels[str("commandLine")]
				image = detectLabels["image"]
				detector = Discovery(data, currentKey)
				result = detector.isMatch(originalFileName,commandLine,image)
				if result:
					ahguid = self.detectInfo[i]["ahGUID"]
					artguid = self.ah1082SubTechniqueInfo["guid"]
					u = uuid.uuid4()
					newRec = eval(rec)
					eventNum = list(newRec)[0]
					theIdentifiedRecord = newRec[eventNum]
					utc = theIdentifiedRecord["UtcTime"]
					iso = utc.replace(" ","T")
					theIdentifiedRecord["IsoTime"] = iso
					del theIdentifiedRecord["UtcTime"]
					theIdentifiedRecord["Atomic-Host-Record-ID"] = str(u)
					theIdentifiedRecord["Atomic-Host-GUID"] = str(ahguid)
					theIdentifiedRecord["Atomic-Red-Team-GUID"] = str(artguid)
					self.taggedEventsOutputDictionary[str(recGuidID)] = theIdentifiedRecord'''