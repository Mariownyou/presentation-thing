import sys
import os

folder = 'C:\\Users\\smj51\\OneDrive\\Рабочий стол\\presentations\\'

def pptx():
    print(sys.argv)
    fileName = str(sys.argv[1]) + str('.pptx')
    open(folder + fileName, 'a').close()
    print(fileName)

if __name__ == '__main__':
    pptx()
