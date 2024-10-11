from matrix import Matrix
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