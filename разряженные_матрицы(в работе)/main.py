from matrix import Matrix, summMatrix
from method1 import packMatrix, unpackingMatrix, unpackingMatrix2
# Лабораторная работа по Разрежанным матрицам.


test1 = Matrix("1matrix.txt")
test2 = Matrix("2matrix.txt")

packMatrix(test1)
print(test1.d)
print(test1.an)

#print(unpackingMatrix2(test1.an, test1.d, test1.row))

unpackingMatrix(test1)

test1.printMatrixunpacking()
# print()
# test1.printMatrix()




