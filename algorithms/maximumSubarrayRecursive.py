def get_maximum(mylist, end, start=0, summation=0, maxim=-10000007, i=-1, j=-1):

    if start < end:
        mid = (start+end)//2
        get_maximum(mylist, mid, start, summation, maxim, i, j)
        var1 = 0
        for i in range(start, mid+1):
            var1 += mylist[i]
        print(var1, start, mid)
        get_maximum(mylist, end, mid+1, summation, maxim, i, j)
        var2 = 0
        for i in range(mid+1, end):
            var2 += mylist[i]

        print(var2, mid+1, end)
        summation = (var1+var2)
        if summation > maxim:
            maxim = summation
            i = start; j = end

    return summation


mylist = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
res = get_maximum(mylist, 15)
