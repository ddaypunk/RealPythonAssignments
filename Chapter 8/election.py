__author__ = 'andydelso'

import random

def simulateVote():
    #just send back a random number for each region
    return random.random(), random.random(), random.random()

def checkRegions(a,b,c):

    if a > 0.13 and b > 0.35:
        return 'A'
    elif a > 0.13 and c > 0.83:
        return 'A'
    elif b > 0.35 and c > 0.83:
        return 'A'
    else:
        return 'B'

if __name__ == '__main__':

    results = []
    count_a = 0
    count_b = 0
    average = 0
    runs = 100000

    for each in range (0,runs):
        #generate reqional results
        chance_A, chance_B, chance_C = simulateVote()

        #check the end result and store it
        electionResult = checkRegions(chance_A, chance_B, chance_C)
        results.append(electionResult)

        if electionResult == 'A':
            count_a = count_a +1
        else:
            count_b = count_b +1

    print "Probability of candidate A winning: " + str(count_a*100/runs) +"%"
    print "Probability of candidate B winning: " + str(count_b*100/runs) +"%"




