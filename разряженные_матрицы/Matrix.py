"""
- Класс Matrix

    Класс будет являться абстракцитей для представления матрицы.
    Этот класс будети являться верхним уровнем для нашей абстракции. Дальше будет происходить наследование от
    метода.


    поля:
    self.matrix - двумерный массив

    методы:
    readFile(nameFile: string)
    sumMatrix(matrix1: Matrix, matrix2: Matrix) => Result: Matrix

"""
import Error

class Matrix:
    def __init__(self, nameFile: str):
        self.matrix = self.readMatrix(nameFile)

    def readMatrix(self, namefile : str):
        new = []
        b = []
        try:
            file = open(namefile)
            array = [row.strip() for row in file]
            for i in range(len(array)):
                buff = array[i].strip("")
                for i in buff:
                    b.append(int(i))
                new.append(b)
                b = []
            return True, new
        except FileNotFoundError:
            errno = Error

