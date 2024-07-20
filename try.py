from Matrix import Matrix

matriz1 = Matrix(int, 3, 3)

matriz1.set_item(1, 0, 0)
matriz1.set_item(2, 0, 1)
matriz1.set_item(3, 0, 2)
matriz1.set_item(10, 1, 0)
matriz1.set_item(6, 1, 1)
matriz1.set_item(5, 1, 2)
matriz1.set_item(4, 2, 0)
matriz1.set_item(60, 2, 1)
matriz1.set_item(10, 2, 2)

print(matriz1.get_3x3_determinant())