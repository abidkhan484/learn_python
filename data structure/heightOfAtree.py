class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if not root:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(height(root))
