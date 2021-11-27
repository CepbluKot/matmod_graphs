import numpy as np
import matplotlib.pyplot as plt

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)


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


def zFunc(a, b, c='r', axNum=1):
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
    if axNum == 1:
        ax1.plot(funcX, funcY, c)
    if axNum == 2:
        ax2.plot(funcX, funcY, c)
    if axNum == 3:
        ax3.plot(funcX, funcY, c)
    if axNum == 4:
        ax4.plot(funcX, funcY, c)


def sFunc(a, b, c='b', axNum=1):
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

    if axNum == 1:
        ax1.plot(funcX, funcY, c)
    if axNum == 2:
        ax2.plot(funcX, funcY, c)
    if axNum == 3:
        ax3.plot(funcX, funcY, c)
    if axNum == 4:
        ax4.plot(funcX, funcY, c)


def lineFunc(a, b, c='g', axNum=1):
    funcX = []
    funcY = []
    x = a
    while x < b:
        funcX.append(x)
        funcY.append(1)
        x += 0.01
    if axNum == 1:
        ax1.plot(funcX, funcY, c)
    if axNum == 2:
        ax2.plot(funcX, funcY, c)
    if axNum == 3:
        ax3.plot(funcX, funcY, c)
    if axNum == 4:
        ax4.plot(funcX, funcY, c)


zFunc(1, 50, 'r')
sFunc(15, 55, 'y')
zFunc(25 + 30, 95, 'y')
sFunc(50, 100, 'b')

zFunc(100, 700, 'r', 2)
sFunc(700 - ((850 + 701)/2 - 700), 700, 'y', 2)
lineFunc(700, 850, 'y', 2)
zFunc(850, 950, 'y', 2)
sFunc(851, 950, 'b', 2)

zFunc(0, 1.001, 'b', 3)
sFunc(0, 1.001, 'r', 3)


#  1 2 3

zFunc(0, 1.5, 'r', 4)
sFunc(0, 1.5, 'y', 4)
zFunc(1.5, 3, 'y', 4)
sFunc(1.5, 3, 'b', 4)


plt.show()
