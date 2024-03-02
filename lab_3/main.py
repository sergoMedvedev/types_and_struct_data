from Interface import Interface
from PolishEntry import PolishEntry

mass = [1,2,3,4,5,5,6]
print(mass)
mass.pop(-1)
print(mass)

print("Лабораторная работа")
print("Введите строку для расчета: ", end=' ')
in_str = input()

interface = Interface("Польская запись", in_str)
while(True):
    if interface.check_validate():
        break
    else:
        print("Допущена ошибка в строке. Необходимо записать строку без букв. "
              "Если хотите задать функцию, то в качестве авгумента используйте x .")
        print("Введите строку для расчета: ", end=' ')
        interface.input_string = input()






