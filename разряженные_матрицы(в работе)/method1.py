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
            if mass[i][j] != 0 or wasNotZeroElement  :
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
                break
            if i-j >= quantityElemenToRowS:
                matrixRezult[i][j] = 0
                matrixRezult[j][i] = 0
            elif i-j < quantityElemenToRowS:
                matrixRezult[i][j] = an[indexAnArray]
                matrixRezult[j][i] = an[indexAnArray]
                indexAnArray+=1
        indexDarray +=1
    matrix.unpackingMatrix = matrixRezult







def unpackingMatrix2(elements, row_ptr, n):
    # Размер матрицы n равен количеству строк (длина row_ptr)
    n = len(row_ptr)

    # Создаем матрицу n x n, заполненную нулями
    matrix = numpy.zeros((n, n))

    # Индекс в массиве elements
    element_index = 0

    # Проходим по каждой строке
    for i in range(n):
        # Начало и конец элементов для строки i
        start = row_ptr[i] - 1  # Начало строки в elements
        end = row_ptr[i + 1] - 1 if i + 1 < len(row_ptr) else len(elements)  # Конец строки в elements

        # Проходим по каждому элементу строки
        for j in range(i, end - start + i):
            matrix[i, j] = elements[element_index]  # Заполняем верхний треугольник
            matrix[j, i] = elements[element_index]  # Симметрично заполняем нижний треугольник
            element_index += 1

    return matrix











