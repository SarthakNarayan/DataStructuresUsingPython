class Stack:
    def __init__(self):
        self.items = []
    def insert(self,data):
        self.items.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return -1
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

data = '-+8/632'
type_conversion = 'postfix'
operators = '*-+/'
s = Stack()
if type_conversion == 'prefix':
    data = data[::-1]
    
for i in data:
    if i not in operators:
        s.insert(int(i))
    else:
        if i == '*':
            c = s.pop()*s.pop()
        elif i=='+':
            c = s.pop()+s.pop()
        elif i == '-':
            a = s.pop()
            b = s.pop()
            if type_conversion == 'prefix':
                c = a-b
            else:
                c = b-a

        else:
            a = s.pop()
            b = s.pop()
            if type_conversion == 'prefix':
                c = a//b
            else:
                c = b//a
        s.insert(c)

print(s.pop())