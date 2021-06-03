# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 4 python mpi1proc4.py

import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def quad(x):
    return x * x

if rank % 2 == 0:
    value = numpy.random.randint(0, 9)
    print("Процесс", rank, "Значение:", value, "Квадрат:", quad(value))