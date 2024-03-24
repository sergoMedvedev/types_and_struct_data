from Stack import Stack
from function import is_number, calculation_binary,print_point

BINARY_OPERANDS = ['/', '*', '+', '-', '^']
UNARY_OPERANDS = ['sin', 'cos', 'tg', 'ctg']


class PolishEntry:
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
        if condition == 1:
            self.calculation_func()
        else:
            self.calculation()

    '''Вычисления для обычных вырожений'''

    def calculation(self, x=""):
        stack_result = Stack()


        for char in self.input_polish_string:

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
                number2 = float(stack_result.pop())
                number1 = float(stack_result.pop())
                stack_result.push(stack_result.push(calculation_binary(number1, number2, char)))
                stack_result.stack.remove(None)

            elif (char in UNARY_OPERANDS):
                number1 = float(stack_result.pop())
                stack_result.push(stack_result.push(calculation_binary(number1=number1, operand=char)))
                stack_result.stack.remove(None)
        self.result = stack_result.pop()
        if x != "":
            return self.result
        else:
            return None


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








