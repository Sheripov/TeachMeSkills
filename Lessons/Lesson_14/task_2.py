from random import randint


def gen(a, b, diff):
    while True:
        yield randint(a, b)
        a, b = a + diff, b + diff


my_gen = gen(1, 10, 10)

for i in my_gen:
    print(i)
