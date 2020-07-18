# for i, elem in enumerate(['a','b','c','d']):
#     print(f'{i} - {elem}')
import random
n = 6
m = 3
g = []
t = 0
# список в списке называется матрица или двумерный массив
for i in range(0, n):
    n1 = []
    for j in range(0, m):
        c = random.randint(1, 9)
        n1.append(c)
        t += c
    g.append(n1)
for i in g:
    print(i)
print(t)
t1 = t / (n * m)
print(t1)
count = 0
for i, en in enumerate(g):
    for j, eng in enumerate(en):
        avg2 = j + i
        if eng > t1 and avg2:
            count += 1

print(count)
