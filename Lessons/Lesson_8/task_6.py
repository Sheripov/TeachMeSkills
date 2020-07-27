from functools import reduce
func1 = filter(
    lambda name: name % 3 == 0,
    [1, 2, 3, 4, 5, 6],
)

result = reduce(
    lambda a, x: a * x,
    func1
)
print(result)