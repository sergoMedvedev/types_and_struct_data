import numpy

from matrix import Matrix
from numpy import zeros
#Метод сжания по Дженнингу

def packMatrix(matrix):
    mass = matrix.matrix
    an = []
    d =[]

    an.append(mass[0][0])
    d.append(1)

    for i in range(1, len(mass), 1):
        wasNotZeroElement = False

        for j in range(0, i+1, 1):
            if mass[i][j] != 0 or wasNotZeroElement or j == i:
                wasNotZeroElement = True
                an.append(mass[i][j])

        d.append(len(an))

    matrix.an = an
    matrix.d = d


def unpackingMatrix(matrix):
    an = matrix.an
    d = matrix.d
    rows = matrix.row
    column = matrix.column


    matrixRezult = []
    for i in range(rows):
        buf = []
        for j in range(column):
            buf.append(".")
        matrixRezult.append(buf)

    matrixRezult[0][0] = an[0]
    indexAnArray = 1
    indexDarray = 0
    for i in range(1, rows, 1):
        quantityElemenToRowS = d[indexDarray+1] - d[indexDarray]
        for j in range(0, i+1, 1):
            lenRow = i+1
            if quantityElemenToRowS == 0:
                matrixRezult[i][j] = 0
                matrixRezult[j][i] = 0
            if i-j >= quantityElemenToRowS:
                matrixRezult[i][j] = 0
                matrixRezult[j][i] = 0
            elif i-j < quantityElemenToRowS:
                matrixRezult[i][j] = an[indexAnArray]
                matrixRezult[j][i] = an[indexAnArray]
                indexAnArray+=1
        indexDarray +=1
    matrix.unpackingMatrix = matrixRezult


def summMatrixs(matrix1, matrix2):

    #создадим пустую матрицу
    matrixResult = Matrix()

    dA = matrix1.d
    anA = matrix1.an

    dB = matrix2.d
    anB = matrix2.d

    dr = []
    anr=[]
    row = matrix1.row

    dr.append(1)
    anr.append(matrix1.an[0] + matrix2.an[0])
    indexA = 1
    indexB = 1
    for i in range(1, row, 1):
        startA = dA[i-1]
        finishA = dA[i]
        lenSegmA = finishA - startA

        startB = dB[i-1]
        finishB = dB[i]
        lenSegmB = finishB - startB

        for j in range(0, i, 1):
            pass








