class MinHeap:
    def __init__(self, data=None):
        self.heap = []
        if data is not None:
            for node in data:
                self.append(node)

    def append(self, data=0):
        """
        Adds a new value and then adjusts the heap
        """
        self.heap.append(data)
        self.__sift_up()

    def push(self, data=0):
        """
        Replaces the min value and adjusts the heap
        """
        if len(self.heap) < 1:
            return 
        self.heap[0] = data
        self.__sift_down()

    def pop(self):
        """
        Deletes the head value an returns it
        """
        if len(self.heap) < 1:
            return 
        pop = self.heap[0]
        try:
            self.heap[0] = self.heap.pop()
            self.__sift_down()
            return pop
        except IndexError:
            return pop
    
    def replace(self, index:int, data=0):
        """
        Replaces the value at the given inde xand adjusts the heap
        """
        if len(self.heap) < 1:
            return 
        self.heap[index] = data
        self.__sift_down(index)
        self.__sift_up(index)

    def delete(self, index:int):
        """
        Replaces the value at the given index and adjusts the heap
        """
        if len(self.heap) < 1:
            return 
        self.heap[index] = self.heap.pop()
        self.__sift_down(index)
    
    def peek(self):
        """
        Returns the min value
        """
        return self.heap[0]
    
    def __delete(self, index=0):
        self.heap[index] = float("inf")

    def __sift_down(self, index=0):
        if index > len(self.heap)-1:
            return
        child1 = index*2 + 1
        child2 = index*2 + 2
        if child1 > len(self.heap)-1:
            return
        if child2 > len(self.heap)-1:
            child2 = child1
        while self.heap[child1] < self.heap[index] or self.heap[child2] < self.heap[index]:
            if self.heap[child1] < self.heap[index] and self.heap[child1] < self.heap[child2]:
                self.heap[index], self.heap[child1] = self.heap[child1], self.heap[index]
                index = child1
            else:
                self.heap[index], self.heap[child2] = self.heap[child2], self.heap[index]
                index = child2
            child1 = index*2 + 1
            child2 = index*2 + 2
            if child1 > len(self.heap)-1:
                return
            if child2 > len(self.heap)-1:
                child2 = child1
            
    def __sift_up(self, index=None):
        if index is None:
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
        for index in range(1,len(self.heap)):
            string = f"{string}{self.heap[index]}, "
            nodes += 1
            if nodes >= 2**level:
                level += 1
                nodes = 0
                string = f"{string}\n"
            if index + 2 >= len(self.heap):
                string = f"{string}{self.heap[index+1]}"
                return string
    def __len__(self):
        return len(self.heap)

class MaxHeap(MinHeap):
    def __init__(self, data=None):
        self.heap = []
        if data is not None:
            for node in data:
                self.append(node)

    def append(self, data=0):
        """
        Adds a new value and then adjusts the heap
        """
        self.heap.append(data)
        self.__sift_up()

    def push(self, data=0):
        """
        Replaces the min value and adjusts the heap
        """
        if len(self.heap) < 1:
            return 
        self.heap[0] = data
        self.__sift_down()

    def pop(self):
        """
        Deletes the head value an returns it
        """
        if len(self.heap) < 1:
            return 
        pop = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.__sift_down()
        return pop
    
    def replace(self, index:int, data=0):
        """
        Replaces the value at the given inde xand adjusts the heap
        """
        if len(self.heap) < 1:
            return 
        self.heap[index] = data
        self.__sift_down(index)
        self.__sift_up(index)

    def delete(self, index:int):
        """
        Replaces the value at the given index and adjusts the heap
        """
        if len(self.heap) < 1:
            return 
        self.heap[index] = self.heap.pop()
        self.__sift_down(index)
    
    def peek(self):
        """
        Returns the min value
        """
        return self.heap[0]
    
    def __delete(self, index=0):
        self.heap[index] = float("inf")

    def __sift_down(self, index=0):
        if index > len(self.heap)-1:
            return
        child1 = index*2 + 1
        child2 = index*2 + 2
        if child1 > len(self.heap)-1:
            return
        if child2 > len(self.heap)-1:
            child2 = child1
        while self.heap[child1] > self.heap[index] or self.heap[child2] > self.heap[index]:
            if self.heap[child1] > self.heap[index] and self.heap[child1] > self.heap[child2]:
                self.heap[index], self.heap[child1] = self.heap[child1], self.heap[index]
                index = child1
            else:
                self.heap[index], self.heap[child2] = self.heap[child2], self.heap[index]
                index = child2
            child1 = index*2 + 1
            child2 = index*2 + 2
            if child1 > len(self.heap)-1:
                return
            if child2 > len(self.heap)-1:
                child2 = child1
            
    def __sift_up(self, index=None):
        if index is None:
            index = len(self.heap) - 1
        if index < 1:
            return 
        if index % 2 > 0:
            parent = round((index-1) / 2)
        else:
            parent = int((index-2) / 2)
        while self.heap[index] > self.heap[parent]:
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
        for index in range(1,len(self.heap)):
            string = f"{string}{self.heap[index]}, "
            nodes += 1
            if nodes >= 2**level:
                level += 1
                nodes = 0
                string = f"{string}\n"
            if index + 2 >= len(self.heap):
                string = f"{string}{self.heap[index+1]}"
                return string
    def __len__(self):
        return len(self.heap)
                      