# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 2 python passRandomDraw.py

import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = numpy.zeros(1)

if rank == 1:
    randNum = numpy.random.random_sample(1)
    print("Процесс", rank, "отобразил число", randNum)
    comm.Send(randNum, dest=0)

if rank == 0:
    print("Процесс", rank, "до получания работает с числом", randNum)
    comm.Recv(randNum, source=1)
    print("Процесс", rank, "получил число", randNum)