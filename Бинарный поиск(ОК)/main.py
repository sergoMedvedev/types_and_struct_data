# входной массив
array = [1, 5, 7, 9, 15, 24, 34, 56, 78, 80, 90, 91]
number = 1


class Binar:
    def __init__(self, array = None, number = None):
        self.array = array
        self.number = number
        self.result = 0
        self.search(self.array,self.number)


    def search(self,array, number):
        try:
            if array == None:
                self.result = False
                return
            elif number == None:
                self.result = None
                return
            len_array = int(len(array) / 2)
            firstArray = array[0: len_array]
            secondArray = array[len_array:]


            if firstArray[-1] > number:
                self.search(firstArray, number)
            elif secondArray[0] < number:
                self.search(secondArray, number)
            elif firstArray[-1] == number or secondArray[0] == number:
                if firstArray[-1] == number:
                    self.result = firstArray[-1]
                else:
                    self.result = secondArray[0]

        except IndexError:
            self.result = None

# на анализе алгоритмов можно будет сравнить этот бинарный поиск с нерекурсивным (есть такая лаба)

def testBinarPoisk(array = None, number = None):
    test = Binar(array, number)
    if test.result == number or test.result == None:
        print("Test OK")
    elif test.result == False:
        print("массив или число не задано. Test OK")
    else:
        print("Test NO")

testBinarPoisk([-3,1,2,3,4,8,12,14], 100)
testBinarPoisk([-3,1,2,3,4,8,12,14], 12)
testBinarPoisk([-3,1,2,3,4,8,12,14])
testBinarPoisk(100)
testBinarPoisk([-3], -3)
testBinarPoisk([2,4,6,8,10,12,14,16,18,20,22,24,26,28], 18)


