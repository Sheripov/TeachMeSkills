# Дан список целых чисел. Подсчитать сколько четных чисел в списке
while True:
    input_num = input('\nВведите целые числа через пробел:\n')
    if input_num == 'exit':
        break
    source_list = input_num.split(" ")
    try:
        print(f'Исходный список: {source_list}')
        count = 0
        # len1 = len(source_list)
        # i = 0
        # while i < len1:
        #     if int(i) % 2 == 0:
        #         count += 1
        #         i += 1
        for i in source_list:
            if int(i) % 2 == 0:
                count += 1
        print(f'Количество чётных чисел в списке: {count}')
    except ValueError:
        print("Введите только целые числа через пробел!")
