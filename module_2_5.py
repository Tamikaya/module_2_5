def get_matrix(n, m, value):
    matrix = []  # Создайте пустой список

    for i in range(n):  # Диапазон перебераемый для n (кол-во строк)
        matrix.append([])  # Добавили пустой список в список matrix
        for j in range(m):  # Диапазон перебераемый для m (кол-во столбцов)
            matrix[i].append(value)  # Пополнить пустой список matrix.append([])значением value

    return matrix  # Вернуть значение matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)





