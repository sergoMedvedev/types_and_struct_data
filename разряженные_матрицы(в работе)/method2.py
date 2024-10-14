# В данном файле были реализованы функции для метода Рейнбольдта-Местеньи

from matrix import Matrix

#Метод для упаковки методом Рейнбольдта-Местеньи
def pakcMatrix2(matrix):
    mass = matrix.matrix
    an = []
    nr = []
    nc = []
    jr = []
    jc = []

    for i in range(0, matrix.row):
        jr.append(-1)

    for i in range(0, matrix.column):
        jc.append(-1)

    for i in range(0, matrix.row):
        for j in range(0, matrix.column):
            if mass[i][j] != 0:
                an.append(mass[i][j])

                if jr[i] == -1:
                    jr[i] = len(an)-1
                    nr.append(len(an)-1)
                else:
                    nr.append(jr[i])

                    cur_idx = jr[i]

                    while nr[cur_idx] != jr[i]:
                        cur_idx +=1

                    nr[cur_idx] = len(an) - 1

                if jc[j] == -1:
                    jc[j] = len(an) - 1
                    nc.append(len(an) - 1)
                else:
                    nc.append(jc[j])
                    cur_idx = jc[j]

                    while nc[cur_idx] != jc[j]:
                        cur_idx+=1

                    nc[cur_idx] = len(an) -1

    matrix.an = an
    matrix.nr = nr
    matrix.nc = nc
    matrix.jc = jc
    matrix.jr = jr

def unpackMatrix2(matrix):
    an = matrix.an
    nr = matrix.nr
    nc = matrix.nc
    jr = matrix.jr
    jc = matrix.jc

    mass = []

    for i in range(0, matrix.row):
        buff = []
        for j in range(0, matrix.column):
            buff.append(0)
        mass.append(buff)

    for i in range(0, len(an)):
        col_inx = -1
        row_inx = -1
        cur_nc = nc[i]
        cur_nr = nr[i]

        while col_inx == -1:
            for j in range(0, matrix.column):
                if jc[j] == cur_nc:
                    col_inx = j
                    break

            cur_nc = nc[cur_nc]

        while row_inx == -1:
            for j in range(0, matrix.row):
                if jr[j] == cur_nr:
                    row_inx = j
                    break

            cur_nr = nr[cur_nr]

        mass[row_inx][col_inx] = an[i]

    matrix.unpackingMatrix = mass


def multiplicationMatrix(matrix1, matrix2): # возвращает новую матрицу
    mass1 = matrix1.matrix
    mass2 = matrix2.matrix
    resultMatrix = Matrix()


    if matrix1.column != matrix2.row:
        print("Число столбцов первой матрицы должно быть равно числу строк второй матрицы")
        return resultMatrix


    result = [[0 for _ in range(len(mass2[0]))] for _ in range(len(mass1))]

    # Умножение матриц
    for i in range(len(mass1)):
        for j in range(len(mass2[0])):
            for k in range(len(mass2)):
                result[i][j] += mass1[i][k] * mass2[k][j]
    resultMatrix.matrix = result
    return resultMatrix

def multiplicationMatrixMR(matrix1, matrix2): # возвращает матрицу и ее параметры упаковки
    resultMatrix = Matrix()

    if matrix1.column != matrix2.row:
        print("Число столбцов первой матрицы должно быть равно числу строк второй матрицы")
        return resultMatrix

    indexRow = 0
    indexcol = 0

    an = []
    nr = []
    nc = []
    jr = []
    jc = []

    for i in range(0, matrix1.row):
        jr.append(-1)

    for i in range(0, matrix2.column):
        jc.append(-1)

    for i in range(0, matrix1.row):
        indexRow = matrix1.jr[i]

        #если строка пустая, то переходим к следующей
        if indexRow == -1:
            continue

        for j in range(0, matrix2.column):
            indexcol = matrix2.jc[j]

            if indexcol == -1:
                continue

            sum = 0

            rowEnd = False

            while not rowEnd: # цикл прохода по текущей строке
                colEnd = False
                # поиск текущего индекса по столбцу или строке в зависимости от переданных элементов
                curRowElemInx = getCurrentInd(indexRow, matrix1.column, matrix1.jc, matrix1.nc)

                while not colEnd:
                    curColElemIdx = getCurrentInd(indexcol, matrix2.row, matrix2.jr, matrix2.nr)
                    if curColElemIdx > curRowElemInx: # если индекс элемента в колонке больше индекса элемента в строке, то нет смысла продолжать
                        break

                    #пороверка совпадения индекса элемента строки и столбца
                    if curColElemIdx == curRowElemInx:
                        sum += matrix1.an[indexRow] * matrix2.an[indexcol]

                    indexcol = matrix2.nc[indexcol] #следующий индекс столбца

                    if indexcol == matrix2.jc[j]: # если прошел круг - выход
                        colEnd = True

                indexRow = matrix1.nr[indexRow] # следующий индекс

                if indexRow == matrix1.jr[i]: # если прошел круг - вышел
                    rowEnd = True

            if (sum != 0):
                jr, nr = setFirstIdxAndNextIdx(i, jr, nr, len(an)) #заполнение массива jr и nr
                jc, nc = setFirstIdxAndNextIdx(j, jc, nc, len(an))  # заполнение массива jc и nc
                an.append(sum) # заполняем an

    resultMatrix.row = matrix1.row
    resultMatrix.column = matrix2.column
    resultMatrix.an = an
    resultMatrix.nr = nr
    resultMatrix.nc = nc
    resultMatrix.jr = jr
    resultMatrix.jc = jc

    return resultMatrix





def setFirstIdxAndNextIdx(idx, jr, nr, an_size):
    if jr[idx] ==-1:
        jr[idx] = an_size
        nr.append(an_size)
    else:
        nr.append(jr[idx])
        cur_idx = jr[idx]

        while nr[cur_idx] != jr[idx]:
            cur_idx += 1

        nr[cur_idx] = an_size

    return jr, nr



def getCurrentInd(indexRow, column, jc, nc):
    idx = -1
    while idx == -1:
        for i in range(0, column):
            if jc[i] == indexRow:
                idx = i
                break

        indexRow = nc[indexRow]

    return idx


