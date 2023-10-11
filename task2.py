# Розмір масиву
rows = 7
cols = 7

# Ініціалізація пустого масиву
array = [[0 for _ in range(cols)] for _ in range(rows)]

# Заповнення масиву згідно з варіантом
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == 6 or j == 0 or j == 6:
            array[i][j] = 1
        else:
            array[i][j] = 0

# Виведення масиву на екран
for i in range(rows):
    for j in range(cols):
        print(array[i][j], end=' ')
    print()
