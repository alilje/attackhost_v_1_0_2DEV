import os
import os.path
from gov.sandia.atomicHost.datestimes.files import FileSuffix
import subprocess
import datetime

class AHEventsFile:
	def __init__(self,globalConfigInfo):
		# This is the global configuration information
		self.globalConfigInfo = globalConfigInfo
		# this is the Windows Event File you are using. It will normall have the file extension .evtx
		self.inputWindowsEventFile = self.globalConfigInfo["tagged-workflow-input-evtx-file"]
		# This is the directory name where JSON output from an .evtx file will be saved. This can be set in the .yaml file
		self.jsonFromEventsDirectoryName = self.globalConfigInfo['events-as-json-from-evtx-output-dir']
		# This is the absolute path to the JSON file from EVTX
		self.absolutePath2JSONFromEventsFile = self._getABSPathJSONOutputFileName()
		self.psForEvents2JSON = self.globalConfigInfo['ps-for-events-to-JSON-from-evtx']
		self.absolutePathForPSEventsToJSON = os.path.join(self.globalConfigInfo['powershell-directory'],self.psForEvents2JSON).replace("\\","/")

	def _getFileDateTimeSequence(self):
		"""

		:rtype: object
		"""
		theDate = datetime.datetime.now()
		theDateSequence = str(theDate.year) + str(theDate.month) + str(theDate.day)
		theTimeSequence = str(theDate.hour) + str(theDate.day) + str(theDate.minute) + str(theDate.second) + str(theDate.microsecond)
		theMergedSequence = theDateSequence + "-" + theTimeSequence
		return theMergedSequence

	def _getABSPathJSONOutputFileName(self):
		outputFileForJsonFromEVTX = os.path.join(self.jsonFromEventsDirectoryName,self.globalConfigInfo['events-as-json-from-evtx-output-filename']).replace('\\','/')
		return outputFileForJsonFromEVTX

	def getJSONFromEVTXFile(self):
		self.eventFileName = self.inputWindowsEventFile
		self.jsonFileName = self.absolutePath2JSONFromEventsFile
		command = self.absolutePathForPSEventsToJSON + " " + self.eventFileName + " " + self.jsonFileName
		p = subprocess.Popen(['powershell.exe', command])
		p.wait()

class AHEvent:
	def __init__(self):
		pass




class AHEvents2JSONFile:


	def __init__(self,powershelldir):
		self.eventFileName = ""
		self.jsonFileName = ""
		self.powershelldir = powershelldir

	def getJSONFromEVTXFile(self,eventFileName,jsonFileName):
		self.eventFileName = eventFileName
		self.jsonFileName = jsonFileName
		self.eventFileName = eventFileName

		self.jsonFileName = jsonFileName
		aPath = os.path.join(self.powershelldir,"getEventsInFile.ps1").replace('/',"\\")
		command = aPath + " " + self.eventFileName + " " + self.jsonFileName
		p = subprocess.Popen(['powershell.exe', command])
		p.wait()


class AHTaggedJSONFile:

	def __init__(self,outputFile):
		self.outputFile = outputFile

	def writeTaggedEventJSONFileHeader(self):
		g = open(self.outputFile,"w")
		g.write('{ "detection-results" : [')
		g.close()
