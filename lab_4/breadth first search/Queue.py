
class Queue:

    def __init__(self):
        self.arrary =[]


    def add(self, number):
        self.arrary.append(number)

    def get(self):
        if len(self.arrary) == 0:
            return None
        else:
            number = self.arrary[0]
            self.arrary.pop(0)
            return number

    def check(self):
        return self.arrary[0]
