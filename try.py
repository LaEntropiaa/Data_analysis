class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
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
            return current_node.data
        except AttributeError:
            return None

    def show_values(self):
        current_node = self.head
        print("[", end="")
        while True:
            print(f"{current_node.data} -> ", end="")
            current_node = current_node.next
            if current_node.next is None:
                print(f"{current_node.data} -> ", end="")
                break
        print("None]")

lista = LinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
print(lista.get(-1))

