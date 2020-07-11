# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1
while True:
    input_num = input('\nВведите текс через пробел:\n')
    if input_num == 'exit':
        break
    source_list = input_num.split(" ")
    output_list = []
    # i = 0
    # l = len(source_list)
    # while i < l:
    #     output_list.append(source_list[i])
    #     i += 1
    for i in source_list:
        output_list.append(i)
    output_list.pop(0)
    output_list.append(source_list[0])
    print(f'Исходный список: {source_list}')
    print(f'Конечный список: {output_list}')
