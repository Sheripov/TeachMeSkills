from random import randint

def gen():
    while True:
        yield randint(0, 10)

my_gen = gen()

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))