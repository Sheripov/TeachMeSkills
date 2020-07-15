# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.
mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
max_num = max(mlist)
for index, value in enumerate(mlist):
    if value % 2 == 0:
        mlist[index] = max_num
print(mlist)

