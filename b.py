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


def zFunc(a, b, c='r', axNum=1, temp=False, t=0, label='', intP = 0):
    funcX = []
    funcY = []
    x = a

    i = intP
    j = 0
    fx = 0
    fy = 0
    while x < b:

        funcX.append(x)

        if a < x and x <= (a+b)/2:
            
            j = nu1(x, a, b)
            if x >  i - 0.1 and x < i + 0.1 and intP != 0:
                fx = x
                fy = j
            funcY.append(j)

        elif (a+b)/2 < x and x < b:

            j = nu2(x, a, b)
            
            if x >  i - 0.1 and x < i + 0.1 and intP != 0:
                fx = x
                fy = j
                
                
            funcY.append(j)

        else:
            funcY.append(1)
        
        x += 0.01
    print(label,fx, fy)

        
    if axNum == 1:
        ax1.plot(funcX, funcY, c)
        if temp == True:
            ax1.axvline(x = t, color = 'g', label = 'temp')
        if label != '':
            ax1.set_xlabel(label)
            ax1.set_ylabel('nu')
    if axNum == 2:
        ax2.plot(funcX, funcY, c)
        if temp == True:
            ax2.axvline(x = t, color = 'g', label = 'temp')
        if label != '':
            ax2.set_xlabel(label)
            ax2.set_ylabel('nu')
    if axNum == 3:
        ax3.plot(funcX, funcY, c)
        if temp == True:
            ax3.axvline(x = t, color = 'g', label = 'temp')
        if label != '':
            ax3.set_xlabel(label)
            ax3.set_ylabel('nu')
    if axNum == 4:
        ax4.plot(funcX, funcY, c)
        if temp == True:
            ax4.axvline(x = t, color = 'g', label = 'temp')
        if label != '':
            ax4.set_xlabel(label)
            ax4.set_ylabel('nu')
    


def sFunc(a, b, c='b', axNum=1, temp=False, t=0, label='', intP=0):
    funcX = []
    funcY = []
    x = a
    i = intP
    fx= 0
    fy=0
    j = 0
    while x < b:
        y = (a + b) / 2
        funcX.append(x)

        if x <= a:
            funcY.append(0)

        elif a < x and x <= y:
            j = nu3(x, a, b)

            if x >  i - 0.1 and x < i + 0.1 and intP != 0:
                fx = x
                fy = j
            funcY.append(j)

        elif y < x and x < b:
            j = nu4(x, a, b)
            if x >  i - 0.1 and x < i + 0.1 and intP != 0:
                fx = x
                fy = j
            funcY.append(j)

        x += 0.01
    print(label,fx, fy)

    if axNum == 1:
        ax1.plot(funcX, funcY, c)
        if temp == True:
            ax1.axvline(x = t, color = 'g', label = 'temp')
        if label != '':
            ax1.set_xlabel(label)
            ax1.set_ylabel('nu')
    if axNum == 2:
        ax2.plot(funcX, funcY, c)
        if temp == True:
            ax2.axvline(x = t, color = 'g', label = 'temp')
        if label != '':
            ax2.set_xlabel(label)
            ax2.set_ylabel('nu')
    if axNum == 3:
        ax3.plot(funcX, funcY, c)
        if temp == True:
            ax3.axvline(x = t, color = 'g', label = 'temp')
        if label != '':
            ax3.set_xlabel(label)
            ax3.set_ylabel('nu')
    if axNum == 4:
        ax4.plot(funcX, funcY, c)
        if temp == True:
            ax4.axvline(x = t, color = 'g', label = 'temp')
        if label != '':
            ax4.set_xlabel(label)
            ax4.set_ylabel('nu')


def lineFunc(a, b, c='g', axNum=1, temp = False,t=0):
    funcX = []
    funcY = []
    x = a
    sec_cord = 0
    while x < b:
        funcX.append(x)
        funcY.append(1)
        x += 0.01
    if axNum == 1:
        ax1.plot(funcX, funcY, c)
        if temp == True:
            ax1.axvline(x = t, color = 'g', label = 'temp')
    if axNum == 2:
        ax2.plot(funcX, funcY, c)
        if temp == True:
            ax2.axvline(x = t, color = 'g', label = 'temp')
    if axNum == 3:
        ax3.plot(funcX, funcY, c)
        if temp == True:
            ax3.axvline(x = t, color = 'g', label = 'temp')
    if axNum == 4:
        ax4.plot(funcX, funcY, c)
        if temp == True:
            ax4.axvline(x = t, color = 'g', label = 'temp')
    


# config ########

temp = 35
pechT = 700
speed = 1

# ###############


zFunc(1, 50, 'r', 1, True, temp, 'temp', 35)
sFunc(15, 55, 'y', 1, True, temp, '', 35)
zFunc(25 + 30, 95, 'y', 1, False, 0)
sFunc(50, 100, 'b', 1, False, 0)

zFunc(100, 700, 'r', 2, True, pechT, 'Tpech', pechT)
sFunc(700 - ((850 + 701)/2 - 700), 700, 'y', 2, True, pechT)
lineFunc(700, 850, 'y', 2, True, pechT)
zFunc(850, 950, 'y', 2, True, pechT)
sFunc(851, 950, 'b', 2, True, pechT)

zFunc(0, 1.001, 'b', 3, True, speed,'speed', speed)
sFunc(0, 1.001, 'r', 3, False, 0)


#  1 2 3

zFunc(0, 1.01, 'r', 4, False, 0, 'Mode')
sFunc(0, 1.01, 'y', 4)
zFunc(1.01, 2, 'y', 4, True,1)
sFunc(1.01, 2, 'b', 4)


plt.show()
