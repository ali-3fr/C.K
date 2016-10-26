# -*- coding: utf-8 -*-
def y(t):
    #при удалении двоеточия : SyntaxError: invalid syntax
    v0 = 5  # Начальная скорость
    #при удалении отступа перед выражением v0 = 5 : IndentationError: expected an indented block
    #если отступ перед v0 = 5 будет из трех пробелов : IndentationError: unexpected indent
    # если Удалить первую круглую скобку :  SyntaxError: invalid syntax
    # если Удалить аргумент t  :  print y(t) TypeError: y() takes no arguments (1 given)
    g = 9.81  # Ускорение свободного падения
    return v0 * t - 0.5 * g * t ** 2


t = 0.6  # Время
print y(t)
#Заменить первое выражение print y(t) на print y()  :  print y() TypeError: y() takes exactly 1 argument (0 given)
t = 0.9
print y(t)
