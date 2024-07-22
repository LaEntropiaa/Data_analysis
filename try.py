from Matrix import Matrix

matriz1 = Matrix(4, 4)

matriz1.set_item(4, 0, 0)
matriz1.set_item(5, 0, 1)
matriz1.set_item(1, 0, 2)
matriz1.set_item(2, 0, 3)

matriz1.set_item(1, 1, 0)
matriz1.set_item(3, 1, 1)
matriz1.set_item(9, 1, 2)
matriz1.set_item(9, 1, 3)

matriz1.set_item(6, 2, 0)
matriz1.set_item(7, 2, 1)
matriz1.set_item(0, 2, 2)
matriz1.set_item(2, 2, 3)

matriz1.set_item(4, 3, 0)
matriz1.set_item(4, 3, 1)
matriz1.set_item(3, 3 ,2)
matriz1.set_item(6, 3, 3)

print(matriz1.get_nxn_determinant())