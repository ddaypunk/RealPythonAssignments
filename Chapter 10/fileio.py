__author__ = 'andydelso'

if __name__ == '__main__':
    #part one
    myOutputFile = open("hello.txt", "w")
    myOutputFile.writelines("This is my first file.")
    myOutputFile.close()

    #part two
    myOutputFile = open("hello.txt", "w")
    linesToWrite = ["This is my file.", "\nThere are many like it", "\nbut this one is mine."]

    myOutputFile.writelines(linesToWrite)
    myOutputFile.close()

    #part three
    myOutputFile = open("hello.txt", "a")
    nextLine = ["\nNON SEQUITUR"]
    myOutputFile.writelines(nextLine)
    myOutputFile.close()

    #part four
    myInputFile = open("hello.txt", "r")

    #updated to loop through instead of
    #just printing the list returned
    for each in myInputFile.readlines():
        print each,

    myInputFile.close()

    #part five
    myInputFile = open("hello.txt", "r")

    line = myInputFile.readline()

    while line != "":
        print line,

        line = myInputFile.readline()

    myInputFile.close()

    #part six
    #use with keyword because it will cleanup itself
    with open("hello.txt", "r") as myInputFile:
        for line in myInputFile.readlines():
            print line,

    #alternately
    with open("hello.txt", "r") as myInputFile, open("hi.txt", "w") as myOutputFile:
        for line in myInputFile.readlines():
            myOutputFile.write(line)

