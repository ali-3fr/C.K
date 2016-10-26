# -*- coding: utf-8 -*-
def average(N):
    sum=0
    for i in range(0,N+1):
        sum+=i
    return sum/N
N = input(u'Введите натуральное число N:')
print 'среднее значение целых чисел i=1,2,…,N : '+ str(average(N))



