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

                    cursor_idx = jr[i]

                    while nr[cursor_idx] != jr[i]:
                        cursor_idx +=1

                    nr[cursor_idx] = len(an) - 1

                if jc[j] == -1:
                    jc[j] = len(an) - 1
                    nc.append(len(an) - 1)
                else:
                    nc.append(jc[j])
                    cursor_idx = jc[j]

                    while nc[cursor_idx] != jc[j]:
                        cursor_idx+=1

                    nc[cursor_idx] = len(an) -1

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



