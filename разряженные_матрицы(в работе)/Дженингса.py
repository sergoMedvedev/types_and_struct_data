
from Matrix import Matrix
from InterfaceForMatrix import InterfaceForMatrix

class Дженингс(Matrix, InterfaceForMatrix):

    def __init__(self, nameFile: str):
        self.matrix = Matrix.readMatrix(namefile=nameFile)
        print(self.matrix)


    def packing(self):
        pass
