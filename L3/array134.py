# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: mpirun -n 2 python array134.py

from numpy import array, random, nanmax, argmax, unravel_index
from scipy.spatial.distance import pdist, squareform
from math import dist
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def generateCoordinateList(size):
    coordinates = []
    for i in range(size):
        coordinates.append((random.randint(0, 9), random.randint(0, 9)))
    return coordinates

def searchMaximumDistance(coords):
    maxDist = dist(coords[0], coords[1])
    for i in range(0, len(coords) - 1):
        for j in range(i + 1, len(coords)):
            maxDist = max(dist(coords[i], coords[j]), maxDist)
    return maxDist

def searchCoordinatesWithDistance(coords, distance):
    pair = [(0, 0), (0, 0)]
    for i in range(0, len(coords) - 1):
        for j in range(i + 1, len(coords)):
            if distance == dist(coords[i], coords[j]):
                return [coords[i], coords[j]]
    return pair

if rank == 0:
    print("Введите n:")
    n = array([int(input())])
    comm.Send(n, 1)

if rank == 1:
    n = array([0])
    comm.Recv(n, 0)
    coordinates = generateCoordinateList(n[0])
    distance = searchMaximumDistance(coordinates)
    pair = searchCoordinatesWithDistance(coordinates, distance)
    print(
        "Координаты:", coordinates,
        "\nМаксимальное расстояние:", distance,
        "\nТочки, расположенные на максимальном расстоянии:", pair)
    