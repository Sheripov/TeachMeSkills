# Дан список целых чисел. Подсчитать сколько четных чисел в списке
while True:
    input_num = input('\nВведите целые числа через пробел:\n')
    if input_num == 'exit':
        break
    source_list = input_num.split(" ")
    try:
        print(f'Исходный список: {source_list}')
        count = 0
        choose = input('Выберите цикл: 1 - For, 2 - While\n')
        if choose == '1':
            len1 = len(source_list)
            i = 0
            while i < len1:
                if int(i) % 2 == 0:
                    count += 1
                i += 1
        elif choose == '2':
            for i in source_list:
                if int(i) % 2 == 0:
                    count += 1
        else:
            print('Введен неправильный номер')
        print(f'Количество чётных чисел в списке: {count}')
    except ValueError:
        print("Введите только целые числа через пробел!")
