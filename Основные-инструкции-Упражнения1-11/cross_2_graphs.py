# -*- coding: utf-8 -*-
from math import fabs
def f(x):
    return x
def g(x):
    return x**2
def cross(varepsilon , N):
    scale = float(8 / N)
    for i in range(0, N + 1):
        if fabs(f(-4+i*scale)-g(-4+i*scale))<varepsilon:
            return -4+i*scale
    return None

varepsilon = input(u'Введите число ε')
N = input(u'Введите число N')
print 'approximate cross point is :'+ str(cross(varepsilon , N))

