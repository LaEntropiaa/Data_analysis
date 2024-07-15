import math

class Hash:
    __C = 1 / (1 + math.sqrt(5) / 2)
    def __init__(self, size:int, data:dict = None):
        self.size = size
        self.objects = 0
        self.array = [None for _ in range(self.size)]
        if data is not None:
            if self.size < len(data):
                self.size = len(data)
            for item in data.items():
                self.add(item[1], item[0])

    def __str__(self):
        string = "{"
        for i in self.array:
            if i is None:
                continue
            string = f"{string} {i[0]}:{i[1]},"
        string = f"{string[:-1]} {'}'}"
        return string
    
    def __setitem__(self, key, data):
        if self.objects >= self.size:
            raise KeyError("HashTable out of space")
        position = self.__hash(key)
        while self.array[position] is not None:
            if self.array[position][0] == key:
                self.array[position][1] = data
                return
            position = (position + 1) % self.size
        self.array[position] = (key, data)
        self.objects += 1

    def __getitem__(self, key):
        position = self.__hash(key)
        while self.array[position] is not None:
            if self.array[position][0] == key:
                return self.array[position][1]
            position = (position + 1) % self.size
        raise KeyError("Key not found")

    def __hash(self, key) -> int:
        key = hash(key)
        position = round(self.size * ((key * self.__C) % 1))
        return position        

    def add(self, data, key) -> None:
        if self.objects >= self.size:
            raise KeyError("HashTable out of space")
        position = self.__hash(key)
        while self.array[position] is not None:
            if self.array[position][0] == key:
                self.array[position][1] = data
                return
            position = (position + 1) % self.size
        self.array[position] = (key, data)
        self.objects += 1
    
    def get(self, key):
        position = self.__hash(key)
        while self.array[position] is not None:
            if self.array[position][0] == key:
                return self.array[position][1]
            position = (position + 1) % self.size
        raise KeyError("Key not found")

    def delete(self, key) -> None:
        position = self.__hash(key)
        while self.array[position] is not None and position < self.size:
            if self.array[position][0] == key:
                self.array[position] = None
                self.objects -= 1
                return
            position = (position + 1) % self.size
        raise KeyError("Key not found")

    def search_k(self, key) -> int:
        position = self.__hash(key)
        while self.array[position] is not None and position < self.size:
            if self.array[position][0] == key:
                return position
            position = (position + 1) % self.size
        return -1
    
    def search_v(self, data):
        position = 0
        while self.array[position] is not None and position < self.size:
            if self.array[position][1] == data:
                return position
            position += 1
        return -1
    
    def keys(self) -> list:
        keys = []
        for key in self.array:
            if key is not None:
                keys.append(key[0])
        return keys
    
    def values(self) -> list:
        values = []
        for value in self.array:
            if value is not None:
                values.append(value[1])
        return values

    def items(self) -> list:
        items = []         
        for item in self.array:
            if item is not None:
                items.append(item)
        return items
    
    def clear(self) -> None:
        self.array = []
        self.objects = 0

        