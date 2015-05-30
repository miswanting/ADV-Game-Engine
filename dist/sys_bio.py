#coding=utf-8
'''
This file provides the following several classes:
	BIOFileLoader
		path
			Type: String
			defined when load() run. Refers to the relative path of the loaded file.
		dir
			Type: String
			defined when load() run. Refers to the relative directory of the loaded file.
		filename
			Type: String
			defined when load() run. Refers to the filename of the loaded file.
		content
			Type: List
			defined when load() run. Refers to the content of the loaded file.

		__init__()
			Does nothing.
		load(path)
			Load specific file. And there is no return data.
			path: This parameter needs accurate path which contains direction, name and extension.
		save()
			Save current file data. And there is no return data.
	BIOFolderLoader
		dir
		content

		__init__()
		new(path)
		load(dir)
		getPath()
		getEveryContentFile(withPath = False)
		getEveryContentFolder(withPath = False)
		refresh()
'''
import os
class PathManager(object):
	"""
	Now this class is just for class-BIOFolderLoader.
	"""
	path = ''
	dir = ''
	# story\
	fileName = ''
	# test.tp
	extension = ''
	# tp
	def __init__(self):
		#super(, self).__init__()
		#self.arg = arg
		pass

	# Public function
	def setPath(self, newPath):
		self.path = newPath
		self.breakPath()
		# print('setPath:'+newPath,self.dir,self.fileName)
	def setDir(self, newDir):
		self.dir = newDir
		self.generatePath()
	def setFileName(self, newFileName):
		self.fileName = newFileName
		self.extension = newFileName.split('.')[1]
		self.generatePath()

	# Private function
	def generatePath(self):
		self.path = self.dir + '\\' +self.fileName
	def breakPath(self):
		tmp = self.path.split('\\')
		self.dir, self.fileName = os.path.split(self.path)
		self.extension = tmp[-1].split('.')[1]
class BIOFileLoader:
	path = ''
	dir = ''
	fileName = ''
	content = []
	def __init__(self):
		pass
	#一级函数
	def load(self, path):
		self.path = path
		self.dir, self.fileName = os.path.split(self.path)
		if os.path.exists(self.path):
			self.content = []
			file = open(self.path)
			raw_content = file.readlines()
			file.close()
			for line in raw_content:
				if line[-1] == '\n':
					self.content.append(line[0:-1])
				else:
					self.content.append(line)
		else:
			print('[WARN]There is no file named: \'' + self.path + '\'')
	def save(self):
		file = open(self.path, 'w')
		# print(self.content,self.path)
		for line in self.content:
			file.writelines(line + '\n')
		file.close()
class BIOFolderLoader(object):
	'''
	load:CD to a new directory.
	new:New a file in current directory.
	delete:Delete a file in current directory.
	setPath:CD to a new directory and set a pre-fileName.
	getEveryContentFile:Get a list of every file contented.
	getEveryContentFolder:Get a list of every folder contented.
	refresh:Reload current directory.
	TODO Built in class-BIOFileLoader.
	'''
	path = PathManager()
	content = []
	def __init__(self):
		pass
	#一级函数
	def new(self, fileName = path.fileName):
		self.path.setFileName(fileName)
		if not os.path.exists(self.path.path):
			file = open(self.path.path, 'w')
			file.close()
		# print('new:'+fileName)
	def delete(self, fileName = path.fileName):
		pass
	def load(self, dir = path.dir):
		self.path.setDir(dir)
		self.content = os.listdir(self.path.dir)
		# print('load:'+dir,self.path.dir,self.content)
	def setPath(self, path):
		self.path.setPath(path)
	def getEveryContentFile(self, withPath = False):
		tmp = []
		for each in self.content:
			if os.path.isfile(self.getPath(each)):
				if withPath:
					tmp.append(self.getPath(each))
				else:
					tmp.append(each)
		return tmp
	def getEveryContentFolder(self, withPath = False):
		tmp = []
		for each in self.content:
			if os.path.isdir(self.getPath(each)):
				if withPath:
					tmp.append(self.getPath(each))
				else:
					tmp.append(each)
		return tmp
	def refresh(self):
		self.load(self.path.dir)
	#二级函数
	def getPath(self, fileName):
		return self.path.dir + fileName

if __name__ == '__main__':
	A = BIOFileLoader()
	B = BIOFolderLoader()
	C = PathManager()
	A.load('story\\test.tp')
	print(A.content)
