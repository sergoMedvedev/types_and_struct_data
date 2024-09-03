class Node:

    def __init__(self, weight, left, right, number):
        self.number = number # число это 1 или 0
        self.weight = weight # вес вершины это число
        self.left = self.getBreachLeft(left) #ссылка на левую вершину
        self.right = self.getBreachRigth(right) #ссылка на правую вершину
        self.totleResult = self.summTotleResult(self.left, self.right) # суммарный вес

    def summTotleResult(self, left, right):
        if left == None:
            return 0
        if right == None:
            return 0
        return left.getWeight() + right.getWeight()

    def getWeight(self):
        if self.weight == 0:
            return 0
        return self.weight

    def getBreachLeft(self, left):
        if left == None:
            return None
        return left

    def getBreachRigth(self, right):
        if right == None:
            return None
        return right


def makeUnit(weight, name, number):
    if name != "":
        return Node(weight, None, None, number)



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

    #Построение дерева Хаффмана

    dictResult ={}


    # ТУТ КАКОЕ-ТО ГОВНО! НАДО ПОДУМАТЬ И РЕАЛИЗОВАТЬ!!!!!!!!!

    while frequency != {}:
        frequency = dict(sorted(frequency.items(), key=lambda x: x[1]))
        print(frequency)
        left = makeUnit(frequency[list(frequency.keys())[0]], list(frequency.keys())[0], 1)
        dictResult[left] = list(frequency.keys())[0]
        del frequency[list(frequency.keys())[0]]
        right = makeUnit(frequency[list(frequency.keys())[0]], list(frequency.keys())[0], 0)
        dictResult[right] = list(frequency.keys())[0]
        del frequency[list(frequency.keys())[0]]

        resultUnit = Node(left.getWeight()+right.getWeight(), left, right,1)













main("aa aaabb ff fh")
