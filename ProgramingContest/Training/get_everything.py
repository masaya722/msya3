N, M = map(int, input().split())
key = []
for _ in range(M):
    a, b = map(int, input().split())
    treasureList = list(map(int, input().split()))
    pick = 0
    for treasure in treasureList:
        pick += 1 << treasure - 1
    key.append((a, pick))

ALL = 1 << N

cost = []
INF = 10 ** 20
for _ in range(M + 1):
    cost.append([INF] * ALL)
cost[0][0] = 0

for i in range(1, M + 1):
    c, p = key[i - 1]
    for j in range(ALL):
        cost[i][j] = min(cost[i][j], cost[i - 1][j])
        cost[i][j | p] = min(cost[i][j | p], cost[i - 1][j] + c)

ans = cost[M][ALL - 1]
if ans == INF:
    ans = -1
print(ans)
