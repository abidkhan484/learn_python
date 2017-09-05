def sequence(seq, st, length1, length2, res=[]):

    if not seq[length2][length1]:
        return res
    if seq[length2][length1]=='\\':
        res.append(st[length1-1])
        return sequence(seq, st, length1-1, length2-1, res)
    if seq[length2][length1]=='u':
        return sequence(seq, st, length1, length2-1, res)
    return sequence(seq, st, length1-1, length2, res)


def lcs(st, st2):
    length1 = len(st)+1
    length2 = len(st2)+1

    mylist = [[0 for j in range(length1)] for i in range(length2)]
    seq = [[0 for j in range(length1)] for i in range(length2)]
    
    for i in range(1, length2):
        for j in range(1, length1):
            # if position of string1 is equal to string2 position
            # mylist adds 1
            if st[j-1] == st2[i-1]:
                seq[i][j] = '\\'
                mylist[i][j] = mylist[i-1][j-1] + 1
                
            else:
                if mylist[i][j-1] > mylist[i-1][j]:
                    seq[i][j] = 'l'
                    mylist[i][j] = mylist[i][j-1]
                else:
                    seq[i][j] = 'u'
                    mylist[i][j] = mylist[i-1][j]


    res = sequence(seq, st, length1-1, length2-1)
    res.reverse()
    
    '''
    res = []
    length1 -= 1; length2 -= 1
    
    while seq[length2][length1]:
        if seq[length2][length1]=='\\':
            length1 -= 1; length2 -= 1
            res.append(st[length1])
        elif seq[length2][length1] == 'u':
            length2 -= 1
        else:
            length1 -= 1

    res.reverse()

###############################################################
    # this loop is for print all the element; try this
    
    length2 -= 2; i = length2
    while length1:
        length2 = i
        while length2:
            print(mylist[length1][length2], end=' ')
            length2 -= 1
        print()
        length1 -= 1
    '''
    
    return mylist[-1][-1], ''.join(res)

s = 'python' #input().strip()
st = 'panther' #input().strip()
length, seq = lcs(s, st)
print('here the strings are \'%s\' and \'%s\'.' %(s, st))
print('the required LCS is %d\nand the sequence is \'%s\'' %(length, seq))
