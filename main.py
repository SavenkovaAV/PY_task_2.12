def find_size(matrix):  # находим размер для нового квадратного массива
    num_rows = len(matrix)  # Находим количество строк исходного массива
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    for row in matrix:  # Проходимся по каждой строке, чтобы найти минииальное количество столбцов
        num_cols = min(num_cols, len(row))
    return min(num_rows, num_cols)


with open("input.txt", "r") as inputFile:  # Открываем файл input.txt в режиме чтения
    newLst = []
    for line in inputFile:  # Читаем каждую строку файла и добавляем каждый элемент в список
        lst = line.split()
        row = [int(x) for x in lst]
        newLst.append(row)

result = []
size = find_size(newLst)
for i in range(size):  # Присваиваем новому массиву значения исходного так, чтобы получился квадрат
    row = []
    for j in range(size):
        row.append(newLst[i][j])
    result.append(row)

with open('output.txt', 'w') as outFile:  # Открываем файл output.txt в режиме записи
    for row in result:  # Записываем каждый элемент в файл в формате строки
        for item in row:
            outFile.write(str(item) + ' ')
        outFile.write('\n')
