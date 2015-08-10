#coding=utf-8

import os
import time

import lib_standardDataFormat

class Game:
	'''
	1. Read save data.
	2. Load map.
	3. Show text.
	4. Generate code.
	5. Handle user input.
	'''
	isRunning = True
	currentSavePath = 'save'
	currentMapPath = 'story\\老头の穿越之旅：血阳城'
	currentSave = 'sys.save'
	currentMap = 'init.map'
	saveLoader = lib_standardDataFormat.infoLoader()
	mapLoader = lib_standardDataFormat.mapLoader()
	readin = ''
	def __init__(self):
		os.system('title Crazy_Engine(ADV)[Beta]')
		self.readSave()

	def readSave(self):
		self.saveLoader.load(self.currentSavePath, self.currentSave)
	def run(self):
		while self.isRunning:
			os.system('cls')
			#time.sleep(1)
			self.mapLoader.load(self.currentMapPath, self.currentMap)
			self.handleMap()
	def handleMap(self):
		for line in self.mapLoader.getText():
			print(self.showValue(line) + '\n')
		for line in self.mapLoader.getCode():
			cmd = line.split(' ')
			self.handleCMD(cmd)
		if self.readin == 'qs':
			self.saveGame()
	def handleCMD(self, cmd):
		if cmd[0] == 'goto':
			self.readin = 'None'
			self.currentMap = cmd[1] + '.map'
		elif cmd[0] == 'echo':
			print(cmd[1])
		elif cmd[0] == 'input':
			self.readin = input('>')
			if self.readin == '':
				self.readin = 'None'
		elif cmd[0] == '=':
			if self.readin != 'None':
				self.saveLoader.setValueByEntry(cmd[1], self.readin, 'value')
		elif cmd[0] == 'wait':
			if cmd[1].isdigit():
				time.sleep(int(cmd[1]))
			else:
				print('[WARN]等待时间不能设置为数字！')
		elif cmd[0] == 'title':
			os.system(each)
		elif cmd[0] == 'if':
			value, newCMD = cmd[1], cmd[2:]
			if value.find('=') != -1:
				value1, value2 = value.split('=')
				if value1 == 'input':
					value1 = self.readin
				else:
					value1 = self.saveLoader.getValueByEntry(value1, 'value')
				if not value2.isdigit():
					value2 = self.saveLoader.getValueByEntry(value2, 'value')
				if value1 == value2:
					self.handleCMD(newCMD)
			elif value.find('>') != -1:
				isError = False
				value1, value2 = value.split('>')
				if value1 == 'input':
					if self.readin.isdigit():
						value1 = int(self.readin)
					else:
						isError = True
						print('[WARN]请输入数字！')
				elif self.saveLoader.getValueByEntry(value1, 'value').isdigit():
					value1 = int(self.saveLoader.getValueByEntry(value1, 'value'))
				else:
					isError = True
					print('[WARN]用户变量' + value1 + '不是数字！')
				if value2.isdigit():
					value2 = int(value2)
				elif self.saveLoader.getValueByEntry(value2, 'value').isdigit():
					value2 = int(self.saveLoader.getValueByEntry(value2, 'value'))
				else:
					isError = True
					print('[WARN]用户变量' + value2 + '不是数字！')
				if value1 > value2 and isError == False:
					self.handleCMD(newCMD)
			elif value.find('<') != -1:
				isError = False
				value1, value2 = value.split('<')
				if value1 == 'input':
					if self.readin.isdigit():
						value1 = int(self.readin)
					else:
						isError = True
						print('[WARN]请输入数字！')
				elif self.saveLoader.getValueByEntry(value1, 'value').isdigit():
					value1 = int(self.saveLoader.getValueByEntry(value1, 'value'))
				else:
					isError = True
					print('[WARN]用户变量' + value1 + '不是数字！')
				if value2.isdigit():
					value2 = int(value2)
				elif self.saveLoader.getValueByEntry(value2, 'value').isdigit():
					value2 = int(self.saveLoader.getValueByEntry(value2, 'value'))
				else:
					isError = True
					print('[WARN]用户变量' + value2 + '不是数字！')
				if value1 < value2 and isError == False:
					self.handleCMD(newCMD)
			elif value.find('!') != -1:
				isError = False
				value1, value2 = value.split('!')
				if value1 == 'input':
					value1 = self.readin
				else:
					value1 = self.saveLoader.getValueByEntry(value1, 'value')
				if not value2.isdigit():
					value2 = self.saveLoader.getValueByEntry(value2, 'value')
				if value1 != value2:
					self.handleCMD(newCMD)
	def showValue(self, text):
		newPieces = []
		if text.find('${') != -1:
			pieces = text.split('${')
			for each in pieces:
				if each.find('}') != -1:
					lenth = 0
					for every in each:
						if every != '}':
							lenth = lenth + 1
						else:
							break
					trueValue = self.saveLoader.getValueByEntry(each[0:lenth], 'value')
					if trueValue != '!':
						each = trueValue + each[lenth + 1:]
						newPieces.append(each)
					else:
						print('[WARN]查无' + each[0:lenth] + '变量！')
				else:
					newPieces.append(each)
			text = "".join(newPieces)
			return text
		else:
			return text
	def delSpace(self, text):
		for each in text:
			if each != ' ':
				tmp.append(each)
		return tmp
if __name__ == '__main__':
	I = Game()
	I.run()
