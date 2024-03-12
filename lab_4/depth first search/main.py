from Tokin import Tokin
from Stack import  Stack

n = Tokin('N', None, None)
m = Tokin('M', n, None)
l = Tokin('L', None, None)
k = Tokin('K', None, None)
j = Tokin('J', None, None)
i = Tokin('I', None, None)
h = Tokin('H', None, None)
d = Tokin('D', h, i)
e = Tokin('E', j, None)
f = Tokin('F', None, k)
g = Tokin('G', l, m)
b = Tokin('B', d, e)
c = Tokin('C', f, g)
a = Tokin('A', b, c)

arrayTokin = [a,b,c,d,e,f,g,h,i,g,k,l,m,n]

print('Введите вершину (большую букву): ')
vertex = input()
stack = Stack()
tokenStart =Tokin
outList =[]
for i in arrayTokin:
    if i.element == vertex:
        tokenStart = i
# stack.push(tokenStart)
outList.append(tokenStart.element)
head = tokenStart
while True:
    if head.right != None and head.left != None:

        while ((head.left != None) or (head.right != None)):

            if head.left != None:
                stack.push(head.left)
            if head.right != None:
                stack.push(head.right)

            head = stack.pop()
            outList.append(head.element)
            print(outList)
            continue

    elif ((head.left != None) or (head.right != None)):
        while (head.left != None) or (head.right != None):

            if head.left != None:
                stack.push(head.left)
            if head.right != None:
                stack.push(head.right)

            head = stack.pop()
            outList.append(head.element)
            print(outList)
            continue



    elif stack.stack == []:
        break
    else:
        head = stack.pop()
        outList.append(head.element)
        continue

print(outList)






