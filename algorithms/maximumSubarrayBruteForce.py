# problem: 4.1-2
# introduction to algorithms (see also page 70)


mylist = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

length = len(mylist)
maxim = -10000007
start=0; end=0

for i in range(length):
    j = i; summation = 0
    while j<length:
        summation += mylist[j]
        if summation > maxim:
            start = i+1 #as this is 0 indexed
            end = j+1 #as this is 0 indexed
            maxim = summation
        
        j += 1

print(maxim, start, end)
