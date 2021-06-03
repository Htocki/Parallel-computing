# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: python array23.py

import numpy
import random

k = 3
l = 7
n = 10

array = numpy.array([random.randint(0, 9) for i in range(n)])
sum = numpy.sum(array[0:k]) + numpy.sum(array[l+1:len(array)])

print("Массив:", array, "Сумма:", sum)