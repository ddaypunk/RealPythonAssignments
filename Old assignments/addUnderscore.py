__author__ = 'andydelso'

def addUnderscores(word):
    new_word ="_"
    for i in range(0, len(word)):
        new_word = new_word + word[i] +"_"
    return new_word
phrase = "hello "

if __name__ == '__main__':
    print addUnderscores("hello ")