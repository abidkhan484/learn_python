class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        pass
    
    def create(self, root, item):
        if not root:
            return Node(item)
        curr = root
        while curr:
            if not curr.left:
                curr.left = Node(item)
                break
            if not curr.right:
                curr.right = Node(item)
                break
