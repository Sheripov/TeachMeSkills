# Введите число. Если это число делиться на 1000 без остатка, то выведите на
# экран "millennium"
while True:
    str_input = input('Введите число("exit" для выхода): ')
    if str_input == 'exit':
        exit()
    else:
        if str_input.isdigit():
            user_in = int(str_input)
            if user_in % 1000 == 0:
                print('millennium')
            else:
                print('Введенная цифра не кратно 1000')
        else:
            print('Ошибка ввода. Введите только цифры')
