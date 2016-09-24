#coding=utf-8

'''
vFile = [directory:str, fileName:str, [Content..:str]]
vFolder = [directory:str, folderName:str, [vFolder..], [vFile..]]
'''

import sys_bios

class TPOS:

    startCharacter = '|'
    breakCharacter = ':'
	endCharacter = '>'

    bios = sys_bios.BIOS()

    vFile = []
    vFolder = []
    TPFile = []
    TPFolder = []

    def __init__(self, autoSave = True):
        self.autoSave = autoSave

    # Public function
    def openTPFile(self, TPFile):
        self.TPFile = bios.getVFile(TPFile)
        self.generateFile()
        return True

    def closeTPFile(self, TPFile):
        self.TPFile = []
        return True

    def getTPFolder(self, TPFolder):
        self.TPFolder = bios.getVFolder(TPFolder)
        return self.TPFolder

    def setTPFolder(self, TPFolder):
        # TODO
        return True

    def new(self, vFile):
        return True

    def delete(self, vFile):
        return True

    def read(self, vFile):
        return vFile

    def write(self, vFile):
        return True

    def isExist(self, vFile):
        pass

    def getFolder(self, vFolder):
        return vFolder

    def setFolder(self, vFolder):
        return True

    # Private function
    def generateFile(self):
        mode = ''
        isFirst = True

		vFolder = [self.TPFile[0], self.TPFile[1], []]
        vFile = []
        for each in self.TPFile[2]:
            if each[0] == self.startCharacter:
                for every in each:
                    if every == self.startCharacter:
						mode = 'Dir'
                    elif every == self.breakCharacter:
                        mode = 'FileName'
					elif every == self.endCharacter:
						mode = 'Data'
					elif mode == 'Dir':
						Dir += every
                    elif mode == 'FileName':
						FileName += every
					elif mode == 'Data':
						Data += every
                if FileName == '':
                    if Dir == '':
                        vFile[2].append(Data)
                        Data = ''
                    else:
                        print('[WARN][TPOS-generateFile]TP文件格式非法！')
                else:
                    if isFirst:
                        isFirst = False
                    else:
                        self.vFolder[2].append(vFile)
                    vFile = [Dir, FileName, [Data]]
                    Dir, FileName, Data = '', '', ''
