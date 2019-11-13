__author__ = 'andydelso'
from random import randint


def flipCoin():
    return randint(0,1)

if __name__ == '__main__':

    trials = 10000
    flips = 0

    for each in range(0,trials):
        flips += 1

        if flipCoin() == 0:
            while flipCoin() == 0:
                flips += 1
            flips += 1
        else:
            while flipCoin() == 1:
                flips += 1
            flips += 1


    print str(flips/float(trials)*100) + "%"