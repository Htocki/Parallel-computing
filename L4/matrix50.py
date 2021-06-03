# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 2 python matrix20.py

from numpy import argmax, argmin, array, random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def swap(matrix):
    maxs = argmax(matrix, axis = 0)
    mins = argmin(matrix, axis = 0)
    for i in range(len(maxs)):
        max = matrix[maxs[i], i]
        matrix[maxs[i], i] = matrix[mins[i], i]
        matrix[mins[i], i] = max
    return matrix

if rank == 0:
    print("Введите m:")
    m = int(input())
    print("Введите n:")
    n = int(input())
    comm.Send(array([n, m]), 1)

if rank == 1:
    data = array([0, 0])
    comm.Recv(data, 0)
    n = data[0]
    m = data[1]
    matrix = array([random.randint(1, 9) for i in range(m * n)])
    matrix.shape = (m, n)
    print("\nM:", m, "\nN:", n, "\nМатрица:\n", matrix)
    print("Матрица после перестановки:\n", swap(matrix))