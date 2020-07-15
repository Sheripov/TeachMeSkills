# Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
# элемент и поменять его местами с элементом главной диагонали.
matrix = [[4, 2, 8, 4], [87, 62, 3, 8], [91, 151, 111, 12], [113, 141, 115, 1116]]
print(matrix)
for i, value in enumerate(matrix):
    tmp = matrix[i][i]
    tmp_max = value.index(max(value))
    matrix[i][i] = max(value)
    matrix[i][tmp_max] = tmp

print(matrix)

