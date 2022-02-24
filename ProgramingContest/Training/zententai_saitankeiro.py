INF = 10 ** 18

N, M = map(int, input().split())

dist = []

for i in range(N):
    dist.append([])
    for j in range(N):
        dist[i].append(INF)

for _ in range(M):
    u, v, c = list(map(int, input().split()))
    dist[u][v] = c

for i in range(N):
    dist[i][i] = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            dist[j][k] = min(dist[j][k],dist[j][i]+dist[i][k])

ans = 0
for i in range(N):
    for j in range(N):
        ans += dist[i][j]
print(ans)