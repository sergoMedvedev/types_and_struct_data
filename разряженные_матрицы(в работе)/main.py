from matrix import Matrix, summMatrix
from method1 import *
from method2 import *

test1 = Matrix("1part/1matrix.txt")
test2 = Matrix("1part/2matrix.txt")

test3 = Matrix("2part/1matrix.txt")
test4 = Matrix("2part/2matrix.txt")

pakcMatrix2(test3)
print(test3.an)
print(test3.nr)
print(test3.nc)
print(test3.jr)
print(test3.jc)

unpackMatrix2(test3)

test3.printMatrixunpacking()









