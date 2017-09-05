def merge_two_list(li, li2):

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
    mid = len(li)-1; start = 0
    li = li + li2
    end = len(li)-1
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
    #print(tmp)
    
    if p==(p or r):
        tmp.extend(li[start:b])
        return li[:a] + tmp + li[(c+1):]
    else:
        tmp.extend(li[mid:(c+1)])
        return li[:a] + tmp + li[(c+1):]
'''    

def merge_sort(li):

    left, right = [], []
    p = len(li)
    if p > 1:
        left = merge_sort(li[:p//2])
        right = merge_sort(li[p//2:])
        li = merge_two_list(left, right)

    return li


pr = [5, 8, 1, 3, 7, 9, 2]
print(*merge_sort(pr))

#here the code is inefficient, i just know but i'm happy.
#because i just implement it myself and
#try to go beneath the recursion......... :) :)
