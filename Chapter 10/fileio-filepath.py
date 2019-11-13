__author__ = 'andydelso'
import os
import glob

if __name__ == '__main__':
    """#use os and path to open a particular file and read it
    myPath = "/Users/andydelso/Documents/Course materials/Chapter 7/Practice files"

    inputFileName = os.path.join(myPath, "example.txt")

    with open(inputFileName, "r") as myInputFile:
        for line in myInputFile.readlines():
            print line,

    #use os and path to file particular files by type and rename
    myPath = "/Users/andydelso/Documents/Course materials/Chapter 7/Practice files/images"

    fileNamesList = os.listdir(myPath)

    for eachFile in fileNamesList:
        if eachFile.lower().endswith(".gif"):
            print 'Converting "{}" to JPG'.format(eachFile)

            fullFileName = os.path.join(myPath,eachFile)

            newFileName = fullFileName[0:len(fullFileName)-4] + ".jpg"

            os.rename(fullFileName, newFileName)"""

    #alternately, use glob
    myPath = "/Users/andydelso/Documents/Course materials/Chapter 7/Practice files/images"

    possibleFiles = os.path.join(myPath, "*/*.png")

    for fileName in glob.glob(possibleFiles):
        print fileName
