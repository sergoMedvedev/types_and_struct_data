from Stack import Stack
from function import is_number, priority_algebraic
from PolishEntry import PolishEntry

CONST_CHAR = ['/', '*', '^', '+', '-', 'sin', 'cos', 'tg']


class TranslationPolishNotation:
    '''
    класс является переводчиком обычного вырожения в польскую запись.

    поля:
        array_input_str - входной массив
        array_output_str - выходной массив
    методы
        tokin_scobka()- метод, который вызывается, когда встресается скобка
        tokin_xnak_operacii(tokin) - метод вызывается, когда встречается любой другой токин операции

    '''

    def __init__(self, int_array):
        self.input_array = int_array
        self.output_array = []
        self.stack = Stack()

    def tokin_scobka(self):
        while (True):
            if self.stack.stack[-1] != "(":
                self.output_array.append(self.stack.pop())
                continue
            else:
                self.stack.pop()
                break

    def tokin_znak_operacii(self, tokin):  # TODO исправить!!!
        while (True):
            if self.stack.stack == [] or self.stack.check() == "(":
                self.stack.push(tokin)
                return
            elif priority_algebraic(tokin) < priority_algebraic(self.stack.check()):
                self.output_array.append(self.stack.pop())
                while (True):
                    if priority_algebraic(tokin) <= priority_algebraic(self.stack.check()):
                        if self.stack.check() == "(":
                            self.stack.push(tokin)
                            return
                        else:
                            self.output_array.append(self.stack.pop())
                            continue
                    elif priority_algebraic(tokin) > priority_algebraic(self.stack.check()):
                        self.stack.push(tokin)
                        break
                    elif self.stack.stack[-1] == "(":
                        self.stack.push(tokin)
                        break
                return
            elif priority_algebraic(tokin) == priority_algebraic(self.stack.check()):
                self.output_array.append(self.stack.pop())
                self.stack.push(tokin)
                return
            elif (priority_algebraic(tokin) > priority_algebraic(self.stack.check())) or self.stack.stack == [] or \
                    self.stack.stack[-1] == "(":
                self.stack.push(tokin)
                break
            elif tokin == "(":
                return

    def transform_array(self):
        for tokin in self.input_array:
            if is_number(tokin) or tokin == "x":
                self.output_array.append(tokin)
                continue
            elif tokin == "(":
                self.stack.push(tokin)
                continue
            elif tokin == ")":
                self.tokin_scobka()
            elif tokin in CONST_CHAR:
                self.tokin_znak_operacii(tokin)

        if (self.stack.stack) != []:
            while (True):
                self.output_array.append(self.stack.pop())
                if self.stack.stack == []:
                    break



# ["(", 1, "+", 2, ")", "*", 3, "+", 10]
#[10, "+", 18, "*", "(", 1, "+", 7, "-", 8, "*", 2, "/", "(", 1, "/", 3, ")", "+", 1, ")", "+", 10]
