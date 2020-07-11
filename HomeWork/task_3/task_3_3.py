# Ввести строку. Если длина строки больше 10 символов, то создать новую
# строку с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
# Если меньше 10, то вывести на экран второй символ строки
while True:
    str_input = input('Введите строку("exit" для выхода): ')
    if str_input == 'exit':
        exit()
    else:
        if len(str_input) > 10:
            new_str = f"{str_input}!!!"
            print(new_str)
        else:
            print(f'{str_input[1]}')
