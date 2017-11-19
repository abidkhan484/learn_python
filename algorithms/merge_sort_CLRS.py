def mergeList(li, start, mid, end):

    p = mid-start+1
    r = end-mid

    left = [0] * p
    right = [0] * r

    j = start
    for i in range(p):
        left[i] = li[j]
        j += 1
    j = mid+1
    for i in range(r):
        right[i] = li[j]
        j += 1

    k = start; i = 0; j = 0
    while (i < p) and (j < r):
        if left[i] < right[j]:
            li[k] = left[i]
            i += 1
        else:
            li[k] = right[j]
            j += 1
        k += 1

    while i < p:
        li[k] = left[i]
        i += 1; k += 1
    while j < r:
        li[k] = right[j]
        j += 1; k += 1


def merge_sort(li, start, end):

    if end > start:
        mid = (start+end)//2

        merge_sort(li, start, mid)
        merge_sort(li, mid+1, end)
        mergeList(li, start, mid, end)


li = [12, 11, 13, 5, 6, 7]
print('unsorted list', *li)
merge_sort(li, 0, 5)
print('sorted', *li)

'''
# the problem is not solved yet
# i just learnt something from these mistakes

# list contains reference but it works only when we reinitialize this or
# append and such kind of operation. if we slice the list, this will be
# treat as the local variable.


def merge_list(li, start, mid, end):

    tmp = []
    a, b, c = start, mid, end
    p, r = (mid-start+1), (end-mid)

    left = [0] * p
    right = [0] * r

    mid += 1; j = 0
    for i in range(start, mid):
        left[j] = li[i]
        j += 1
    j = 0
    for i in range(mid, end+1):
        right[j] = li[i]
        j += 1


    print(a,b,c, left, right, p, r, start, mid)
    j = start; l, s = 0, 0
    while p and r:
        if left[l] < right[s]:
            li[j] = left[l]
            p -= 1
            l += 1
        else:
            li[j] = right[s]
            print(li)
            r -= 1
            s += 1
        j += 1

    #print('tmp', tmp, start, b, c,'pr', p, r, 'mid', mid)
    if p==(p or r):
        tmp.extend(li[start:(b+1)])
        li = li[:a] + tmp + li[(c+1):]
        print(li)
        return
    else:
        tmp.extend(li[mid:(c+1)])
        li = li[:a] + tmp + li[(c+1):]
        print(li)
        return

merge_list([2,1], 0, 0, 1)

def merge_sort(li, start, end):

    if end > start:
        mid = (start+(end-1))//2

        merge_sort(li, start, mid)
        merge_sort(li, mid+1, end)
        #print(start, mid, end, li)
        merge_list(li, start, mid, end)

    #return li

li = [12, 11, 13, 5, 6, 7]
#li = merge_list(mylist, 4, 5, 7)
#print(*li)
#merge_sort(li, 0, 5)
#print(*li)


    li = mylist[start:mid+1]; li2 = mylist[mid:end+1]
    tmp, i, j = [], 0, 0
    a, b = len(li), len(li2)
    
    while (a > i) and (b > j):
        if li[i] > li2[j]:
            tmp.append(li2[j])
            j += 1
        else:
            tmp.append(li[i])
            i += 1

    if i==a:
        tmp.extend(li2[j:])
    else:
        tmp.extend(li[i:])
        
    return tmp
'''
