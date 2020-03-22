class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class LinkedList():
    def __init__(self):
        self.head = None
    
    def display(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def add_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            traversing = self.head
            while traversing.next is not None:
                traversing = traversing.next
            traversing.next = new_node
            new_node = None

    def add_beg(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def add_after(self,data_after,data):
        new_node = Node(data)
        found = False
        cur_pos = self.head
        while cur_pos is not None:
            if cur_pos.data == data_after:
                found = True
                break
            cur_pos = cur_pos.next
        if found:
            new_node.next = cur_pos.next
            cur_pos.next = new_node
        else:
            print("Data not found")

    def delete_node(self,data):
        cur_node = self.head
        if cur_node.data == data:
            self.head = self.head.next
            cur_node.next = None
        else:
            prev_node = self.head
            cur_node = prev_node.next
            while cur_node is not None:
                if cur_node.data == data:
                    prev_node.next = cur_node.next
                    cur_node.next = None
                prev_node = prev_node.next
                cur_node = cur_node.next



l = LinkedList()
l.add_end(1)
l.add_end(2)
l.add_beg(3)
l.add_after(2,4)
l.display()
l.delete_node(3)
print()
l.display()