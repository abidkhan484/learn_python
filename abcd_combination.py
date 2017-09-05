n = 'abcdefghijklmnopqrstuvwxyz'

li = list(n); mylist = []
i = 1; p = len(li)
while i <= len(li):
    for j in range(p):
        tmp = ''
        for x in range(j, i+j):
            tmp += li[x]
        mylist.append(tmp)
    p -= 1; i += 1

print(len(mylist))
