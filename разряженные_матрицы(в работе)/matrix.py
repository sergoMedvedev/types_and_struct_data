
#Класс матрицы
class Matrix :
     def __init__(self, nameFileWithMatrix):
         self.an = []
         self.d = []
         self.method = ""

         path = "matrix/1part/" + nameFileWithMatrix

         self.matrix = self.readMatrix(path)


     def readMatrix(self, nameFile):
         pass

