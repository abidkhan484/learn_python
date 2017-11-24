n, k = 5, 9
ar = [3, 4, 4, 4, 8]

arr = [[0]*k for _ in range(n)]

# this loop will generate the first row of the 2d array
p = ar[0]
for i in range(k):
    if i-p+1 >= 0:
        arr[0][i] = arr[0][i-p] + p

for i in range(1, n):
    p = ar[i]
    for j in range(k):
        tmp = 0
        if j-p+1 >= 0:
            tmp = arr[i][j-p] + p

        if tmp > arr[i-1][j]:
            arr[i][j] = tmp
        else:
            arr[i][j] = arr[i-1][j]

print(arr[-1][-1])

