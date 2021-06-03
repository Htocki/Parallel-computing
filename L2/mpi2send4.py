# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 4 python mpi2send4.py

import numpy
import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

messages = 0
processCount = 4
default = -1

def getNondefaultValuesCount(array):
    for i in range(len(array)):
        if array[i] == default:
            return i

def removeDefaulValues(array):
    size = getNondefaultValuesCount(array)
    return array[0:size]

if rank == 0:
    first = 0
    second = 0
    third = 0

    while messages < processCount - 1:
        data = numpy.array([default for i in range(6)])
        comm.Recv(data, MPI.ANY_SOURCE)
        sender = data[0]
        data = data[1:len(data)]
        data = removeDefaulValues(data)
        print("Текущий:", rank, "Отправитель:", sender, "Набор:", data)
        messages += 1
        
        if sender == 1:
            first = data
        if sender == 2:
            second = data
        if sender == 3:
            third = data

        if (messages == processCount - 1):
            print("Результат:\n", first, "\n", second, "\n" , third)
    
else:
    size = random.randint(1, 5)
    data = numpy.array([random.randint(0, 9) for i in range(size)])
    data = numpy.insert(data, 0, rank)
    print("Текущий:", rank, "Набор:", data[1:len(data)])
    comm.Send(data, 0)