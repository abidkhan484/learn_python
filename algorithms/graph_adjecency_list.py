class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class adj_list:

    def __init__(self):
        self.my_list = []
        self.counter = 0

    def check_item(self, item, i=0):
            if (i==len(self.my_list)) or (self.my_list[i]==None):
                    return 'lol'
            elif self.my_list[i].data != item:
                    return self.check_item(item, i+1)
            return i


    def make_linked(self, item, next_item):
        
        index = adj_list.check_item(self, item)
        if index=='lol':
            self.my_list[self.counter] = Node(item)
            self.my_list[self.counter].next = Node(next_item)
            self.counter += 1

        else:
            data = self.my_list[index]
            while data.next:
                data = data.next
            data.next = Node(next_item)
        
        return

    def make_list(self, node):
        self.my_list = node*[None]
        return self.my_list

adj = adj_list()

node, edge = input().split()
node, edge = int(node), int(edge)

adj.make_list(node)

for _ in range(edge):
    m, n = input().split()
    m, n = int(m), int(n)

    if m==n:
        adj.make_linked(m, n)
        continue
    adj.make_linked(m, n)
    adj.make_linked(n, m)

for i in range(len(adj.my_list)):
	curr = adj.my_list[i]
	print(curr.data, '-'*4+'>', end= ' ')
	curr = curr.next
	while curr:
		print(curr.data, end=',')
		curr = curr.next
	print()

'''
input:
6 8
1 2
1 4
2 4
2 5
4 5
5 3
3 6
6 6

output:
1 ----> 2,4,
2 ----> 1,4,5,
4 ----> 1,2,5,
5 ----> 2,4,3,
3 ----> 5,6,
6 ----> 3,6,
'''
