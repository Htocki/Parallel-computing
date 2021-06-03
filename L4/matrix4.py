# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 2 python matrix4.py

from numpy import array, append, random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def generateMatrix(m, set):
    matrix = array([0 for i in range(m * len(set))])
    for i in range(m):
        for j in range(len(set)):
            matrix[len(set) * i + j] = set[j]
    matrix.shape = (m, len(set))
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
    set = array([random.randint(0, 9) for i in range(n)])
    print("M:", m, "N:", n, "Набор:", set)
    matrix = generateMatrix(m, set)
    print("Матрица:\n", matrix)