from matrix import Matrix, summMatrix
from method1 import packMatrix
# Лабораторная работа по Разрежанным матрицам.


test1 = Matrix("1matrix.txt")
test2 = Matrix("2matrix.txt")

mass = summMatrix(test2.matrix, test1.matrix)
test3 = Matrix()
test3.matrix = mass

test3.printMatrix()

