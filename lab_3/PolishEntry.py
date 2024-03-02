from Stack import Stack
from function import is_number, calculation_binary

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

    def __init__(self, polish_str):
        self.input_polish_string = polish_str
        self.result = 0
        self.calculation()

    '''Вычисления для обычных вырожений'''

    def calculation(self):
        stack_result = Stack()

        for char in self.input_polish_string:

            if is_number(char):
                stack_result.push(char)
                continue

            elif (char in BINARY_OPERANDS):
                number2 = float(stack_result.pop())
                number1 = float(stack_result.pop())
                stack_result.push(stack_result.push(calculation_binary(number1, number2, char)))
                stack_result.stack.remove(None)

            elif (char in UNARY_OPERANDS):
                number1 = stack_result.pop()
                stack_result.push(stack_result.push(calculation_binary(number1=number1, operand=char)))
                stack_result.stack.remove(None)

        self.result = stack_result.pop()

    def calculation_func(self):
        pass
        # TODO НАПИСАТЬ МЕТОД ЛЯ РАСЧЕТА ВЫРОЖЕНИЯ, КОТОРАЯ ПРЕДСТАВЛЕННА В ВИДЕ ФУНКЦИИ
