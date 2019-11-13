__author__ = 'andydelso'

if __name__ == '__main__':

    desserts = ["ice cream", "cookies"] #1

    desserts.sort() #2
    print desserts

    print desserts.index('ice cream')#3

    food = desserts[:]#4

    food.append("broccoli")#5
    food.append("turnips")

    print desserts #6
    print food

    food.remove("cookies") #7

    print food[:2] #8

    breakfast = "cookies,cookies,cookies".split(",") #9
    print breakfast
