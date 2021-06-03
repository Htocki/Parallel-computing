# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы:
# mpiexec -n 4 python trapParallel_1.py 0.0 1.0 10000

import numpy
import sys
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

a = float(sys.argv[1])
b = float(sys.argv[2])
n = int(sys.argv[3])

def f(x):
    return x * x

def integrateRange(a, b, n):
    integral = -(f(a) + f(b)) / 2.0
    for x in numpy.linspace(a, b, n + 1):
        integral = integral + f(x)
    integral = integral * (b - a) / n
    return integral

h = (b - a) / n
local_n = n / size
local_a = a + rank * local_n * h
local_b = local_a + local_n * h

integral = numpy.zeros(1)
recv_buffer = numpy.zeros(1)

integral = integrateRange(local_a, local_b, local_n)

if rank == 0:
    total = integral[0]
    for i in range(1, size):
        comm.Recv(recv_buffer, ANY_SOURCE)
        total += recv_buffer[0]
else:
    comm.Send(integral)

if comm.rank == 0:
    print("Интеграл от", a, "до", b, ", разделенный на", n, "трапеций равен",
    total, ".")