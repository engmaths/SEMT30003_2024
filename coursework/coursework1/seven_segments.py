from math import *
import numpy as np

fancy=False

def seven_segment(pattern):
    global fancy
    left,lower,right = \
        ('▕','__','▏') if fancy else \
        ('|','__','|')
    def vert(d1,d2,d3):
        print(
        (left  if d1 else " ")+
        (lower if d3 else "  ")+
        (right if d2 else " "))
    bits = [(ai==1) for ai in pattern]
    print(" "+lower+" " if bits[0] else "   ")
    vert(*bits[1:4])
    vert(*bits[4:7])
    number=0
    for i in range(0,4):
        if bits[7+i]:
            number+=pow(2,i)
    print('%X'%int(number))

hexdigits = np.int8([\
    [1,1,1,0,1,1,1, 0,0,0,0],
    [0,0,1,0,0,1,0, 1,0,0,0],
    [1,0,1,1,1,0,1, 0,1,0,0],
    [1,0,1,1,0,1,1, 1,1,0,0],
    [0,1,1,1,0,1,0, 0,0,1,0],
    [1,1,0,1,0,1,1, 1,0,1,0],
    [1,1,0,1,1,1,1, 0,1,1,0],
    [1,0,1,0,0,1,0, 1,1,1,0],
    [1,1,1,1,1,1,1, 0,0,0,1],
    [1,1,1,1,0,1,1, 1,0,0,1],
    [1,1,1,1,1,1,0, 0,1,0,1],
    [0,1,0,1,1,1,1, 1,1,0,1],
    [1,1,0,0,1,0,1, 0,0,1,1],
    [0,0,1,1,1,1,1, 1,0,1,1],
    [1,1,0,1,1,0,1, 0,1,1,1],
    [1,1,0,1,1,0,0, 1,1,1,1]])*2-1

zero, one, two, three, four, five, six, seven, eight, nine, hexA, hexB, hexC, hexD, hexE, hexF = hexdigits

test1 = np.int8([1,-1,1,1,-1,1,1,-1,-1,-1,-1])
test2 = np.int8([1,1,1,1,1,1,1,-1,-1,-1,-1])

if __name__=="__main__":
    for d in hexdigits: seven_segment(d)
    seven_segment(three)
    seven_segment(six)
    seven_segment(one)
    print("test1")
    seven_segment(test1)
    print("test2")
    seven_segment(test2)




