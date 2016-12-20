# -*- coding: utf-8 -*-
import tradezial
def f(x):
    return 2*x**3
def my_trapezodial (a,b,N):
    sum=0
    x=[]
    step =(b-a)/N
    for i in range(0,N+1):
        x.append(a+i*step)
    for i in range(1,N+1):
        sum += step*(f(x[i-1])+f(x[i]))/float(2)
    return sum

print my_trapezodial(1,3,2)
print tradezial.trapezoidal(f,1,3,2)

def testing():
    if my_trapezodial(1,3,2)==tradezial.trapezoidal(f,1,3,2):
        print "значения совпадают"
    else :
        print "значения не совпадают"
testing()