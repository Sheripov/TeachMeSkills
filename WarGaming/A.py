from collections import Counter

inp = tuple(input().split(" "))

table_size = int(inp[0])
number_to_find = int(inp[1])


def get_simple_divisors(n):
    result = []
    i = 2
    while i < n:
        if n % i == 0:
            n /= i
            result.append(i)
        else:
            i += 1
    result.append(int(n))
    return result


ls = get_simple_divisors(number_to_find)
kkk = Counter(ls).items()
d = [k for k, _ in kkk]
m = [v for _, v in kkk]
k = [0 for _ in range(len(set(ls)))]
ln = range(len(m))
divisors = set()
try:
    while True:
        r = 1
        for i1, i2 in zip(d, k):
            r *= i1 ** i2
        divisors.add(r)

        k[0] += 1
        for i in ln:
            if k[i] > m[i]:
                k[i] = 0
                k[i + 1] += 1  # IndexError
except IndexError:
    pass

divisors = {d for d in divisors if
            d <= table_size and number_to_find / d <= table_size}
print(len(divisors))
