# -*- coding: utf-8 -*-
# Программа для вычисления Объема трех кубов
from numpy import linspace
import matplotlib.pyplot as mpl
L = linspace(1.0,3.0,num=3)
V=L**3
print 'Объем  трех кубов : '+ str(V)
mpl.plot(L,V,'o')
mpl.show()
