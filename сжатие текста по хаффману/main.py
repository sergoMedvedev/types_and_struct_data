from pyparsing import empty


class Node:

    def __init__(self, item, value: int, r, l, byte):
        self.item = item  # символ
        self.value = value  # значение повторения
        self.r = r  # правый корень
        self.l = l  # левый корень
        self.byteNumber = byte

def main(string: str):
    # функция будет производить сжатие по хаффману.
    string.lower()

    # словать, который будет хранить в себе симво ли количество раз, за которое он встретился
    frequency = {}

    # вычисляем частотность
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # сортируем словарь по по возрастанию
    frequency = dict(sorted(frequency.items(), key=lambda x: x[1]))
    print(frequency)

    leftTree = None
    rithtTree = None

    for item in frequency.keys():
        left = None
        ritht = None
        if rithtTree == None:
            ritht = Node(item, frequency[item], None, None, 1)
            continue
        elif leftTree == None:
            left = Node(item, frequency[item], None, None, 0)
            continue
        # обработать краевые моменты пустота, один символ

        if left != None and ritht != None:

            if rithtTree == None and leftTree == None:
                rithtTree = Node(item, frequency[item], ritht, left, 1)
                left = None
                ritht = rithtTree
            elif leftTree != None and rithtTree != None:
                leftTree = Node(item, frequency[item], ritht, left, 0)
                left = leftTree
                ritht = leftTree

        elif left == None and ritht != None:
            pass







main("aa aaabb ff fh")
