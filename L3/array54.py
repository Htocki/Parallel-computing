# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: python array54.py

import numpy
import random

print("Введите n:")
n = int(input())

a = numpy.array([random.randint(0, 9) for i in range(n)])
b = numpy.array([value for value in a if not value % 2])

print("Массив A:", a)
print("Массив B:", b, "Сумма элементов:", numpy.sum(b))