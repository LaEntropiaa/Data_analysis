from Matrix import Matrix

matriz1 = Matrix(3, 3)

matriz1.set_item(2, 0, 0)
matriz1.set_item(1, 0, 1)
matriz1.set_item(0, 0, 2)

matriz1.set_item(1, 1, 0)
matriz1.set_item(-1, 1, 1)
matriz1.set_item(1, 1, 2)

matriz1.set_item(0, 2, 0)
matriz1.set_item(2, 2, 1)
matriz1.set_item(-1, 2, 2)

print(matriz1)
print()
print(matriz1.get_inverse() * matriz1)