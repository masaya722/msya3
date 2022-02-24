N, M = map(int,input().split())
A = []
for _ in range(N):
    A.append(input())
group = []
for i in range(11):
    group.append([])
for i in range(N):
    for j in range(M):
        if A[i][j] == 'S':
            n = 0
        elif A[i][j] == 'G':
            n = 10
        else:
            n = int(A[i][j])
        group[n].append((i, j))

cost = []
INF = 10 ** 20
for i in range(N):
    cost.append([INF] * M)
sy, sx = group[0][0]
cost[sy][sx] = 0

for n in range(1, 11):
    for i1, j1 in group[n]:
        for i2, j2 in group[n - 1]:
            cost[i1][j1] = min(cost[i1][j1], cost[i2][j2] + abs(i1 - i2) + abs(j1 - j2))

gy, gx = group[10][0]
ans = cost[gy][gx]
if ans == INF:
    ans = -1
print(ans)
