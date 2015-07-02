#coding=utf-8

'''
The format of this code is advocated!
'''

import os

class BIOS:

	'''
	new(path):
		New a file.
	delete(path):
		Delete a file.
	load(path):
		Load a file.
	save(file):
		Save a file.
	getEveryFileByDir(withPath = False):
		Get a list of every file with data.
	getEveryFolderByDir(withPath = False):
		Get a list of every folder.
	'''

	# Public function
	def new(self, path, content = []):
		dir, fileName = os.path.split(path)
		self.save([dir, fileName, content])

	def delete(self, path):
		pass

	def load(self, path):
		dir, fileName = os.path.split(path)
		if os.path.exists(path):
			file = open(path)
			raw_content = file.readlines()
			file.close()
			content = []
			for line in raw_content:
				if line[-1] == '\n':
					content.append(line[0:-1])
				else:
					content.append(line)
			return [dir, fileName, content]
		else:
			print('[WARN]There is no file named: \'' + self.path + '\'')

	def save(self, file):
		path = file[0] + '\\' + file[1]
		file = open(path, 'w')
		# print(self.content,self.path)
		for line in file[2]:
			file.writelines(line + '\n')
		file.close()

	def getEveryFileByDir(self, dir):
		list = os.listdir(dir)
		fileList = []
		for each in list:
			if os.path.isfile(dir + '\\' + each):
				fileList.append(self.load(dir + '\\' + each))
		return fileList

	def getEveryFolderByDir(self, dir):
		list = os.listdir(dir)
		folderList = []
		for each in list:
			if os.path.isdir(dir + '\\' + each):
				folderList.append([dir, each])
		return folderList

if __name__ == '__main__':
	I = BIOS()
	print(I.load('story\\test.tp')[0] + '\\' + I.load('story\\test.tp')[1])
	print(I.getEveryFileByDir('story'))
	print(I.getEveryFolderByDir('story'))
