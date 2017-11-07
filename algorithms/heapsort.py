def add(p):
    mylist.append(p)
    length = len(mylist)-1
    # this part of the code just organise the element
    # according to the algorithm (bottom to top)
    while length:
        par = (length-1)>>1
        if mylist[par] < p:
            mylist[length] = mylist[par]
            length = par
            continue
        break
    mylist[length] = p


def move_to_down(end):
    # this one Down the element
    item = mylist[0]
    i = 0
    childpos = (2*i)+1
    while childpos < end:
        rightpos = childpos + 1
        if (rightpos < end) and (mylist[childpos] < mylist[rightpos]):
            childpos = rightpos
        if mylist[childpos] < mylist[i]:
            mylist[i] = item
            return
        mylist[i] = mylist[childpos]
        i = childpos
        childpos = (2*i)+1
    mylist[i] = item


def heapSort(mylist):
    length = len(mylist)
    while length != 1:
        mylist[0], mylist[length-1] = mylist[length-1], mylist[0]
        length -= 1
        move_to_down(length)


mylist = []

add(1);add(2);add(9);add(7);add(5)
print('building max-heap', *mylist)

heapSort(mylist)
print('after sorting', *mylist)
