__author__ = 'andydelso'

import random

if __name__ == '__main__':

    rolls = []

    for each in range (0,10000):
        dieRoll = random.randint(1,6)
        rolls.append(dieRoll)

    total = 0

    for each in rolls:
        total = total + each

    print "Average roll is: ", (total / 10000)