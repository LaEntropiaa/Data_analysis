class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data:list=None):
        self.head = None
        self.index = 0
        if data is not None:
            for node in data:
                self.append(node)
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def pre_append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert(self, data, index):
        new_node = Node(data)
        current_node = self.head
        current_index = 0
        while index != current_index:
            current_node = current_node.next
            current_index += 1
        next_node = current_node.next
        current_node.next = new_node
        new_node.next = next_node

    def get(self, index):
        current_node = self.head
        current_index = 0
        while index != current_index:
            try:
                current_node = current_node.next
            except AttributeError:
                return None
            current_index += 1
        try:
            return current_node
        except AttributeError:
            return None
    
    def pop(self):
        last_node = self.head.next.next
        pre_node = self.head
        while last_node is not None:
            pre_node = pre_node.next
            last_node = last_node.next
        last_node = pre_node.next
        pre_node.next = None
        return last_node.data

    def __len__(self):
        length = 1
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            length += 1
        return length

    def __str__(self):
        current_node = self.head
        string = "["
        while True:
            string = f"{string} {current_node.data} ->"
            current_node = current_node.next
            if current_node.next is None:
                string = f"{string} {current_node.data} ->"
                break
        string = f"{string} None]"
        return string
    
    def __getitem__(self, index):
        current_node = self.head
        current_index = 0
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

        if self.index < len(self):
            data = self[self.index]
            self.index += 1
            return data
        else:
            self.index = 0
            raise StopIteration
    
    def __delitem__(self, index):
        self.get(index-1).next = self.get(index+1)
    
    def __setitem__(self, index, data):
        new_node = Node(data)
        new_node.next = self.get(index+1)
        self.get(index-1).next = new_node

mylist = LinkedList([1,2,3,4,5,6])
print(mylist.pop(), "\n", mylist)



