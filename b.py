import numpy as np
import matplotlib.pyplot as plt
import math


def nu1(x, a, b):

    res = 1 - 2 * ((x - a) / (b - a))**2
    return res


def nu2(x, a, b):

    res = 2 * ((b - x) / (b - a))**2
    return res


def nu3(x, a, b):

    res = 2 * ((x-a)/(b-a))**2
    return res


def nu4(x, a, b):

    res = 1 - 2 * ((x - b) / (b-a))**2
    return res


def zFunc(a, b, c = 'r'):
    funcX = []
    funcY = []
    x = a

    while x < b:

        funcX.append(x)

        if a < x and x <= (a+b)/2:

            funcY.append(nu1(x, a, b))

        elif (a+b)/2 < x and x < b:
            funcY.append(nu2(x, a, b))

        else:
            funcY.append(1)

        x += 0.01
    plt.plot(funcX, funcY, c)


def sFunc(a, b, c = 'b'):
    funcX = []
    funcY = []
    x = a

    while x < b:
        y = (a + b) / 2
        funcX.append(x)

        if x <= a:
            funcY.append(0)

        elif a < x and x <= y:

            funcY.append(nu3(x, a, b))

        elif y < x and x < b:
            funcY.append(nu4(x, a, b))

        x += 0.01

    plt.plot(funcX, funcY, c)



zFunc(1, 35)
sFunc(25-5, 55-5, 'y')
zFunc(25 + 30 - 5 , 65 + 30 - 5, 'y')
sFunc(75, 100)

plt.show()
