class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

# Depth level traversal
    def pre_order(self,start,traversal):
        """root -> left -> right"""
        if start:
            traversal += (str(start.data) + "->")
            traversal = self.pre_order(start.left,traversal)
            traversal = self.pre_order(start.right,traversal)
        return traversal

    def in_order(self,start,traversal):
        """ left -> root -> right"""
        if start:
            traversal = self.in_order(start.left,traversal)
            traversal += (str(start.data) + "->")
            traversal = self.in_order(start.right,traversal)
        return traversal

    def post_order(self,start,traversal):
        """ left -> right -> root """
        if start:
            traversal = self.post_order(start.left,traversal)
            traversal = self.post_order(start.right,traversal)
            traversal += (str(start.data) + "->")
        return traversal

# Level order traversal we use queue

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.pre_order(tree.root,""))
print(tree.in_order(tree.root,""))
print(tree.post_order(tree.root,""))

        