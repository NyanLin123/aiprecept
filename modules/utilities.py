import random
import math

def argmaxall(gen):
    maxv = -math.inf
    for (e,v) in gen:
        if v>maxv:
            maxvals, maxv = [e], v
        elif v==maxv:
            maxvals.append(e)
    return maxvals


def argmaxe(lst):
    return argmaxall(enumerate(lst))

def argmax(gen):
    return random.choice(argmaxall(gen))

def test():
    assert argmax(enumerate([9,83,2,1,43,98])) in [2,4]

test()