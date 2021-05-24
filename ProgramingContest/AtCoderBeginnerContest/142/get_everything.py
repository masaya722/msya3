N, M = map(int, input().split())
key = []
c = []
for _ in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    pick = 0
    for c in C:
        pick += 1 << c - 1
    key.append((a, pick))

ALL = 1 << N
cost = []
inf = 10 ** 10
for i in range(M + 1):
    cost.append([inf] * ALL)

cost[0][0] = 0

for i in range(1, M + 1):
    c, p = key[i-1]
    for j in range(ALL):
        cost[i][j] = min(cost[i][j], cost[i - 1][j])
        cost[i][j | p] = min(cost[i][j | p], cost[i - 1][j] + c)

ans = cost[M][ALL - 1]
if ans == inf:
    ans = -1
print(ans)
