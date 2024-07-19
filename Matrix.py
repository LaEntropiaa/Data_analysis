from Array import Array as arr

class Matrix:
    def __init__(self, dtype:type, rows:int = 1, columns:int = 1) -> None:
        self.matrix = arr(arr, rows)
        self.dtype = dtype 
        for i in range(rows):
            self.matrix[i] = arr(dtype, columns)

    def shape(self) -> tuple:
        """
        Returns the size of the matrix as a tuple
        """
        return (len(self.matrix), len(self.matrix[0]) )
    
    def set_item(self, value, row:int, column:int) -> None:
        """
        Sets the value of a certain item
        """
        if not self.__is_valid_type(value):
            raise TypeError("The value given is not of the correct type")
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
        return self.matrix[row].to_list()

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

    def longest_str_size(self) -> int:
        """
        Returns the string size of the value with the longest string
        """
        highest_values = []
        for i in self.matrix:
            highest_values.append(i.longest_str_size())
        num:int = highest_values[0]
        for i in highest_values:
            if i > num:
                num = i
        return num
    
    def fill(self, value) -> None:
        """
        Fills the whole matrix with certain value
        """
        if not self.__is_valid_type(value):
            raise TypeError("The value given is not of the correct type")
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
        for i in range(self.shape()[0] + 1):
            row = self.get_row(i)
            for k in row:
                space = " " * (len(str(k)) - minimal_space + 4)
                string = f"{string}{k}{space}"
            string = f"{string}\n"
        return string

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ValueError(
                "Matrix does not support adding 2 different size matrix"
                )
        new_matrix = Matrix(self.dtype, self.shape()[0], self.shape()[1])
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
        new_matrix = Matrix(self.dtype, self.shape()[0], self.shape()[1])
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
        new_matrix = Matrix(self.dtype, self.shape()[0], other.shape()[1])
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

