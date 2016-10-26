# -*- coding: utf-8 -*-
from random import *
import numpy as np

x=[]
for i in range(0,6):
    x.append(uniform(0,10))

arr =np.array(x)
print 'unsorted array : '+str(arr)
arr.sort()
print 'sorted array   : '+str(arr)


