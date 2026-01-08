print("This is my calculator")
import math
import operator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        print("denominator can't be zero")
    else:
        return x/y
