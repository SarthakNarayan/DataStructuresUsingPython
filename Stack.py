# Stack class with operations

class Stack():
    def __init__(self):
        # this function is run when the class is initialized
        # so when you create a class items list is created
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def get_stack(self):
        return self.items
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

s = Stack()
print(s.is_empty())
print(s.peek())
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.is_empty())
print(s.peek())