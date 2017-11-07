def add(p):
    mylist.append(p)
    length = len(mylist)-1
    # this part of the code just organise the element
    # according to the algorithm (bottom to top)
    while length:
        par = (length-1)>>1
        if mylist[par] > p:
            mylist[length] = mylist[par]
            length = par
            continue
        break
    mylist[length] = p


def move_to_top(pagli):
    # this loop moves the element to the Top
    i = pagli
    while pagli:
        par = (i-1)//2
        if mylist[par] > mylist[pagli]:
            mylist[pagli], mylist[par] = mylist[par], mylist[pagli]
            pagli = par
        else:
            break

def move_to_down(i):
    # this one Down the element
    length = len(mylist)
    item = mylist[i]
    childpos = (2*i)+1
    while childpos < length:
        rightpos = childpos + 1
        if rightpos < length and not mylist[childpos] < mylist[rightpos]:
            childpos = rightpos
        mylist[i] = mylist[childpos]
        i = childpos
        childpos = (2*i)+1
    mylist[i] = item


def delete(p):
    length = len(mylist)
    for i in range(length-1):
        if mylist[i]==p:
            mylist[i], mylist[-1] = mylist[-1], mylist[i]
            mylist.pop()
            break
    else:
        mylist.pop()
        return


    move_to_down(i)
    move_to_top(i)


def printMin():
    print(mylist[0])


mylist = []; items = set()

add(234);add(252);add(273);add(492); add(85)
print(mylist)
delete(234)
print(mylist)
