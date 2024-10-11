from matrix import Matrix, summMatrix
from method1 import packMatrix, unpackingMatrix, summMatrixs
# Лабораторная работа по Разрежанным матрицам.


test1 = Matrix("1matrix.txt")
test2 = Matrix("2matrix.txt")

packMatrix(test1)
packMatrix(test2)

#summMatrixs(test1, test2)

print(test1.d)
print(test1.an)

print(test2.d)
print(test2.an)

test2.printMatrix()
print()
unpackingMatrix(test2)
test2.printMatrixunpacking()


#unpackingMatrix(test1)


# print()
# test1.printMatrix()




