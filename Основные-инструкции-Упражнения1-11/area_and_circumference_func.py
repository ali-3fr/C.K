# -*- coding: utf-8 -*-
from math import pi
def area (r):
    return pi*r**2
def circumference(r):
    return 2*pi*r
r = input(u'Введите радиус окружности : ')
print 'площади круга  : ' + str(area(r))
print 'длины окружности : ' + str(circumference(r))

