# Составить список чисел Фибоначчи содержащий 15 элементов.
class Fibonacci:
    def __init__(self, input_num):
        if not input_num.isdigit():
            print('Вводите только целые числа')
            quit()
        self.n = int(input_num)
        if self.n < 2:
            print('Ряд Фибоначчи должен быть больше 1')
            quit()

    def for_realisation(self):
        print('Реализация в цикле For in')
        fib1 = 1
        fib2 = 1
        fib_list = [1, 1]
        for i in range(2, self.n):
            fib1, fib2 = fib2, fib1 + fib2
            fib_list.append(fib2)
        return fib_list

    def while_realisation(self):
        print('Реализация в цикле For in')
        fib1 = fib2 = 1
        fib_list = [1, 1]
        while self.n > 2:
            fib1, fib2 = fib2, fib1 + fib2
            fib_list.append(fib2)
            self.n -= 1
        return fib_list

    def switch_case(self, inpt):
        if inpt == '1':
            print(self.for_realisation())
        elif inpt == '2':
            print(self.while_realisation())
        else:
            print('Введите 1 или 2')


while True:
    fib_num = input('\nВведите количество элементов в списке: ')
    choose = input('Введите:\n'
                   '"1" для реализации в цикле For in\n'
                   '"2" для реализации в цикле While\n'
                   '"3" для выхода\n')
    if choose == '3':
        break
    fibonacci = Fibonacci(fib_num)
    fibonacci.switch_case(choose)
