
#Класс матрицы
class Matrix :
     def __init__(self, nameFileWithMatrix = ""):
         self.an = []
         self.d = []
         self.method = ""
         self.unpackingMatrix = [[]]


         path = "matrix/1part/" + nameFileWithMatrix

         if nameFileWithMatrix != "":
             self.matrix = self.readMatrix(path)
         else:
             self.matrix = [[]]

         self.row = len(self.matrix)
         self.column = len(self.matrix[0])


     def readMatrix(self, nameFile):
         with open(nameFile, "r") as file:
             matrix = [list(map(int, line.split())) for line in file]
         return matrix


     def printMatrix(self):
         for i in range(len(self.matrix)):
             for j in range(len(self.matrix[0])):
                 print(self.matrix[i][j], end="\t")
             print("")

     def printMatrixunpacking(self):
         for i in range(self.row):
             for j in range(self.column):
                 print(self.unpackingMatrix[i][j], end="\t")
             print("")

def summMatrix(matrix1, matrix2):
    matrixResult = []

    for i in range(len(matrix1)):
        bufMatrix =[]
        for j in range(len(matrix1[0])):
            bufMatrix.append(matrix1[i][j] + matrix2[i][j])
        matrixResult.append(bufMatrix)
    return matrixResult



