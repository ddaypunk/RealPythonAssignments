__author__ = 'andydelso'
import random

def isVowel(char):

    if char.lower() in "aeiou":
        return True
    else:
        return False

if __name__ == '__main__':

    #initialize string source lists
    nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",\
             "extrovert", "gorilla"]
    verbs = ["kicks", "jingles", "bounces", "slurps", "meows", \
             "explodes", "curdles"]
    adjectives = ["furry", "balding", "incredulous", "fragrant", \
                  "exuberant", "glistening"]
    prepositions = ["against", "after", "into", "beneath", "upon", \
                    "for", "in", "like", "over", "within"]
    adverbs = ["curiously", "extravagantly", "tantalizingly", \
               "furiously", "sensuously"]

    poem = """{} {} {} \n\n{} {} {} {} {} the {} {}\n{}, the {} {}\nthe {} {} {} a {} {}"""

    #select 3 unique nouns
    noun1 = random.choice(nouns)

    noun2 = random.choice(nouns)
    while noun1 == noun2:
        noun2 = random.choice(nouns)

    noun3 = random.choice(nouns)

    while noun1 == noun3 or noun2 == noun3:
        noun3 = random.choice(nouns)

    #select the verbs
    verb1 = random.choice(verbs)

    verb2 = random.choice(verbs)
    while verb1 == verb2:
        verb2 = random.choice(verbs)

    verb3 = random.choice(verbs)

    while verb1 == verb3 or verb2 == verb3:
        verb3 = random.choice(verbs)

    #select the adjectives
    adj1 = random.choice(adjectives)

    adj2 = random.choice(adjectives)
    while adj1 == adj2:
        adj2 = random.choice(adjectives)

    adj3 = random.choice(adjectives)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = random.choice(adjectives)

    #select prepositions
    prep1 = random.choice(prepositions)

    prep2 = random.choice(prepositions)
    while prep1 == prep2:
        prep2 = random.choice(prepositions)

    #select the adverb
    adverb1 = random.choice(adverbs)

    if isVowel(adj1[0]):
        first = 'An'
    else:
        first = 'A'

    print poem.format(first, adj1, noun1,\
                      first, adj1, noun1, verb1, prep1, adj2, noun2,\
                      adverb1, noun1, verb2,\
                      noun2, verb3, prep2, adj3, noun3)