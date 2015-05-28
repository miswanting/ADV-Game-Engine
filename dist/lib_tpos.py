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

    path = sys_bio.PathManager()
    vPath = sys_bio.PathManager()

    path.setDir('story\\')
    path.setFileName('test.tp')
    vPath.setDir('\\')

    file = sys_bio.BIOFolderLoader()
    data = []
    def __init__(self):
        #super(, self).__init__()
        #self.arg = arg
        pass

    # Public function
    def init(self, fileName = 'test.tp'):
        self.path.fileName = fileName
        self.file.new(self.path.fileName)
    def destroy(arg):
        self.path.fileName = 'test.tp'
        sys_bio.delete(self.path.fileName)
    def new(self, virtualFileName):
        self.vPath.setFileName(virtualFileName)
        self.load()
        print(self.vPath.fileName)
        self.data.append(
        self.startCharacter + self.vPath.dir +
        self.splitCharacter + self.vPath.fileName.split('.')[0] +
        self.splitCharacter + self.vPath.fileName.split('.')[1] +
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
    def exist(self, fileName, dir = '\\'):
        self.load()
        isExist = False
        for file in self.data:
            if (dir == file[0] and fileName.split('.')[0] == file[1] and fileName.split('.')[1] == file[2]):
                isExist = True
        return isExist

    # Private function
    def load(self):
        self.file.load(self.path.dir)
        self.TPFileAnalyze()
    def save(self):
        content = []
        for file in self.data:
            fileHead = True
            for line in file[3]:
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
        self.data = []
        dir, fileName, extension, unitContent, content, virtualFile = '', '', '', '', [], []
        for line in self.file.content:
            isBroken = False
            isContent = False
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
                        isContent = True
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
                        elif isContent:
                            unitContent += every
                content.append(unitContent)
        virtualFile.append(content)
        self.data.append(virtualFile)
if __name__ == '__main__':
    I = TPManager()
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
