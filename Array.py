class Array:
    def __init__(self, dtype:type, size:int = 0, data:list = None) -> None:
        self.size:int = size
        self.dtype:type = dtype
        self.items = []
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

    def append(self, data) -> None:
        """
        Appends a new value to the array if posible.
        """
        if not self.__is_valid_type(data):
            raise TypeError("Data given is not of a valid type")
        if len(self.items) >= self.size():
            raise RuntimeError("Size of the array is unsufficient")
        self.items.append(data)

    def __is_valid_type(self, data) -> bool:
        if isinstance(data, self.dtype):
            return True
        return False