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
    endCharacter = '>'

    path = sys_bio.PathManager()

    folder = sys_bio.BIOFolderLoader()
    file = sys_bio.BIOFileLoader()

    data = []
    def __init__(self):
        #super(, self).__init__()
        #self.arg = arg
        pass

    # Public function
    def init(self, path):
        self.path.setPath(path)
        self.folder.load(self.path.dir)
        self.folder.new(self.path.fileName)
    def destroy(arg):
        self.path.fileName = 'test.tp'
        sys_bio.delete(self.path.fileName)
    def new(self, path):
        self.load()
        if self.exist(path):
            pass
        else:
            self.data.append([path, []])
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
        self.load()
        isExist = False
        for file in self.data:
            if (path == file[0]):
                isExist = True
        return isExist

    # Private function
    def load(self):
        self.file.load(self.path.path)
        self.TPFileAnalyze()
    def save(self):
        print(self.data)
        content = []
        for file in self.data:
            fileHead = True
            for line in file[3]:
                if fileHead:
                    # print(self.data,file[0],file[1],file[2])
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
        print(self.file.content)
        self.file.save()
    def refresh(self):
        pass
    def TPFileAnalyze(self):
        '''
        data{virtualFile{dir, fileName, extension, content{}}}
        '''
        isFirst, self.data, virtualFile, content = True, [], [], []
        for line in self.file.content:
            mode, path, contentUnit = '', '', ''
            if line[0] != self.startCharacter:
                pass
            else:
                for every in line:
                    if every == self.startCharacter:
                        mode = 'path'
                    elif every == self.endCharacter:
                        mode = 'content'
                        if path == '':
                            content.append(contentUnit)
                            contentUnit = ''
                        else:
                            # At the very begining of a virtual file.
                            if isFirst:
                                isFirst = False
                                virtualFile = [path]
                                path = ''
                            else:
                                virtualFile.append(content)
                                content = []
                                self.data.append(virtualFile)
                                virtualFile = []
                    elif mode == 'path':
                        path += every
                    elif mode == 'content':
                        contentUnit += every
        virtualFile.append(content)
        self.data.append(virtualFile)
'''
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
'''
if __name__ == '__main__':
    I = TPManager()
    I.init('story\\test.tp')# New a new TP file.
    I.new('folder\\test.txt')# New a new text file in the TP file.
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
