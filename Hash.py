

class Hash:
    def __init__(self, size:int):
        self.__C = 1 / 1.618033988749895
        self.__items = 0
        self.array = []
        for i in range(size):
            self.array.append(None)

    def __hash(self, key:str) -> int:
        K = hash(key)
        location = round(len(self.array)(K * self.__C % 1))
        return location
    
    def __assign(self, hash_val:int, data) -> None:
        if self.__items >= len(self.array):
            raise IndexError("Hash table is out of capacity!")
        while self.array[hash_val] is not None :
            hash_val = hash(hash_val)
            hash_val = self.__hash(hash_val)
        self.array[hash_val] = data

    def __len__(self) -> int:
        return len(self.array)
    
    def add(self, data, key) -> None:
        self.__assign(self.__hash(key), (data, key))
    
    def get(self, key):
        key = self.__hash(key)
        if 