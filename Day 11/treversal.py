class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def preOrder(root):
    if root != None:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")

root = Node(10)
root.left = Node(6)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(9)
root.right.left = Node(8)
preOrder(root)
inOrder(root)
postOrder(root )
