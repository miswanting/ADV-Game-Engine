#coding=utf-8

import sys_bios

class TPOS:

	startCharacter = '|'
    breakCharacter = ':'
	endCharacter = '>'

	bios = sys_bios.BIOS()

    vFile = []
    TPFile = []

    def __init__(self, autoSave = True):
        self.autoSave = autoSave

	# Public function
    def setTarget(self, vFile):
        self.vFile = vFile

    def init(self, vFile = []):
        if vFile == []:
            if self.vFile == []:
                print('[WARN][TPOS-init]请先设置目标指针！')
            else:
                self.bios.new(self.vFile)
        else:
            self.bios.new(vFile)

    def new(self, TPFile):
        pass

    # Private function
    def load(self):
        # Step 1: ->vFile
        self.vFile = self.bios.getVFile(self.vFile)
        # Step 2: vFile->TPContainer
        # TPContainer[vDir, vFileName, TPFile[TPDir, TPFileName, TPData[]]]
        self.TPContainer = [self.vFile[0], self.vFile[1], []]

        mode = ''
        isFirst = True

		TPFile = []
		TPDir = ''
		TPFileName = ''
        for each in self.vFile[2]:
            if each[0] == self.startCharacter:
                TPDataUnit = ''
                for every in each:
                    if every == self.startCharacter:
						mode = 'TPDir'
                    elif every == self.breakCharacter:
                        mode = 'TPFileName'
					elif every == self.endCharacter:
						mode = 'TPData'
					elif mode == 'TPDir':
						TPDir += every
                    elif mode == 'TPFileName':
						TPFileName += every
					elif mode == 'TPData':
						TPDataUnit += every
                if TPFileName == '':
                    if TPDir == '':
                        TPFile[2].append(TPDataUnit)
                        TPDataUnit = ''
                    else:
                        print('[WARN][TPOS-load]TP文件名不能为空！')
                else:
                    if isFirst:
    					isFirst = False
					else:
						self.TPContainer[2].append(TPFile)
					newTPFile = [TPDir, TPFileName, [TPDataUnit]]
					TPDir, TPFileName, TPDataUnit = '', '', ''
			else:
				print('[INFO][TPOS-load]TP文件不能存在无效行！')
        if TPFile == []:
			pass
		else:
            self.TPContainer[2].append(TPFile)

    def save(self):
        # Step 1: TPFile->vFile
        self.vFile = [self.TPFile[0], self.TPFile[1], []]
		for TPFile in self.TPContainer[2]:
			FILE_HEAD = True
			for TPData in TPFile[2]:
				line = ''
				if FILE_HEAD:
					line = self.startCharacter + TPFile[0] + self.breakCharacter + TPFile[1] + self.endCharacter + TPData
				else:
					line = self.startCharacter + self.breakCharacter + self.endCharacter + TPData
				self.vFile[2].append(line)
        # Step 2: vFile->
		self.bios.setVFile(self.vFile)
if __name__ == '__main__':
	I = TPOS(True)
# TEST function-setTarget([Path, FileName]):void
    # Test 1:
    I.setTarget(['test', 'test.tp'])
# TEST function-init():void
    # Test 2:
    I.init()
# TEST function-new([Path, FileName, [Content..]]):void
    # Test 3:
    I.new(['test', '1.txt'])
# TEST function-setTPFile([Path, FileName, [Content..]):void
    I.setTPFile(['test', '2.txt', ['Line 1', 'Line 2']])
# TEST function-getTPFile([Path, FileName]):[Path, FileName, [Content..]]
    I.getTPFile(['test', '2.txt'])
# TEST function-getTPFolder([Path, FolderName]):[Path, FolderName ,[TPFolder..] , [TPFile..]]
    I.getTPFolder(['test', '2.txt'])

# TEST function-delete([Path, FileName]):void
    # Test 5
# TEST function-destroy([Path, FileName]):void
    I.destroy(['test', 'test.tp'])
