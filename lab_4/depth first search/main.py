from Tokin import Tokin

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

print('Введите вершину: ', end='')
vertex = int(input())


