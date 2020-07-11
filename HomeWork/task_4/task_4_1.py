# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2
while True:
    input_num = input('\nВведите целые числа через пробел:\n')
    if input_num == 'exit':
        break
    source_list = input_num.split(" ")
    try:
        print(f'Исходный список: {source_list}')
        output_list = []
        choose = input('Выберите цикл: 1 - For, 2 - While\n')
        if choose == '2':
            len1 = len(source_list)
            i = 0
            while i < len1:
                output_list.append(int(source_list[i]) * -2)
                i += 1
        elif choose == '1':
            for i in source_list:
                output_list.append(int(i) * -2)
        else:
            print('Введен неправильный номер')
        print(f'Конечный список: {output_list}')
    except ValueError:
        print("Введите только целые числа через пробел!")


