#coding=utf-8

import time

import lib_standardFileFormat

class mapCloud:
	'''
	This class is used to manage the story line.
	'''
	cloud = []
	initMap = ''
	cloudBranch = []
	cloudEnd = []
	cloudDir = ''
	targetList = []
	def __init__(self):
		pass
	# Public function
	def setCloudDir(self, dir):
		self.cloudDir = dir
	def setInitMap(self, initMap):
		self.initMap = initMap
	def addToCloud(self, cloud):
		if not self.isExist(cloud.fileName):
			self.cloud.append(cloud)
	def delFromCloudByFileName(self, fileName):
		pass
	def generate(self):
		self.refresh(True)
	def refresh(self, isAll = False):
		if isAll:
			self.cloud = []
			self.chainMap(self.initMap)
			self.obChainMap()
			self.generateTag()
	def getNextMap(self, mapName):
		for each in self.cloud:
			if each.fileName == mapName:
				return each.nextMaps
	def getLastMap(self, mapName):
		for each in self.cloud:
			if each.fileName == mapName:
				return each.lastMaps
	# Private function
	def isExist(self, fileName):
		cloud_found = False
		for each in self.cloud:
			if each.fileName == fileName:
				cloud_found = True
		if cloud_found:
			return True
		else:
			return False
	def chainMap(self, startMapName):
		self.targetList = [startMapName]
		while self.targetList != []:
			self.chainMapUnit()
	def obChainMap(self):
		for each in self.cloud:
			for every in self.cloud:
				for everyMap in every.nextMaps:
					if each.fileName == everyMap:
						each.addLastMap(every.fileName)
	def generateTag(self):
		for each in self.cloud:
			if each.lastMaps == []:
				each.addTag('start')
			if each.nextMaps == []:
				each.addTag('end')
			if len(each.lastMaps) > 1:
				each.addTag('retrain')
			if len(each.nextMaps) == 1 and each.nextMaps[0] == each.fileName:
				each.addTag('~~Dangerous circle~~')
	def chainMapUnit(self):
		newUnit = mapCloudUnit()
		newUnit.reset()
		newUnit.extractFromFile(self.cloudDir + self.targetList[0])
		self.targetList.pop(0)
		self.addToCloud(newUnit)
		if newUnit.nextMaps != []:
			for each in newUnit.nextMaps:
				if not self.isExist(each):
					list_found = False
					for every in self.targetList:
						if every == each:
							list_found = True
					if not list_found:
						self.targetList.append(each)
		else:
			print('[WARN]There is no next map.')
class mapCloudUnit:
	'''
	This class is used to be an abstract model of every map.
	'''
	lastMaps = []
	nextMaps = []
	tag = []#tag = branch, start, end, the_end, retrain, input
	fileName = ''
	filePath = ''
	mapLoader = lib_standardFileFormat.mapLoader()
	def __init__(self):
		pass
	def reset(self):
		self.lastMaps = []
		self.nextMaps = []
		self.tag = []
		self.fileName = ''
		self.filePath = ''
	def extractFromFile(self, path):
		self.filePath = path
		self.mapLoader.load(self.filePath)
		self.fileName = self.mapLoader.getFileName()
		code = self.mapLoader.getCode()
		for line in code:
			if line.find('= ') != -1:
				self.addTag('input')
			if line.find('the_end') != -1:
				self.addTag('the_end')
			if line.find('goto') != -1:
				flag = line.find('goto')
				flag += 5
				self.addNextMap(line[flag:] + '.map')
		if len(self.nextMaps) > 1:
			self.addTag('branch')
	def addLastMap(self, newMap):
		hasFound = False
		for each in self.lastMaps:
			if each == newMap:
				hasFound = True
		if not hasFound:
			self.lastMaps.append(newMap)
	def addNextMap(self, newMap):
		hasFound = False
		for each in self.nextMaps:
			if each == newMap:
				hasFound = True
		if not hasFound:
			self.nextMaps.append(newMap)
	def addTag(self, newTag):
		hasFound = False
		for each in self.tag:
			if each == newTag:
				hasFound = True
		if not hasFound:
			self.tag.append(newTag)
if __name__ == '__main__':
	# 实例化
	I = mapCloud()
	# Set cloud dir.
	I.setCloudDir('story\\老头の穿越之旅：血阳城\\')
	# Set entry map.
	I.setInitMap('init.map')
	# Start analyzing.
	I.generate()
	# Show every chained map.
	for each in I.cloud:
		print(each.nextMaps)
