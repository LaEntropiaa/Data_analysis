class Array:
    def __init__(self, dtype:type, size:int = 1, data:list = None) -> None:
        self.size:int = size
        self.dtype:type = dtype
        self.items = []
        #Fill the list with None's so there is no conflict with the insert or other methods like that
        for i in range(size):
            self.items.append(None)
        if not isinstance(self.dtype, type):
            raise ValueError("The data type given needs to be of type 'type'")
        if data is None:
            return
        if len(data) > self.size:
            raise ValueError("The list given was too large!")
        for i in data:
            if not self.__is_valid_type(i):
                raise ValueError("Items in the list given are not of the correct type")
            self.items.append(i)

    def append(self, value) -> None:
        """
        Appends a new value to the array if posible.
        """
        if not self.__is_valid_type(value):
            raise TypeError("Value given is not of a valid type")
        if len(self.items) >= self.size():
            raise RuntimeError("Size of the array is unsufficient")
        for i in range(self.size, 0, -1):
            if self.items[i] is not None:
                self.items[i + 1] = value
                return
        self.items[0] = value
        

    def insert(self, value, index:int) -> None:
        """
        Inserts a value at the given position
        """
        if not self.__is_valid_type(value):
            raise TypeError("Value given is not of a valid type")
        if index > self.size - 1:
            raise IndexError("Index given is out of range")
        self.items[index] = value

    def pop(self) :
        """
        Deletes the last value and returns it
        """
        for i in range(self.size - 1, 0, -1):
            if self.items[i] is not None:
                temporal = self.items[i]
                self.items[i] = None
                return temporal
        return None

    def remove(self, index:int) -> None:
        """
        Removes the item at the given index
        """ 
        if index > self.size - 1:
            raise IndexError("Index given is out of range")
        self.items[index] = None

    def index(self, value) -> int:
        """
        Takes a value and returns the first index where it finds it.
        Returns -1 if it's not in the array
        """
        if not self.__is_valid_type(value):
            raise TypeError("Value given is not of a valid type")
        for i in range(self.size - 1):
            if self.items[i] == value:
                return i
        return -1
    
    def get(self, index:int):
        """
        Returns the value at the given index
        """
        if index > self.size - 1:
            raise IndexError("Index given is out of range")
        return self.items[index]
    
    def count(self, value) -> int:
        """
        Returns the number of ocurrences of a given value
        """
        if not self.__is_valid_type(value):
            raise TypeError("Value given i not of  a valid type")
        count = 0
        for i in range(self.size - 1):
            if self.items[i] == value:
                count += 1
        return count

    def reverse(self) -> None:
        """
        Reverses the order of the array
        """
        self.items.reverse()

    def __is_valid_type(self, data) -> bool:
        if isinstance(data, self.dtype):
            return True
        return False
    
    def __len__(self):
        count = 0
        for i in self.items:
            if i is not None:
                count = count + 1
        return count
    
    def __str__(self):
        return str(self.items)
    
    def __getitem__(self, index):
        if index > self.size - 1:
            raise IndexError("Index given is out of range")
        return self.items[index]
    
    def __setitem__(self, index, value):
        if not self.__is_valid_type(value):
            raise TypeError("Value given is not of a valid type")
        if index > self.size - 1:
            raise IndexError("Index given is out of range")
        self.items[index] = value
    
    def __delitem__(self, index):
        if index > self.size - 1:
            raise IndexError("Index given is out of range")
        self.items[index] = None
    
    def __iter__(self):
        return self.items