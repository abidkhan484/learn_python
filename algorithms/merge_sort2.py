def merge_list(mylist, start, mid, end):

    tmp = []
    a, b, c = start, mid, end
    p, r = (mid-start), (end-mid+1)
    #print(a,b,c,p,r)
    while p and r:
        if li[start] < li[mid]:
            tmp.append(li[start])
            p -= 1
            start += 1
        else:
            tmp.append(li[mid])
            r -= 1
            mid += 1

    if p==(p or r):
        tmp.extend(li[start:b])
        return li[:a] + tmp + li[(c+1):]
    else:
        tmp.extend(li[mid:(c+1)])
        return li[:a] + tmp + li[(c+1):]

'''
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


mylist = [2,1,3,2,4,5]
li = merge_list(mylist, 0,1,2)
#print(li)

def merge_sort(li, start, end):

    if end>start:
        mid = (start+end)//2
        merge_sort(li, start, mid)
        print(li, start, mid, end)
        merge_sort(li, mid+1, end)
        print(li, start, mid, end)
        li = merge_list(li, start, mid, end)
        #print(li)

    return li

print(*merge_sort([6,5,3,1,8,7,2,4], 0, 7))
