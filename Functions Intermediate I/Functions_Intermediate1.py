from random import random


def randInt(min=0,max=100):
    rand_num=round((random()*(max-min))+min)
    return rand_num

for i in range(100):
    print(randInt(min=2,max=50))