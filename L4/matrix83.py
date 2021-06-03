# Программа написана и проверена на Python 3.9.5
# Комманда для выполнения программы: python matrix83.py

from numpy import array, random, diagonal, sum, fliplr

def arithmeticMeans(matrix):
    arithMeams = array([0. for i in range(len(matrix))])
    matrix = fliplr(matrix)
    for i in range(len(matrix)):
        d = diagonal(matrix, offset = len(matrix) - 1 - i)
        arithMeams[i] = sum(d) / len(d)
    return arithMeams

print("Введите m:")
m = int(input())
a = array([random.randint(1, 9) for i in range(m * m)])
a.shape = (m, m)
print("\nM:", m, "\nМатрица:\n", a)
print(
    "среднее арифметическое элементов диагоналей параллельных побочной:\n",
    arithmeticMeans(a))