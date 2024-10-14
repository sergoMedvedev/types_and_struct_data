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


def method2():
    test1 = Matrix("2part/1matrix.txt")
    test2 = Matrix("2part/2matrix.txt")


    pakcMatrix2(test1)
    pakcMatrix2(test2)

    print("|Матрица 1|")
    test1.printMatrix()
    print()
    print("|Матрица 2|")
    test2.printMatrix()
    print("-------------------------------")
    print("\n")

    print("|Сжатый формат 1 матрицы|")
    print("an = ", test1.an)
    print("nr = ", test1.nr)
    print("nc = ", test1.nc)
    print("jc = ", test1.jc)
    print("jr = ", test1.jr)

    print("")

    print("|Сжатый формат 2 матрицы|")
    print("an = ", test2.an)
    print("nr = ", test2.nr)
    print("nc = ", test2.nc)
    print("jc = ", test2.jc)
    print("jr = ", test2.jr)

    print("\n")
    print("-------------------------------")

    print("обычное умножение:")
    res = multiplicationMatrix(test1, test2)
    res.printMatrix()
    print()

    print("специальное умножение:")

    res1 = multiplicationMatrixMR(test1, test2)
    print()
    print("сжатый ввид:")
    print("an = ", res1.an)
    print("nr = ", res1.nr)
    print("nc = ", res1.nc)
    print("jc = ", res1.jc)
    print("jr = ", res1.jr)
    print()
    print("обычный ввид:")

    unpackMatrix2(res1)
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
        method2()
    elif str == "0":
        exit()
    else:
        print("Введите корректное номер метода!")
        continue
