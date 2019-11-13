__author__ = 'andydelso'
import os
import glob

if __name__ == '__main__':
    myRootPath = "/Users/andydelso/Documents/Course materials/Chapter 7/Practice files"
    myPath = os.path.join(myRootPath, "images")

    for eachPath in os.listdir(myPath):
        print os.path.join(myPath, eachPath)

    print "\n END OF #1 \n"

    listOfPics1 = os.path.join(myPath, "*/*.png")

    for each1 in glob.glob(listOfPics1):
        print each1,

    listOfPics2 = os.path.join(myPath, "*.PNG")

    for each2 in glob.glob(listOfPics2):
        print each2,