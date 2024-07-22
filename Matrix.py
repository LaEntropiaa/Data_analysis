from Array import Array as arr

class Matrix:
    def __init__(self, rows:int = 1, columns:int = 1) -> None:
        self.matrix = []
        for i in range(rows):
            temp = []
            for k in range(columns):
                temp.append(0)
            self.matrix.append(temp)

    def shape(self) -> tuple:
        """
        Returns the size of the matrix as a tuple
        """
        return (len(self.matrix), len(self.matrix[0]) )
    
    def set_item(self, value, row:int, column:int) -> None:
        """
        Sets the value of a certain item
        """
        try:
            self.matrix[row][column] = value
        except IndexError:
            raise IndexError("Row or column is out of matrix range")
        
    def get_item(self, row:int, column:int):
        """
        Returns the value at the given index
        """
        try:
            return self.matrix[row][column]
        except IndexError:
            raise IndexError("Row or column is out of matrix range")
        
    def get_row(self, row:int) -> list:
        """
        Returns the row a a list
        """
        if row > self.shape()[0] - 1:
            raise IndexError("Column index out of range")
        return self.matrix[row]

    def get_column(self, column:int) -> list:
        """
        Returns the column as a list
        """
        if column > self.shape()[1] - 1:
            raise IndexError("Row index out of range")
        row_list = []
        for i in self.matrix:
            row_list.append(i[column])
        return row_list

    def get_transpose(self):
        """
        Returns a diagonaly fliped version of the matrix
        """
        new_matrix = Matrix(self.shape()[1], self.shape()[0])
        keys = [
            (i, k) 
            for i in range(self.shape()[0]) 
            for k in range(self.shape()[1])
            ]
        for i, k in keys:
            new_matrix.set_item(self.get_item(i, k), k, i)
        return new_matrix
    
    def get_minor(self, row:int, column:int):
        """
        Returns the minor of a given value
        """
        new_matrix = Matrix(self.shape()[0] - 1, self.shape()[1] - 1)
        self_values = []
        other_keys = [
            (i, k) 
            for i in range(new_matrix.shape()[0]) 
            for k in range(new_matrix.shape()[1])
            ]
        for i in range(self.shape()[0]):
            for k in range(self.shape()[1]):
                if i == row or k == column:
                    continue
                self_values.append(self.get_item(i, k))
        value_count = 0
        for i, k in other_keys:
            new_matrix.set_item(self_values[value_count], i, k)
            value_count += 1
        return new_matrix

    def get_2x2_determinant(self) -> int:
        if self.shape()[0] != 2 and self.shape()[1]:
            raise ValueError("Matrix dimentions are wrong")
        return (self.get_item(0, 0) * self.get_item(1, 1)) - (self.get_item(0,1) * self.get_item(1, 0))
        
    def get_3x3_determinant(self) -> int:
        if self.shape()[0] != 3 and self.shape()[1]:
            raise ValueError("Matrix dimentions are wrong")
        a = self.get_item(0, 0) * ((self.get_item(1, 1) * self.get_item(2, 2)) - (self.get_item(1, 2) * self.get_item(2, 1)))
        b = self.get_item(0, 1) * ((self.get_item(1, 0) * self.get_item(2, 2)) - (self.get_item(1, 2) * self.get_item(2, 0)))
        c = self.get_item(0, 2) * ((self.get_item(1, 0) * self.get_item(2, 1)) - (self.get_item(1, 1) * self.get_item(2, 0)))
        return a - b + c

    def get_nxn_determinant(self) -> int:
        """
        Returns the determinant of a square
        """
        value = 0
        if self.shape()[0] != self.shape()[1]:
            raise ValueError("Matrix has to be squared")
        if self.shape()[0] == 1:
            return self.get_item(0, 0)
        if self.shape()[0] == 2:
            return self.get_2x2_determinant()
        if self.shape()[0] == 3:
            return self.get_3x3_determinant()
        for i in range(len(self.get_row(0))):
            if (2 + i) % 2 == 0:
                determinant_sign = 1
            else:
                determinant_sign = -1
            value += self.get_item(0, i) * (determinant_sign * self.get_minor(0, i).get_nxn_determinant())
        return value
        

    def get_adjoint(self):
        """
        Return the adjoint of the matrix as a Matrix
        """
        new_matrix = Matrix(self.shape()[0], self.shape()[1])
        keys = [
            (i, k)
            for i in range(self.shape()[0])
            for k in range(self.shape()[1])
        ]
        for i, k in keys:
            if (i + k + 2) % 2 == 0:
                sign = 1
            else:
                sign = -1
            value = sign * self.get_minor(i, k).get_nxn_determinant()
            new_matrix.set_item(value, i, k)
        return new_matrix
    
    def get_inverse(self):
        """
        Return the inverse of the matrix as a Matrix
        """
        new_matrix = self.get_adjoint().get_transpose()
        keys = [
            (i, k)
            for i in range(self.shape()[0])
            for k in range(self.shape()[1])
        ]
        for i, k in keys:
            value = new_matrix.get_item(i, k) / self.get_nxn_determinant()
            new_matrix.set_item(value, i, k)
        return new_matrix

    def longest_str_size(self) -> int:
        """
        Returns the string size of the value with the longest string
        """
        highest_value = []
        for i in self.matrix:
            temp = []
            for k in i:
                temp.append(len(str(k)))
            highest_value.append(max(temp))
        return max(highest_value)
    
    def fill(self, value) -> None:
        """
        Fills the whole matrix with certain value
        """
        keys = [
            (i, k) 
            for i in range(self.shape()[0]) 
            for k in range(self.shape()[1])
            ]
        for i, k in keys:
            self.set_item(value, i, k)
    
    def __is_valid_type(self, value) -> bool:
        if isinstance(value, self.dtype):
            return True
        return False
    
    def __repr__(self) -> str:
        string = "Matrix: ["
        for column in range(self.matrix.size):
            # to avoid putting a coma at the end
            if column == self.matrix.size - 1:
                string = f"{string}{str(self.matrix[column])}"
                continue
            string = f"{string}{str(self.matrix[column])},"
        string = string + "]"
        return string
    
    def __str__(self) -> str:
        #the space designated for every shown value 
        # (makes every value take the same space)
        minimal_space:int = self.longest_str_size()
        string = ""
        for i in range(self.shape()[0]):
            row = self.get_row(i)
            for value in row:
                space = " " * (minimal_space - (len(str(value))) + 4)
                string = f"{string}{value}{space}"
            string = f"{string}\n"
        return string 

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ValueError(
                "Matrix does not support adding 2 different size matrix"
                )
        new_matrix = Matrix(self.shape()[0], self.shape()[1])
        keys = [
            (i, k) 
            for i in range(self.shape()[0]) 
            for k in range(self.shape()[1])
            ]
        for i, k in keys:
            if self.get_item(i, k) == None or other.get_item(i, k) == None:
                continue
            # Sorry for the indentation
            try:
                value = self.get_item(i, k) + other.get_item(i, k)
                new_matrix.set_item(value, i, k)
            except TypeError:
                raise TypeError(
                    "The data type in the matrix does not support addition"
                )
        return new_matrix
    
    def __sub__(self, other):
        if self.shape() != other.shape():
            raise ValueError(
                "Matrix does not support substracting 2 different size matrix"
            )
        new_matrix = Matrix(self.shape()[0], self.shape()[1])
        keys = [
            (i, k) 
            for i in range(self.shape()[0]) 
            for k in range(self.shape()[1])
            ]
        for i, k in keys:
            if self.get_item(i, k) == None or other.get_item(i, k) == None:
                continue
            try:
                value = self.get_item(i, k) - other.get_item(i, k)
                new_matrix.set_item(value, i, k)
            except TypeError:
                raise TypeError(
                    "The data type in the matrix does not support substraction"
                    )
        return new_matrix
    
    def __mul__(self, other):
        if self.shape()[1] != other.shape()[0]:
            raise ValueError(
                "Columns of matrix A are different from rows of matrix B"
            )
        new_matrix = Matrix(self.shape()[0], other.shape()[1])
        keys = [
            (i, k)
            for i in range(self.shape()[0])
            for k in range(other.shape()[1])
        ]
        for i, k in keys:
            row = self.get_row(i)
            column = other.get_column(k)
            value = sum(a * b for a, b in zip(row, column))
            new_matrix.set_item(value, i, k)
        return new_matrix

