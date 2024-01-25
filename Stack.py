class Stack:
    def __init__(self, data=[]) -> None:
        self.stack = data

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self)-1]
    
    def __iter__(self):
        self.current_index = len(self.stack)
        return self
    
    def __next__(self):
        if self.current_index > 0:
            self.current_index -= 1
            return self.stack[self.current_index]
        else:
            raise StopIteration
    
    def __len__(self):
        return len(self.stack)
    
    def __str__(self) -> str:
            return str(object=self.stack)