m, n = list(map(int, input().split()))

li = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
    sp = list(map(int, input().split()))
    li[sp[0]-1][sp[1]-1] = sp[2]
    li[sp[1]-1][sp[0]-1] = sp[2]


for i in range(m):
    for j in range(n):
        print(li[i][j], end=' ')
    print()
