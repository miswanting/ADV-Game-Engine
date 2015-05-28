#coding=utf-8
'''
Write your description here.
'''
import sys_bio
class TPManager(object):
    """
    init:Set up a new TP file, and make it empty.
    destroy:Delete a TP file.
    new:New a new folder or file in a TP file.
    delete:Delete a folder or a file in a TP file.
    push:To bring a text file into a TP file.
    pull:To take a text file from a TP file.
    exist:To find if there is a same file.

    load:To get the text in a text file from a TP file.
    save:To save the text in a text file to a TP file.

    # move
    # copy
    # rename
    """
    startCharacter = '|'
    splitCharacter = ':'
    endCharacter = '>'
    currentDir = '\\story'
    currentTPFileName = 'test.tp'
    currentVirtualDir = '\\'
    currentVirtualFileName = ''

    file = sys_bio.BIOFileLoader()
    data = []
    def __init__(self, ang):
        super(, self).__init__()
        self.arg = arg

    # Public function
    def init(self, fileName = 'test.tp'):
        self.currentTPFileName = fileName
        sys_bio.new(self.currentTPFileName)
    def destroy(arg):
        self.currentTPFileName = 'test.tp'
        sys_bio.delete(self.currentTPFileName)
    def new(self, virtualFileName):
        self.virtualFileName = virtualFileName
        self.load()
        data.append(
        self.startCharacter + self.currentVirtualDir +
        self.splitCharacter + self.currentVirtualFileName.split('.')[0] +
        self.splitCharacter + self.currentVirtualFileName.split('.')[1] +
        self.endCharacter
        )
        self.save()
    def delete(self, virtualFileName):
        self.load()
        # TODO del file in data.
        self.save()
    def push(arg):
        pass
    def pull(arg):
        pass
    def exist(self, path):
        return False

    # Private function
    def load(self):
        self.file.load(self.currentDir + self.currentTPFileName)
        self.TPFileAnalyze()
    def save(self):
        content = []
        for file in self.data:
            fileHead = True
            for line in file.content:
                if fileHead:
                    content.append(
                    self.startCharacter + file[0] +
                    self.splitCharacter + file[1] +
                    self.splitCharacter + file[2] +
                    self.endCharacter + line
                    )
                    fileHead = False
                else:
                    content.append(
                    self.startCharacter + self.endCharacter + line
                    )
        self.file.content = content
        self.file.save()
    def refresh(self):
        pass
    def TPFileAnalyze(self):
        '''
        data{virtualFile{dir, fileName, extension, content{}}}
        '''
        isFirstRun = True
        dir, fileName, extension, unitContent, content, virtualFile = '', '', '', '', [], []
        for line in self.file.content:
            isBroken = False
            mode = 0
            if line[0] != self.startCharacter:
                pass
            else:
                for every in line:
                    if every == self.startCharacter:
                        mode = 0
                    elif every == self.splitCharacter:
                        mode += 1
                    elif every == self.endCharacter:
                        if dir == '':
                            pass
                        else:# At the very begining of a virtual file.
                            if isFirstRun:
                                isFirstRun = False
                            else:
                                virtualFile.append(content)
                                self.data.append(virtualFile)
                            virtualFile = [dir, fileName, extension]
                            dir, fileName, extension = '', '', ''
                        mode = -1
                    else:
                        if mode == 0:
                            dir += every
                        elif mode == 1:
                            fileName += every
                        elif mode == 2:
                            extension += every
                        elif mode == -1:
                            unitContent += every
                content.append(unitContent)
        virtualFile.append(content)
        self.data.append(virtualFile)
if __name__ == '__main__':
    I = TPManager()
    I.setCurrentDir()# Set path.
    print('[TEST]Now I`m in dir: ' + I.getCurrentDir())
    I.setCurrentTPFileName()# Set TP file name.
    print('[TEST]Now I`m in dir: ' + I.getCurrentTPFileName())
    I.init()# New a new TP file.
    I.new('test.txt')# New a new text file in the TP file.
    # data = I.load('test.txt')# Get text.
    # Do something.
    # I.save(data)# Save changes.
    # I.pull('test.txt', '\')# Bring out the file in TP file.
    # I.push('test.txt', '\')# Take file into TP file.
    # I.delete('test.txt')# Delete the file in TP file.
    # # Test folder function in TP file.
    # I.new('\test\test.txt')# New a new text file in the TP file.
    # data = I.load('\test\test.txt')# Get text.
    # Do something.
    # I.save(data)# Save changes.
    # I.pull('\test\test.txt', '\')# Bring out the file in TP file.
    # I.push('\test\test.txt', '\')# Take file into TP file.
    # I.delete('\test\test.txt')# Delete the file in TP file.
    # I.destroy()# Delete the TP file.
