char = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]
print('input char and frequencies are:')
print('char:', *char)
print('frequency:', *freq)

class Node:

    def __init__(self, data, char=None):
        self.data = data
        self.char = char
        self.head = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def __lt__(self, other):
        return self.data < other.data

    def __add__(self, other):
        return self.data + other.data

def push(data):
    heap.append(data)
    length = len(heap)-1
    
    while length:
        par = (length-1)>>1
        if heap[par] > data:
            heap[length] = heap[par]
            length = par
            continue
        break
    heap[length] = data

def _siftdown(pos):
    length = len(heap)
    item = heap[pos]
    leftchild = (2*pos)+1
    while leftchild < length:
        rightchild = leftchild + 1
        if rightchild < length and heap[leftchild] > heap[rightchild]:
            leftchild = rightchild
        if item.data < heap[leftchild].data:
            break
        heap[pos] = heap[leftchild]
        pos = leftchild
        leftchild = (2*pos) + 1
    heap[pos] = item

def pop():
    length = len(heap)-1
    if not length:
        return heap.pop()
    heap[0], heap[length] = heap[length], heap[0]
    item = heap.pop()
    _siftdown(0)
    return item


heap = []
for i in range(len(freq)):
    push(Node(freq[i], char[i]))

while len(heap) > 1:

    first = pop()
    second = pop()
    addition = first + second

    node = Node(addition)
    node.left = first
    node.right = second

    first.head = node
    second.head = node    
    push(node)


tree = heap[0]
def traverse(tree, li, st=''):

    if not tree.left:
        # this check confirms there is no left child of the tree
        # as there is no left child; there is no right child
        print(tree.char+':', st)
        li.append([st, tree.char])

    if tree.right:
        traverse(tree.right, li, st+'1')
    if tree.left:
        traverse(tree.left, li, st+'0')

    return li

print('\n\nand the outputs are:')
li = []
li = traverse(tree, li)
