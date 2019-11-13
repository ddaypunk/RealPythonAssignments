__author__ = 'andydelso'

if __name__ == '__main__':

    while True:

        try:
            entry = int(raw_input("Enter an integer: "))

        except ValueError:
            print "Number Entered was not an integer, please try again."
            continue

        print "The number was: ", entry