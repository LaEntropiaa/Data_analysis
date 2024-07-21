from Matrix import Matrix

matriz1 = Matrix(int, 4, 4)

matriz1.set_item(1, 0, 0)
matriz1.set_item(3, 0, 1)
matriz1.set_item(5, 0, 2)
matriz1.set_item(9, 0, 3)

matriz1.set_item(1, 1, 0)
matriz1.set_item(3, 1, 1)
matriz1.set_item(1, 1, 2)
matriz1.set_item(7, 1, 3)

matriz1.set_item(4, 2, 0)
matriz1.set_item(3, 2, 1)
matriz1.set_item(9, 2, 2)
matriz1.set_item(7, 2, 3)

matriz1.set_item(5, 3, 0)
matriz1.set_item(2, 3, 1)
matriz1.set_item(0, 3, 2)
matriz1.set_item(9, 3, 3)



print(matriz1.get_nxn_determinant())