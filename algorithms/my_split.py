def try_split(string):
    li = []
    temp = ''

    l = len(string)

    for i in range(l):
        if (string[i-1]==' ') and (string[i]!=' '):
            temp += string[i]
        elif (string[i]==' ') and (temp != ''):
            li.append(temp)
            temp = ''
        elif string[i]!=' ':
            temp += string[i]
    if temp!= '':
        li.append(temp)

    return li

n = input()
a = try_split(n)
for i in a:
    print(i, end=' ')
