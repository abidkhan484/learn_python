def minDistance():
    minim = inf; idx = -1
    for i in range(node):
        if not mySet[i] and dis[i] < minim:
            minim = dis[i]
            idx = i
    return idx

inf = 100001
node, edge = map(int, input().split())
ndVal = [[inf] * node for _ in range(node)]
mySet = [False] * node

for _ in range(edge):
    p, q, r = map(int, input().split())
    p, q = p-1, q-1
    if ndVal[p][q] > r:
        ndVal[p][q] = r
        ndVal[q][p] = r

start = int(input().strip())-1
dis = [inf] * node
dis[start] = 0

for _ in range(node):
    u = minDistance()
    if u == -1:
        break
    mySet[u] = True
    for v in range(node):
        if dis[v] > ndVal[u][v] and not mySet[v]:
            dis[v] = ndVal[u][v]

print(sum(dis))


'''input
5 7
1 2 20
1 3 50
1 4 70
1 5 90
2 3 30
3 4 40
4 5 60
2

150

4 6
2 1 1000
3 4 299
2 4 200
2 4 100
3 2 300
3 2 6
2

1106

5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1

15
'''
