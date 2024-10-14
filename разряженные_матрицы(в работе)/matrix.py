
#Класс матрицы
class Matrix:
     def __init__(self, nameFileWithMatrix = ""):
         self.nameFile = nameFileWithMatrix
         self.an = []
         self.nr = []
         self.nc = []
         self.jr = []
         self.jc = []
         self.d = []
         self.method = ""
         self.unpackingMatrix = [[]]


         path = "matrix/" + nameFileWithMatrix

         if nameFileWithMatrix != "":
             self.matrix = self.readMatrix(path)
         else:
             self.matrix = [[]]

         try:
            self.row = len(self.matrix)
            self.column = len(self.matrix[0])
         except IndexError:
            print("Матрица в файле %s пустая. Не подлежит упоковки." % self.nameFile)



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

     def transpose(self):
         self.matrix = [list(row) for row in zip(*self.matrix)]
         buf = self.row
         self.row = self.column
         self.column = buf

def summMatrix(matrix1, matrix2):
    matrixResult = []
    res = Matrix()

    row = matrix1.row
    col = matrix1.column

    for i in range(row):
        bufMatrix =[]
        for j in range(col):
            bufMatrix.append(matrix1.matrix[i][j] + matrix2.matrix[i][j])
        matrixResult.append(bufMatrix)
    res.matrix = matrixResult
    return res




