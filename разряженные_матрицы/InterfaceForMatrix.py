"""

    Этот класс будет работать с объектами матриц, выполнять проверку, выводить информацию на экран.

    - поля

    -методы
    checkResult(matrix1: Matrix, matrix2: Matrix) info: string


"""
from AbstractInterface import AbstractInterface
from Дженингса import Дженингс
class InterfaceForMatrix(AbstractInterface):

    def __init__(self):
        print("Начало работы\n")
        print("какую часть ЛР выолнять? (Введите 1 - первая часть, 2 - вторая часть)\n:")
        numberPart = str(input())

        if numberPart == "1":
            matrix = Дженингс("разряженные_матрицы/data/symmetrical/matrix1.txt")



    def packing(self):
        pass




    def checkResult(self, matrix1, matrix2):
        pass




