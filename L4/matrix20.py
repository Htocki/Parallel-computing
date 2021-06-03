# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 2 python matrix20.py

from numpy import array, append, prod, random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

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
    print("Произведения элементов столбцов:\n", prod(matrix, axis = 0))