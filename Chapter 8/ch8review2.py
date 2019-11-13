#__author__ = 'andydelso'

def checkForQuit(char):
    if entry == 'q' or entry == 'Q':
        print "Quit condition reached"
        return True

if __name__ == '__main__':
    while True:
        entry = raw_input("Enter character: ")
        assert isinstance(entry, str)
        if checkForQuit(entry):
            break
