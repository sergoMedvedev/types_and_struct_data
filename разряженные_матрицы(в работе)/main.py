from matrix import Matrix, summMatrix
from method1 import packMatrix, unpackingMatrix, summMatrixs

test1 = Matrix("1matrix.txt")
test2 = Matrix("2matrix.txt")

packMatrix(test1)
packMatrix(test2)

test1.printMatrix()
print()
test2.printMatrix()
print()
massR = summMatrixs(test1, test2)
unpackingMatrix(massR)
massR.printMatrixunpacking()







