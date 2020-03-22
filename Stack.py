# Stack class with operations

class Stack():
    def __init__(self):
        # this function is run when the class is initialized
        # so when you create a class items list is created
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
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


# Checking balanced parenthesis
def checker(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False

def check_balanced_paranthesis(parenthesis):
    st = Stack()
    Balanced = True
    for i in parenthesis:
        if i in '{[(':
            st.push(i)
        else:
            if st.is_empty():
                Balanced = False
                break
            else:
                top = st.pop()
                Balanced = checker(top,i)
                if not Balanced:
                    break

    if Balanced and st.is_empty():
        return True
    else:
        return False

print(check_balanced_paranthesis('()({})'))