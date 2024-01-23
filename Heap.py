class MinHeap:
    def __init__(self, data=None):
        self.heap = []
        if data is not None:
            for node in data:
                self.append(node)

    def append(self, data:int):
        """
        adds a new value and then hepifies it
        """
        self.heap.append(data)
        self.__hepify()
    
    def __hepify(self):
        """
        Compares the new value with its parent changing its position if needed
        """
        index = len(self.heap) - 1
        if index < 1:
            return 
        if index % 2 > 0:
            parent = round((index-1) / 2)
        else:
            parent = int((index-2) / 2)
        while self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            if index < 1:
                return
            if parent % 2 > 0:
                parent = round((index-1) / 2)
            else:
                parent = int((index-2) / 2)
    
    def __str__(self):
        string = f"{self.heap[0]}\n"
        level = 1
        nodes = 0
        for index in range(1,len(self.heap), 2):
            try:
                string = f"{string}{self.heap[index], self.heap[index+1]}|"
                nodes += 2
            except IndexError:
                string = f"{string}{self.heap[index]}|"
                return string
            if 2**level >= nodes:
                level += 1
                string = f"{string}\n"
            if index + 2 >= len(self.heap):
                return string

            