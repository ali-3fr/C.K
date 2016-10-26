# -*- coding: utf-8 -*-
from math import sqrt
def Leibniz(N):
    sum=0
    for k in  range(0,N+1):
        x=(8 / (float)((4 * k + 1) * (4 * k + 3)))
        sum+=x
    return sum
def Euler(N):
    sum=0
    for k in range(1,N+1):
        sum+=(6/float(k**2))
    return sqrt(sum)
N = input(u'Введите число N: ')
print 'pi by leibniz : ' +str(Leibniz(N))
print 'pi by euler : ' +str(Euler(N))