inp = input().split(" ")
n = int(inp[0])
k = int(inp[1])
r = range(1, min(n, k) + 1)
count = 0

if 1 <= n <= 10 ** 5 and 1 <= k <= 10 ** 9:
    matrix = (i * j for i in r for j in r)
    for i in matrix:
        if i == k:
            count += 1
print(count)
