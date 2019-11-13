__author__ = 'andydelso'

"""
Investment calculator assignent
"""

def invest (amount, rate, time):
    total = amount

    print 'principal amount: ' + str(amount)
    print 'annual rate of return: ' + str(rate)

    for i in range (1,time+1):
        total = total + (total * rate)
        print 'year ' + str(i) + ': $' + str(total)



if __name__ == '__main__':
    invest(2000, .025, 5)