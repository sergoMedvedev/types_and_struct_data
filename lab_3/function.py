import math

'''функция для проверки на число'''


def is_number(s):
    try:
        int(s) or float(s)
        return True
    except ValueError:
        return False


'''функция для нахождения результата вычисления'''
def calculation_binary(number1, number2=1, operand=''):
    if operand == "+":
        return number1 + number2
    elif operand == "-":
        return number1 - number2
    elif operand == "*":
        return number1 * number2
    elif operand == "/":
        return number1 / number2
    elif operand == '^':
        return number1 ** number2
    elif operand == 'sin':
        return math.sin(number1)
    elif operand == 'cos':
        return math.cos(number1)
    elif operand == 'tg':
        return math.tan(number1)



def priority_algebraic(char):
    if char == "(" or char == ")":
        return 5
    elif char == "sin" or char == "cos" or char == "tg":
        return 4
    elif char == "^":
        return 3
    elif char == "*" or char == "/":
        return 2
    elif char == "+" or char == "-":
        return 1
    else:
        return 0