class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data:list=None):
        self.__head = None
        self.__index = 0
        if data is not None:
            for node in data:
                self.append(node)
    
    def append(self, data):
        """
        Appends a new node to the last node
        """
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
            return
        last_node = self.__head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def pre_append(self, data):
        """
        Replaces the __head by a new node
        """
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node
    
    def insert(self, data, index:int):
        """
        Inserts a new node between the node at the given index and the next one
        """
        new_node = Node(data)
        current_node = self.__head
        current_index = 0
        if index < 0:
            raise IndexError("Index out of range")
        while index != current_index:
            current_node = current_node.next
            current_index += 1
        try:
            next_node = current_node.next
        except AttributeError:
            raise IndexError("Index out of range")
        current_node.next = new_node
        new_node.next = next_node

    def get(self, index:int):
        """
        Returns the Node object instead of it's data at the given index
        """
        current_node = self.__head
        current_index = 0
        if index < 0:
            raise IndexError("Index out of range")
        while index != current_index:
            try:
                current_node = current_node.next
            except AttributeError:
                raise IndexError("Index out of range")
            current_index += 1
        try:
            return current_node
        except AttributeError:
            return IndexError("Index out of range")
    
    def pop(self):
        """
        Deletes the last node and returs it's data 
        """
        last_node = self.__head.next.next
        pre_node = self.__head
        while last_node is not None:
            pre_node = pre_node.next
            last_node = last_node.next
        last_node = pre_node.next
        pre_node.next = None
        return last_node.data
    
    def extend(self, list2):
        """
        Concatenates another linked list to the first one
        """
        if isinstance(list2, LinkedList):
            last_node = self.__head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = list2.__head
        elif isinstance(list2, list):
            for node in list2:
                self.append(node)
        else:
            raise ValueError(f"value type {type(list2)} is not valid")

    def count(self, data):
        """
        Returns the ocurrences of a given value
        """
        count = 0
        current_node = self.__head
        while current_node.next is not None:
            if current_node.data == data:
                count += 1
            current_node = current_node.next
        if current_node.data == data:
                count += 1
        return count
    
    def remove(self, data):
        """
        Removes the first occurence of a value
        """
        current_node = self.__head.next
        before_node = self.__head
        if before_node.data == data:
            self.__head = current_node
        while current_node.next is not None:
            if current_node.data == data:
                before_node.next = current_node.next
                return
            before_node = current_node
            current_node = current_node.next
        if current_node.data == data:
            before_node.next = current_node.next
            return
        raise ValueError("Value not in llist")
    
    def reverse(self):
        prev_node = None
        current_node = self.__head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.__head = prev_node

    def index(self, data):
        current_node = self.__head
        current_index = 0
        while current_node is not None:
            if current_node.data == data:
                return current_index
            current_node = current_node.next
            current_index += 1
        raise ValueError(f"{data} not in llist")
    
    def clear(self):
        self.__head = None
        
    def __len__(self):
        length = 1
        current_node = self.__head
        while current_node.next is not None:
            current_node = current_node.next
            length += 1
        return length

    def __str__(self):
        current_node = self.__head
        string = "["
        if current_node is None:
            return "[]"
        while True:
            string = f"{string} {current_node.data} ->"
            current_node = current_node.next
            if current_node is None:
                break
            if current_node.next is None:
                string = f"{string} {current_node.data} ->"
                break
        string = f"{string} None ]"
        return string
    
    def __getitem__(self, index):
        current_node = self.__head
        current_index = 0
        if index < 0:
            raise IndexError("Negative index is not suported")
        while index != current_index:
            try:
                current_node = current_node.next
            except AttributeError:
                raise IndexError("Index out of range")
            current_index += 1
        try:
            return current_node.data
        except AttributeError:
            raise IndexError("Index out of range")

    def __iter__(self):
        return self
     
    def __next__(self):

        if self.__index < len(self):
            data = self[self.__index]
            self.__index += 1
            return data
        else:
            self.__index = 0
            raise StopIteration
    
    def __delitem__(self, index):
        if index < 0:
            raise IndexError("Negative index is not suported")
        try:
            self.get(index-1).next = self.get(index+1)
        except AttributeError:
            raise IndexError("Index out of range")

    def __setitem__(self, index, data):
        if index < 0:
            raise IndexError("Negative index is not suported")
        self.get(index).data = data 
        


def main():
    print("Hi")

if __name__ == "__main__":
    main()