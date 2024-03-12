from function import dowloud_matrix
from Queue import Queue

array = []
'''
   1)приобразовать входной массив в двумерный массив и проверить там:
       - размерность строк и столбцов
   ц    - обработать ошибку открытия файла
'''

while True:
    print("Введите имя файла в корне прошграмма")
    #fileName = input()
    fileName = 'matrix.txt'
    boolen, array = dowloud_matrix(fileName)
    if type(boolen) == False:
        continue
    break
print(array)
print("Введите номер вершины от 0 до ", len(array))
vertex = int(input())
queue = Queue()
outList = []
outList.append(vertex)
cikl = vertex

while True:
    if (queue.arrary != [] and queue.check() in outList):
        _ =queue.get()
        continue
    else:
        for number_stolb in range(len(array)):
            if array[number_stolb][cikl] == 1:
                queue.add(number_stolb)
                print(queue.arrary)
                continue
            else:
                continue
        cikl = queue.get()
        if cikl in outList:
            continue
        else:
            outList.append(cikl)
            print("")
        if len(outList) == len(array):
            break

print(outList)








#
# from collections import deque
#
# def bfs(matrix, start):
#     visited = [False] * len(matrix)
#     queue = deque([start])
#     visited[start] = True
#
#     while queue:
#         node = queue.popleft()
#         print(node, end=" ")
#
#         for neighbor, connected in enumerate(matrix[node]):
#             if connected and not visited[neighbor]:
#                 queue.append(neighbor)
#                 visited[neighbor] = True
#
# # Пример матрицы смежности
# matrix = [
#     [0, 1, 1, 0, 0],
#     [1, 0, 0, 1, 0],
#     [1, 0, 0, 1, 1],
#     [0, 1, 1, 0, 1],
#     [0, 0, 1, 1, 0]
# ]
#
# test = [
#     [0,1,1,0,0,0],
#     [1,0,0,0,0,0],
#     [1,0,0,1,1,0],
#     [0,0,1,0,0,0],
#     [0,0,1,0,0,1],
#     [0,0,0,0,1,0]
# ]
#
# # Начать обход с вершины 0
# bfs(test, 2)
