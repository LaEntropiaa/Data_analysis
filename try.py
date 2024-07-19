from Matrix import Matrix

matriz1 = Matrix(int, 5, 3)
matriz2 = Matrix(int, 3, 3)

matriz1.fill(2)
matriz2.fill(3)

matriz1 = matriz1 * matriz2

matriz1.set_item(8, 2, 1)


print(matriz1.get_transpose())