import os
import os.path
from gov.sandia.atomicHost.filesystem.conventions.normPaths import PathHelper

class Folder:

	def __init__(self):
		self.name = ""


	def createDir(self,name):
		self.name = name
		self.replacebackslashes(self.name)
		
		if not os.path.exists(self.name):
			os.mkdir(self.name)

	def replacebackslashes(self, name):
		pathfix = PathHelper()
		self.name = pathfix.toPosix(self.name)


	def checkDirs(self,name):
		self.name = name
		if os.path.exists(self.name):
			return
		else:
			os.mkdir(self.name)

	