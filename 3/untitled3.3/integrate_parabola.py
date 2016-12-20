# -*- coding: utf-8 -*-
import rectangular
import trapezoidal
def f(x):
    return x*(x-1)
answer=53.33333333
print " Вычислить  интеграл : 53.33333333"
print trapezoidal.trapezoidal(f,2,6,2)
print "погрешность"+str(answer-trapezoidal.trapezoidal(f,2,6,2))
print trapezoidal.trapezoidal(f,2,6,100)
print "погрешность"+str(answer-trapezoidal.trapezoidal(f,2,6,100))
print rectangular.rectangular(f,2,6,2)
print "погрешность"+str(answer-rectangular.rectangular(f,2,6,2))
print rectangular.rectangular(f,2,6,100)
print "погрешность"+str(answer-rectangular.rectangular(f,2,6,100))