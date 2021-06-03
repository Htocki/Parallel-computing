# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 2 python array68.py

from numpy import array, arange
import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    print("Введите n:")
    n = array([int(input())])
    comm.Send(n, 1)

if rank == 1:
    n = array([0])
    comm.Recv(n, 0)
    array = arange(0, n[0], 1)
    print("Процесс:", rank, "Массив:", array)
    
    maximum = max(array)
    minimum = min(array)
    for i in range(len(array)):
        if array[i] == maximum:
            array[i] = minimum
        elif array[i] == minimum:
            array[i] = maximum
    
    print("Процесс:", rank, "Массив:", array)
