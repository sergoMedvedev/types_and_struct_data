from Interface import Interface
from PolishEntry import PolishEntry
from TranslationPolishNotation import TranslationPolishNotation



print("Лабораторная работа")
print("Введите строку для расчета: ", end=' ')
in_str = input()

interface = Interface("Польская запись", in_str)
while (True):
    if interface.check_validate():
        break
    else:
        print("Допущена ошибка в строке. Необходимо записать строку без букв. "
              "Если хотите задать функцию, то в качестве авгумента используйте x .")
        print("Введите строку для расчета:", end='')
        interface.input_string = input()



array_transform = TranslationPolishNotation(interface.input_string)

array_transform.transform_array()

condition = interface.have_x()
print(condition)

print(array_transform.output_array)
polish_result = PolishEntry(array_transform.output_array, condition)

print(polish_result.result)

print("Конец програмы!")
