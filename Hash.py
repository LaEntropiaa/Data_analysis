import math

class Hash:
    __C = 1 / (1 + math.sqrt(5) / 2)
    def __init__(self, size:int):
        self.size = size
        self.array = [None for _ in range(self.size)]
        self.items = 0
        
        