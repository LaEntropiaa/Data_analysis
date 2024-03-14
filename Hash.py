import math

class Hash:
    __C = 1 / (1 + math.sqrt(5) / 2)
    def __init__(self, size:int):
        self.size = size
        self.array = [None for _ in range(self.size)]
        self.items = 0
        
    def __hash(self, key) -> int:
        key = hash(key)
        position = round(self.size * ((key * self.__C) % 1))
        return position        

    def add(self, data, key) -> None:
        if self.items >= self.size:
            raise KeyError("HashTable out of space")
        position = self.__hash(key)
        while self.array[position] is not None:
            if self.array[position][1] == key:
                self.array[position][0] = data
                return
            position = (position + 1) % self.size
        self.array[position] = (data, key)
    
    def get(self, key):
        position = self.__hash(key)
        while self.array[position] is not None:
            if self.array[position][1] == key:
                return self.array[position][0]
            position = (position + 1) % self.size
        raise KeyError("Key not found")
