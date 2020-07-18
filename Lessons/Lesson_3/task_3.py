import random
n = 6
m = 3
g = []
t = 0
# список в списке называется матрица или двумерный массив
for i in range(0, n):
    n = []
    for j in range(0, m):
        c = random.randint(1, 9)
        n.append(c)
        if c == 7:
            t += 1
    g.append(n)
for i in g:
    print(i)
print(t)
