import sys
import os


class pptxAutomator:
    mainFolder = 'C:\\Users\\smj51\\OneDrive\\Рабочий стол\\presentations\\'
    default = 'C:\\Users\\smj51\\OneDrive\\Рабочий стол\\presentations\\all\\'
    name = sys.argv[1]
    folder = sys.argv[2] + '\\'

    def createFilePath(self):
        fileName = str(self.name) + str('.pptx')
        return self.mainFolder + self.folder + self.name + '\\' +  fileName

    def createFolderPath(self):
        return self.mainFolder + self.folder + self.name

    def createFolder(self):
        os.mkdir(self.createFolderPath())
        os.mkdir(self.createFolderPath()+'\\img')

    def createPptx(self):
        self.createFolder()
        open(self.createFilePath(), 'a').close()
        print('Ur folder is succesfuly created ;)')

if __name__ == '__main__':
    pptx = pptxAutomator()
    command = str(sys.argv[0])

    if command == 'pptx.py':
        pptx.createPptx()
