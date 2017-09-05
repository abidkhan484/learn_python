mylist = []

def enqueue(item):
    return mylist.append(item)

def dequeue():
    return mylist[1:]

def print_item():
    return mylist[0]

n = int(input().strip())
for _ in range(n):
    tmp = input().split()
    if tmp[0]=='1':
        enqueue(int(tmp[1]))
    elif tmp[0]=='2':
        mylist = dequeue()
    else:
        print(print_item())
