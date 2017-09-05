class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
            

class BinarySearchTree:

    def __init__(self):
        pass

    def create(self, root, item):
        if not root:
            return Node(item)
        curr = root
        while curr:
            if curr.data > item:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(item)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(item)
                    break

        return root

    def preOrder(self, root):
        if root:
            print(root.data, end=' ')
            BinarySearchTree.preOrder(self, root.left)
            BinarySearchTree.preOrder(self, root.right)

    def postOrder(self, root):
        if root:
            BinarySearchTree.postOrder(self, root.left)
            BinarySearchTree.postOrder(self, root.right)
            print(root.data, end=' ')

    def inOrder(self, root):
        if root:
            BinarySearchTree.inOrder(self, root.left)
            print(root.data, end=' ')
            BinarySearchTree.inOrder(self, root.right)

    # this levelOrder function is not correct. solve it.
    def levelOrder(self, root):
        if root:
            if root.left:
                print(root.data, end=' ')
                BinarySearchTree.levelOrder(self, root.left)
                BinarySearchTree.levelOrder(self, root.right)
            if root.right:
                print(root.data, end=' ')
                BinarySearchTree.levelOrder(self, root.left)
                BinarySearchTree.levelOrder(self, root.right)


    def height(self, root):
        if not root:
            return -1
        return 1 + max(BinarySearchTree.height(self, root.left), BinarySearchTree.height(self, root.right))

bt = BinarySearchTree()
root = None
'''
root = bt.create(root, 3)
root = bt.create(root, 2)
root = bt.create(root, 5)
root = bt.create(root, 1)
root = bt.create(root, 6)
root = bt.create(root, 4)
root = bt.create(root, 7)
root = bt.create(root, 8)
'''
root = bt.create(root, 1)
root = bt.create(root, 2)
root = bt.create(root, 5)
root = bt.create(root, 3)
root = bt.create(root, 6)
root = bt.create(root, 4)
print('levelorder traversing: ', end=' '); bt.levelOrder(root)
print()
print('preorder traversing: ', end=' '); bt.preOrder(root)
print()
print('postorder traversing: ', end=' '); bt.postOrder(root)
print()
print('inorder traversing: ', end=' '); bt.inOrder(root)

# print(bt.height(root))

