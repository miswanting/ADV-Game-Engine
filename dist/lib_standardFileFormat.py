#coding=utf-8
import sys_bio
class mapLoader:
	file = sys_bio.BIOFileLoader()
	def __init__(self):
		pass
	def load(self, path):
		self.file.load(path)
	def save(self):
		self.file.save()
	def getFileName(self):
		return self.file.fileName
	def replaceContentBySection(self, section, content):
		currentSection = ''
		newContent = []
		ignore = False
		for line in self.file.content:
			if line[0] == '[':
				flag1, flag2 = 0, line.find(']')
				if flag2 != -1:
					while line[flag1 + 1] == ' ':
						flag1 += 1#'_|_s'
					while line[flag2 - 1] == ' ':
						flag2 -= 1#'n|_'
					currentSection = line[flag1 + 1:flag2]
					if currentSection == section:
						ignore = True
						newContent.extend(content)
					else:
						ignore = False
				else:
					print('[WARN]Broken data in: \'' + self.file.path + '\'')
			elif not ignore:
				newContent.append(line)
		self.file.content = newContent
	def getContentBySection(self, section):
		section_found = False
		content = []
		currentSection = ''
		for line in self.file.content:
			if line != '':
				if line[0] == '[':
					flag1, flag2 = 0, line.find(']')
					if flag2 != -1:
						while line[flag1 + 1] == ' ':
							flag1 += 1#'_|_s'
						while line[flag2 - 1] == ' ':
							flag2 -= 1#'n|_'
						currentSection = line[flag1 + 1:flag2]
					else:
						print('[WARN]Broken data in: \'' + self.file.path + '\'')
				elif currentSection == section:
					section_found = True
					content.append(line)
			else:
				content.append(line)
		if not section_found:
			print('[WARN]There is no section: \'' + section + '\' in file: \'' + self.file.path + '\'')
		return content
	def getText(self):
		return self.getContentBySection('text')
	def getCode(self):
		return self.getContentBySection('code')
	def replaceText(self, newText):
		self.replaceContentBySection(text, newText)
	def replaceCode(self, newCode):
		self.replaceContentBySection(code, newCode)
class infoLoader:
	file = sys_bio.BIOFileLoader()
	def __init__(self):
		pass
	def load(self, path):
		self.file.load(path)
	def save(self):
		self.file.save()
	def setValueByEntry(self, entry, value, section = ''):
		value = str(value)
		currentSection = ''
		newData = []
		section_found = False
		entry_found = False
		for line in self.file.content:
			if line[0] == '[':
				flag1, flag2 = 0, line.find(']')
				if flag2 != -1:
					while line[flag1 + 1] == ' ':
						flag1 += 1#'_|_s'
					while line[flag2 - 1] == ' ':
						flag2 -= 1#'n|_'
					currentSection = line[flag1 + 1:flag2]
					newData.append('[ ' + currentSection + ' ]')
				else:
					print('[WARN]Broken data in:' + self.file.path + '\'')
			elif currentSection == section:
				section_found = True
				if line.find('=') != -1:
					flag1, flag2, flag3, flag4 = 0, line.find('='), line.find('='), len(line)
					while line[flag1] == ' ':
						flag1 += 1#'_|e'
					while line[flag2 - 1] == ' ':
						flag2 -= 1#'y|_'
					while line[flag3 + 1] == ' ':
						flag3 += 1#'_|_v'
					while line[flag4 - 1] == ' ':
						flag4 -= 1#'e|_'
					if line[flag1:flag2] == entry:
						entry_found = True
						newData.append(line[flag1:flag2] + ' = ' + value)
					else:
						newData.append(line[flag1:flag2] + ' = ' + line[flag3 + 1:flag4])
		if not section_found:
			newData.append('[ ' + section + ' ]')
		self.file.content = newData
		if not entry_found:
			currentSection = ''
			newData = []
			for line in self.file.content:
				if line[0] == '[':
					flag1, flag2 = 0, line.find(']')
					if flag2 != -1:
						while line[flag1 + 1] == ' ':
							flag1 += 1#'_|_s'
						while line[flag2 - 1] == ' ':
							flag2 -= 1#'n|_'
						currentSection = line[flag1 + 1:flag2]
						newData.append('[ ' + currentSection + ' ]')
						if currentSection == section:
							newData.append(entry + ' = ' + value)
					else:
						print('[WARN]Broken data in:' + self.file.path + '\'')
				else:
					newData.append(line)
			self.file.content = newData
	def getValueByEntry(self, entry, section = ''):
		section_found = False
		entry_found = False
		currentSection = ''
		for line in self.file.content:
			if line[0] == '[':
				flag1, flag2 = 0, line.find(']')
				if flag2 != -1:
					while line[flag1 + 1] == ' ':
						flag1 += 1#'_|_s'
					while line[flag2 - 1] == ' ':
						flag2 -= 1#'n|_'
					currentSection = line[flag1 + 1:flag2]
				else:
					print('[WARN]Broken data in: \'' + self.file.path + '\'')
			elif currentSection == section:
				section_found = True
				if line.find('=') != -1:
					flag1, flag2, flag3, flag4 = 0, line.find('='), line.find('='), len(line)
					while line[flag1] == ' ':
						flag1 += 1#'_|e'
					while line[flag2 - 1] == ' ':
						flag2 -= 1#'y|_'
					while line[flag3 + 1] == ' ':
						flag3 += 1#'_|_v'
					while line[flag4 - 1] == ' ':
						flag4 -= 1#'e|_'
					if line[flag1:flag2] == entry:
						entry_found = True
						return line[flag3 + 1:flag4]
		if not section_found:
			print('[WARN]There is no section: \'' + section + '\' in file: \'' + self.file.path + '\'')
		elif not entry_found:
			print('[WARN]There is no entry: \'' + entry + '\' in section: \''+ section + '\' in file: \'' + self.file.path + '\'')
	def addValueByEntry(self, entry, section = '', addend = 1):
		value = self.getValueByEntry(entry, section)
		if value.isdigit():
			newValue = int(value) + addend
			self.setValueByEntry(entry, newValue, section)
		else:
			print('[WARN]The custom variables:\'' + entry + '\' in section: \'' + section + '\' in file: \'' + self.file.path + '\' is not numbers!')
if __name__ == '__main__':
	I = infoLoader()
	I.load('save\sys.save')
	print(I.file.content)
	I.setValueByEntry('name', 'YYY', 'value')
	print(I.getValueByEntry('name', 'value'))
	I.setValueByEntry('age', 18, 'value')
	print(I.getValueByEntry('age', 'value'))
	I.addValueByEntry('age', 'value', -1)
	print(I.getValueByEntry('age', 'value'))
	I.save()
