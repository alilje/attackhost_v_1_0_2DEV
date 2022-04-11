from os import path
from json import loads
class SysmonFileVIAConvertToJSON:

	def __init__(self,file):

		self.filename = file
		f = open(self.filename)
		self.jsonOut = loads(f)


	def printAll(self):
		print(type(self.jsonOut[0]))

	def printKeys(self):
		print(self.jsonOut)



a = SysmonFileVIAConvertToJSON('D:/atomichost-git/data/input/2021.07.29.1437sysmon-data.json')
