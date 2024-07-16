from Array import Array as arr

class Matrix:
    def __init__(self, dtype:type, rows:int = 1, columns:int = 1) -> None:
        self.matrix = arr(arr, rows)
        for i in range(rows):
            self.matrix[i] = arr(dtype, columns)

    def shape(self) -> tuple:
        """
        Returns the size of the matrix as a tuple
        """
        return (len(self.matrix), len(self.matrix[1]))

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
        for i in range(self.matrix.size):
            for k in range(self.matrix[i].size):
                space = " " * (len(str(self.matrix[i][k])) - minimal_space + 4)
                string = f"{string}{self.matrix[i][k]}{space}"
            string = f"{string}\n"
        return string

        

    
