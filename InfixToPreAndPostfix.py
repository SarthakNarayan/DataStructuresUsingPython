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
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

data = "(L-K/A) * (C/B - A)"
operators = '*-+/^'
expression = ""
precedence = {'(':0,'+':1, '-':1, '*':2, '/':2, '^':3} 
s = Stack()
for i in data:
    if i == '(':
        s.insert(i)
    elif i == ')':
        while(s.peek() != '('):
            expression += str(s.pop())
        s.pop()
    elif i not in operators:
        expression += i
    elif i in operators:
        if s.isEmpty():
            s.insert(i)
        elif precedence[i] > precedence[s.peek()]:
            s.insert(i)
        else:
            while(s.peek() != '(' or (precedence[i] < precedence[s.peek()])):
                if s.isEmpty():
                    break
                expression += str(s.pop())
            s.insert(i)
    else:
        pass
while not s.isEmpty():
    expression += s.pop()
print(expression)
            