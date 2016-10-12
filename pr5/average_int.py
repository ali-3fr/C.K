# -*- coding: utf-8 -*-
# Программа для вычисления Среднего значение целых чисел
list1=range(1,6,1)
sum=0
for each_number in list1:
    sum+=each_number
average = (float)(sum/len(list1))
print 'среднее значение 1 , 2 , 3 , 4 , 5 :   ' + str(average)