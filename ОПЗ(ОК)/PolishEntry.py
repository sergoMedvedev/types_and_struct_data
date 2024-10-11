from Stack import Stack
from function import is_number, calculation_binary,print_point
from ErrorEntity import ErrorEntity

BINARY_OPERANDS = ['/', '*', '+', '-', '^']
UNARY_OPERANDS = ['sin', 'cos', 'tg', 'ctg']


class PolishEntry(ErrorEntity):
    """
    Данный класс высчитывает по польской записи значение выражения

    поля:
        input_polish_string обратная польская запись

    методы:
        calculation() -  вычисления для обычного вырожения
        метод вычисления для функции
    """

    def __init__(self, polish_str, condition):
        self.input_polish_string = polish_str
        self.result = 0
        self.condition = condition
        self.error = ErrorEntity()
        if condition == 1:
            self.calculation_func()
        else:
            self.calculation()

    '''Вычисления для обычных вырожений'''

    def calculation(self, x=""):
        stack_result = Stack()


        for char in self.input_polish_string:
            try:
                if is_number(char):
                    stack_result.push(char)
                    continue

                elif char == "x":
                    stack_result.push(x)
                    continue

                elif char == "":
                    stack_result.push(x)
                    continue

                elif (char in BINARY_OPERANDS):
                    if (self.input_polish_string != [] and stack_result.check_two_arg()):
                        number2 = float(stack_result.pop())
                        number1 = float(stack_result.pop())

                        stack_result.push(calculation_binary(number1, number2, char))
                        continue
                    else:
                        self.error.error_OPZ_undefind_arg()

                elif (char in UNARY_OPERANDS):
                    number1 = float(stack_result.pop())
                    stack_result.push(stack_result.push(calculation_binary(number1=number1, operand=char)))
                    stack_result.stack.remove(None)
                self.result = stack_result.check()
                if x != "":
                    return self.result
                else:
                    return None
            except ZeroDivisionError:
                if x == '':
                    return print("Деление на нуль")
                else:
                    return "-"
            except FloatingPointError: # 0 ^ -k и ещё отриц. число в нецелой степени (корень из отриц. числа)
                return "-"
            except ValueError:
                return print("ошибка привычислении. корень из отр. числа")

        self.result = stack_result.pop()
        return self.result
        #

    def calculation_func(self):  # TODO НАПИСАТЬ МЕТОД ЛЯ РАСЧЕТА ВЫРОЖЕНИЯ, КОТОРАЯ ПРЕДСТАВЛЕННА В ВИДЕ ФУНКЦИИ
        print("ВВедите интервалы для нахождения значений функции")
        print("Первое значение х1=", end='')
        x1 = float(input())
        print("Второе значение х2=", end='')
        x2 = float(input())
        print("Введите шаг h=", end='')
        h = float(input())

        if x2 < x1 or x1 == '' or x2 == '' or h < 0:
            self.calculation_func()

        delt = x1
        array_point =[]

        while (delt <= x2):
            array_point.append(delt)
            delt+=h
            if delt>x2:
                array_point.append(x2)
            else:
                continue
        print(array_point)

        for point in array_point:

            print_point(point,self.calculation(point))





-(-(-(-1)))+100

#9+10) ТЕСТ


