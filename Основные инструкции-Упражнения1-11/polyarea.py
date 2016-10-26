# -*- coding: utf-8 -*-
from math import fabs
def polyarea (x, y):
    sum1 = 0
    sum2 = 0
    for i  in range(0,len(x)-1):
        sum1 += x[i]*y[i+1]
    for i in range(0,len(x)-1):
        sum2 +=y[i]*x[i+1]
    return fabs(sum2-sum1)/2
# треугольник
x_3 = [1,2,0]
y_3 = [2,0,0]
print 'ожидаемый результат :2.0'
print  str(polyarea(x_3,y_3))

x_4 = [-1,4,4,-1]
y_4 = [2,2,0,0]
print 'ожидаемый результат : 9.0'
print str(polyarea(x_4, y_4))

y = []
x = []
x = input(u'input  x of coordinatse  <use "," as seperater>: ')
y = input(u'use y of coordinats  <use "," as seperater>: ')
print polyarea(x,y)
