__author__ = 'andydelso'

def factors(num):
    for each in range (1,num+1):
        if not (num%each):
            print str(each) + ' is a divisor of ' + str(num)
        #else:
           # print str(each) + ' is NOT a divisor of ' + str(num)

if __name__ == '__main__':

    factors(int(raw_input("Enter a positive integer: ")))