# -*- coding: utf-8 -*-
import rectangular
def f(x):
    return 2*x**3
def rect(a,b,N):
    sum=0
    step = (b-a)/N
    x=[]
    for i in range(0,N+1):
        x.append(a+i*step)
    for i in range(1,N+1):
        sum+=step*f(((x[i-1]+x[i])/float(2)))
    return sum
print rect(1,3,2)
print rectangular.rectangular(f,1,3,2)
def test():
    if rect(1,3,2)==rectangular.rectangular(f,1,3,2):
        print "значения совпадают"
    else:
        print "значения не совпадают"
test()
