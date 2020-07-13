import random
b = 6
g = []
# список в списке называется матрица или двумерный массив
for i in range(0, b):
    n = []
    for j in range(1, b):
        c = random.randint(1, 9)
        n.append(c)
    g.append(n)
for i in g:
    print(i)



