# -*- coding: utf-8 -*-
import rectangular
import trapezoidal
import math
def f(x):
    return math.sin(x)

print "for 0 to pi"
print trapezoidal.trapezoidal(f,0,math.pi,2)

print trapezoidal.trapezoidal(f,0,math.pi,100)
print rectangular.rectangular(f,0,math.pi,2)
print rectangular.rectangular(f,0,math.pi,100)

print "for 0 to 2pi"

print trapezoidal.trapezoidal(f,0,2*math.pi,2)
print trapezoidal.trapezoidal(f,0,2*math.pi,100)
print rectangular.rectangular(f,0,2*math.pi,2)
print rectangular.rectangular(f,0,2*math.pi,100)


print "по методу трапеции приближаемся сверху к точному решению а по методу прямоугольника снизу"