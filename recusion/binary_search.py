def binarySearch(li, item, end, start=0):

    if end < start:
        return False
    mid = (end+start)//2

    if li[mid]==item:
        return mid+1
    if li[mid] < item:
        return binarySearch(li, item, end, mid+1)
    if li[mid] > item:
        return binarySearch(li, item, mid-1, start)

li = [1,2,3,4,5,6,7,8,9]
item = 7
pr = binarySearch(li, item, 8)
if pr:
    print('%d found on %d position' %(item, pr))
else:
    print('%d is not found on the list' %(item))
