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
        new_node = data
        new_node.next = self.head
        self.head = new_node
    
    def insert(data, index):
        new_node = data
        

    def show_values(self):
        current_node = self.head
        print("[", end="")
        while current_node.next:
            print(f"{current_node.data} -> ", end="")
            current_node = current_node.next
        print("None]")

lista = LinkedList()
lista.append(1)
lista.append(2)
lista.show_values()

