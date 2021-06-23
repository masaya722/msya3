INF = 1_000_000_000_000_000_000

N, M = map(int, input().split())
dist = []

for i in range(0, N):
    dist.append([])
    for j in range(0, N):
        dist[i].append(INF)

for _ in range(0, M):
    u, v, c = map(int, input().split())
    dist[u][v] = c

for i in range(0,N):
    dist[i][i] = 0

for k in range(0, N):
    for x in range(0, N):
        for y in range(0, N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

ans = 0
for i in range(0, N):
    for j in range(0, N):
        ans += dist[i][j]

print(ans)
