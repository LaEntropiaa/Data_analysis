from Matrix import Matrix

matriz1 = Matrix(int, 5, 3)
matriz2 = Matrix(int, 3, 3)

matriz1.fill(2)
matriz2.fill(3)

matriz1 = matriz1 * matriz2

print(matriz1.matrix[4])