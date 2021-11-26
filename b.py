import numpy as np
import matplotlib.pyplot as plt
import math


def nu1(x, a, b):

    res = 1 - 2 * ((x - a) / (b - a))**2
    return res


def nu2(x, a, b):

    res = 2 * ((b - x) / (b - a))**2
    return res


def fx(t):

    res = 1000 * math.sqrt(2) / 2 * t
    return res


funcX = []
funcY = []


h = 5

x = 0
a = 0
b = 20
while x < b:

    funcX.append(x)

    if a < x and x <= (a+b)/2:
        
        funcY.append(nu1(x, a, b))

    elif (a+b)/2 < x and x < b:
        funcY.append(nu2(x, a, b))

    else:
        funcY.append(1)
    
    x += 0.5

print('x:', funcX)
print('y:', funcY)

fig = plt.figure()

plt.plot(funcX, funcY)


plt.show()
