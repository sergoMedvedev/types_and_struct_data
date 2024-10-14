from matrix import Matrix, summMatrix
from method1 import *
from method2 import *


def method1():
    test1 = Matrix("1part/1matrix.txt")
    test2 = Matrix("1part/2matrix.txt")

    packMatrix(test1)
    packMatrix(test2)

    print("|Матрица 1|")
    test1.printMatrix()
    print()
    print("|Матрица 2|")
    test2.printMatrix()
    print("-------------------------------")
    print("\n")

    print("|Сжатый формат 1 матрицы|")
    print(test1.an)
    print(test1.d)
    print("")

    print("|Сжатый формат 2 матрицы|")
    print(test2.an)
    print(test2.d)

    print("\n")
    print("-------------------------------")

    print("обычное сложение:")
    res = summMatrix(test1, test2)
    res.printMatrix()

    print("специальная сумма:")

    res1 = summMatrixs(test1, test2)
    print()
    print("сжатый ввид:")
    print(res1.an)
    print(res1.d)
    print()
    print("обычный ввид:")

    unpackingMatrix(res1)
    res1.printMatrixunpacking()


print("Лабораторная работа по разреженным матрицам")
print("Выберите вариант лабораторной работы:")
print("\t 1 - схема Дженннинга (первая часть)")
print("\t 2 - схема Рейнбольдца - Мусееньи (вторая часть)")
str = "1"
while (True):
    print("Введите номер действия:", end=" ")
    str = input()
    if str == "1":
        method1()
    elif str == "2":
        pass
    elif str == "0":
        exit()
    else:
        print("Введите корректное номер метода!")
        continue