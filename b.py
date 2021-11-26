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


def zFuncAx1(a, b, c='r', axNum=1):
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


def sFuncAx1(a, b, c='b', axNum=1):
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


zFuncAx1(1, 35, 'r')
sFuncAx1(25-5, 55-5, 'y')
zFuncAx1(25 + 30 - 5, 65 + 30 - 5, 'y')
sFuncAx1(75, 100, 'b')

plt.show()
