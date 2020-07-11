# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()
dic = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
choose = input('Выберите цикл: 1 - For, 2 - While\n')
if choose == '1':
    for i in list(dic.keys()):
        print(f'{i}: {dic[i]} -> {i}{len(i)}: {dic[i]}')
        dic[f'{i}{len(i)}'] = dic.pop(i)
elif choose == '2':
    l = list(dic.keys())
    len1 = len(l)
    i = 0
    while i < len1:
        print(f'{l[i]}: {dic[l[i]]} -> {l[i]}{len(l[i])}: {dic[l[i]]}')
        dic[f'{l[i]}{len(l[i])}'] = dic.pop(l[i])
        i += 1
else:
    print('Введен неправильный номер')
print(dic)
