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
    anB = matrix2.an

    dr = []
    anr=[]
    row = matrix1.row

    dr.append(1)
    anr.append(matrix1.an[0] + matrix2.an[0])
    indexA = 0
    indexB = 0
    for i in range(1, row, 1):

        startA = dA[i-1]
        finishA = dA[i]
        lenSegmA = finishA - startA

        startB = dB[i-1]
        finishB = dB[i]
        lenSegmB = finishB - startB


        diff = abs(lenSegmB-lenSegmA)

        flag = False
        if diff != 0:
            if lenSegmB > lenSegmA:
                for j in range(0, diff, 1):
                    cursor_element = anB[dB[i-1]+j]
                    if cursor_element != 0 and not flag:
                        anr.append(cursor_element)
                lenSegmA -=1
            else:
                for j in range(0, diff, 1):
                    cursor_element = anA[dA[i-1]+j]
                    if cursor_element != 0 and not flag:
                        anr.append(cursor_element)
                lenSegmA -= 1
            wasNotZeroElement = flag
            sum =0
            for j in range(0, lenSegmA, 1):

                summ = anA[dA[i]-lenSegmA+j]+anB[dB[i]-lenSegmB+j]

                if summ == 0 and not wasNotZeroElement and dA[i] != dA[i-1]+j:
                    continue

                anr.append(summ)
                wasNotZeroElement = True

            dr.append(len(anr))
        else:

            wasNotZeroElement = False
            for j in range(0, dA[i]- dA[i-1], 1):
                summ = 0
                summ = anA[dA[i-1]+j] + anB[dB[i-1]+j]

                if i == j and summ == 0:
                    anr.append(summ)

                if summ == 0 and wasNotZeroElement and dA != dA[i-1]+j:
                    continue

                anr.append(summ)
                wasNotZeroElement = True
            dr.append(len(anr))

    matrixResult.an = anr
    matrixResult.d = dr
    matrixResult.row = matrix1.row
    matrixResult.column = matrix1.column
    return matrixResult




















