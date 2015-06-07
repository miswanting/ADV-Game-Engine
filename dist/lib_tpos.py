#coding=utf-8
'''
Write your description here.
'''
import sys_bio
class TPManager(object):
    """
    init(path):Set up a new TP file, and make it empty.
    destroy:Delete a TP file.
    new(path):New a new folder or file in a TP file.
    delete:Delete a folder or a file in a TP file.
    pushContent(path, data):To bring a text file into a TP file.
    pullContent(path):To take a text file from a TP file.
    exist(path):To find if there is a same file.
    setPath(path):To set current path.

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
            self.data.append([path, ['']])
        self.save()
    def delete(self, virtualFileName):
        self.load()
        # TODO del file in data.
        self.save()
    def setPath(self, path):
        self.path.setPath(path)
    def pushContent(self, path, data):
        self.load()
        if self.exist(path):
            newData = []
            for file in self.data:
                if path == file[0]:
                    newData.append([path, data])
                else:
                    newData.append(file)
            self.data = newData
        else:
            self.data.append([path, data])
        self.save()
    def pullContent(self, path):
        self.load()
        if self.exist(path):
            for file in self.data:
                if path == file[0]:
                    return file[1]
        else:
            return False
    def exist(self, path):
        self.load()
        isExist = False
        if self.data == []:
            print('Empty TP file!')
        else:
            for file in self.data:
                if (path == file[0]):
                    isExist = True
        return isExist

    # Private function
    def load(self):
        self.file.load(self.path.path)
        self.TPFileAnalyze()
        return self.data
    def save(self):
        newData, newContent = [], []
        def isExist(file):
            isExist = False
            for each in newData:
                if file[0] == each[0]:
                    isExist = True
            return isExist
        for file in self.data:
            if isExist(file):
                print('Find  a same file in TP file.')
            else:
                newData.append(file)
        for file in newData:
            fileHead = True
            for line in file[1]:
                if fileHead:
                    newContent.append(self.startCharacter + file[0] + self.endCharacter + line)
                    fileHead = False
                else:
                    newContent.append(self.startCharacter + self.endCharacter + line)
        self.file.content = newContent
        self.file.save()
    def refresh(self):
        pass
    def TPFileAnalyze(self):
        '''
        data{virtualFile{path, content{}}}
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
                    elif mode == 'path':
                        path += every
                    elif mode == 'content':
                        contentUnit += every
                if path == '':
                    virtualFile[1].append(contentUnit)
                    contentUnit = ''
                else:
                    content = []
                    if isFirst:
                        isFirst = False
                    else:
                        self.data.append(virtualFile)
                    content.append(contentUnit)
                    contentUnit = ''
                    virtualFile = [path, content]
        if virtualFile == []:
            pass
        else:
            self.data.append(virtualFile)
if __name__ == '__main__':
    I = TPManager()
    I.init('story\\test.tp')# New a new TP file.
    print('This should be a empty list:', I.data)
    I.setPath('story\\test.tp')
    I.new('folder\\number.txt')# New a new text file in the TP file.
    data = ['111', '222', '333']
    I.pushContent('folder\\number.txt', data)
    data = I.pullContent('folder\\number.txt')# Get text.
    print('This should be 3 number list:', data)
    I.data.append(['a.txt', ['aaa', 'bbb', 'ccc']])
    I.save()# Save changes.
    data = I.pullContent('a.txt')# Get text.
    print('This should be 3 abc list:', data)
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
