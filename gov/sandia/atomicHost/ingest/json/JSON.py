import json

class EventsArray:

	def __init__(self,filename):
		self.filename = filename
		self.data = []

	def getData(self):
		f = open(self.filename,'r')
		self.data = json.load(f)
		f.close()
		return self.data

