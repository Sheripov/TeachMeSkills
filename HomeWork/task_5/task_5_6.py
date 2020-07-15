# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего).
mlist = [1, 2, 3, 4, 5, 6, 1, 8, 9, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19]
count = 1
count_rising = 0
size = len(mlist)
for i in range(count-1, size):
    tmp =[i, 0]
    for j in range(count-1, size):
        try:
            if mlist[j] < mlist[j+1]:
                pass
            else:
                count_rising += 1
            count += 1
        except IndexError:
            count += 1
            count_rising += 1
print(count_rising)



