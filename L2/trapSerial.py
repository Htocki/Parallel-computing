# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: python trapSerial.py 0.0 1.0 1000

import numpy
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
n = int(sys.argv[3])

def f(x):
    return x * x

def integrateRange(a, b, n):
    '''Целочисленное интегрирование на интервеле от a до b по правилу
    трапеций, разбивая интервал на n трапеций.'''
    integral = -(f(a) + f(b)) / 2.0
    for x in numpy.linspace(a, b, n + 1):
        integral = integral + f(x)
    integral = integral * (b - a) / n
    return integral

integral = integrateRange(a, b, n)
print("Интеграл от", a, "до", b, ", разделенный на", n, "трапеций равен",
    integral, ".")