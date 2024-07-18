from Matrix import Matrix

matriz1 = Matrix(int, 4, 2)
matriz2 = Matrix(int, 4, 2)

matriz1.set_item(8, 3, 1)
matriz2.set_item(12, 3, 1)

matriz1 = matriz1 - matriz2
print(matriz1)