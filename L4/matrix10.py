# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 2 python matrix10.py

from numpy import array, append, random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def generateMatrix(m, n):
    matrix = array([0 for i in range(m * n)])
    for i in range(m):
        for j in range(n):
            matrix[n * i + j] = random.randint(1, 9)
    matrix.shape = (m, n)
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
    matrix = generateMatrix(m, n)
    print("\nM:", m, "\nN:", n, "\nМатрица:\n", matrix)
    print("Нечетные столбцы:\n", matrix[:, 0::2])