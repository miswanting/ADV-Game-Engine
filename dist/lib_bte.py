#coding=utf-8
'''
This file provides the following several classes:
	
'''
import lib_standardFileFormat
class BTextEditor:
	isRunning = True
	isCoding = True
	file = lib_standardFileFormat.mapLoader()
	def __init__(self):
		pass
	#一级函数
	def load(self, path):
		self.file.load(path)
	def save(self):
		self.file.save()
	def run(self):
		self.display()
		if self.isRunning:
			self.loop()
	#二级函数
	def loop(self):
		cmd = input('>')
		self.doWithCmd(cmd)
		self.display()
	#三级函数
	def doWithCmd(self, cmd):
		if self.isCoding:
			pass
		else:
			if cmd == '`back':
				self.isCoding = False
	def display(self):
		text = self.numberList(self.file.getText())
		for line in text:
			print(line)
		print('---------------------------------')
		code = self.numberList(self.file.getCode())
		for line in code:
			print(line)
	#四级函数
	def numberList(self, list):
		currentNumber = 1
		textList = []
		for each in list:
			textList.append(str(currentNumber) + ':\t' + each)
			currentNumber += 1
		return textList
	def getUnitNameByNumber(self, list, numberAsString):
		currentNumber = 1
		if numberAsString.isdigit():
			for each in list:
				if str(currentNumber) == numberAsString:
					return each
				currentNumber += 1
			print('[WARN]... I have nothing to say...')
		else:
			print('[WARN]Function only recive story number as string!')
if __name__ == '__main__':
	A = BTextEditor()
	