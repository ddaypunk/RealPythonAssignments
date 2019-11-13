__author__ = 'andydelso'

if __name__ == '__main__':
    with open("poem.txt", "r") as inputFile, open("output.txt", "w") as outputFile:

        for each in inputFile.readlines():
            outputFile.write(each)

    with open("output.txt", "a") as appendFile:
        appendFile.write("\nThis line was added later by append")
