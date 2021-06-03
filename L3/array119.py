# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 2 python array119.py

import numpy
import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def createArray(size):
    array = numpy.arange(size)
    array = numpy.repeat(array, 2)
    array = array[0:size]
    return array

def repeatSeries(array):
    size = len(array)
    i = 0
    while i < size:
        if i == 0 or array[i] != array[i-1]:
            array = numpy.insert(array, i, array[i])
            size += 1
        i += 1
    return array

if rank == 0:
    print("Введите n:")
    n = numpy.array([int(input())])
    comm.Send(n, 1)

if rank == 1:
    n = numpy.array([0])
    comm.Recv(n, 0)
    array = createArray(n[0])
    print("Процесс:", rank, "Массив:", array)
    array = repeatSeries(array)
    print("Процесс:", rank, "Массив:", array)