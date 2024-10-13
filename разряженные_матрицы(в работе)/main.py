from matrix import Matrix, summMatrix
from method1 import *
from method2 import *

test1 = Matrix("1part/1matrix.txt")
test2 = Matrix("1part/2matrix.txt")

test3 = Matrix("2part/1matrix.txt")
test4 = Matrix("2part/2matrix.txt")


pakcMatrix2(test3)
pakcMatrix2(test4)

test4.transpose()

res1 = multiplicationMatrix(test3, test4)
res1.printMatrix()
print("первая матрица")
print()

res = multiplicationMatrixMR(test3, test4)
unpackMatrix2(res)
res.printMatrixunpacking()











