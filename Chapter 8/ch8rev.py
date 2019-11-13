__author__ = 'andydelso'

def ch8revcheck(inString):
    if len(inString) < 5:
        print "The length is less than 5 characters"
    elif len(inString) > 5:
        print "The length is greater than 5 characters"
    else:
        print "The length is 5 characters"

if __name__ == '__main__':

    entry = raw_input("Enter a word: ")

    ch8revcheck(entry)
