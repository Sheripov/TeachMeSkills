inp = "6 12".split(" ")
n = int(inp[0])
k = int(inp[1])


def mult(n, k):
    r = [i for i in range(1, min(n, k))]
    print(r)
    count = 0
    if 1 <= n <= 100000 and 1 <= k <= 1000000000:
        # matrix = (i * j for i in r for j in r)
        # matrix.sort()
        for i in r:
            if i > k:
                break
            for j in r:
                if j > k:
                    break
                if i * j == k:
                    count += 1
    return count


mult(n, k)
