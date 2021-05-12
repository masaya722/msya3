import heapq

N, M = map(int, input().split())

G = []
for _ in range(0, N):
    G.append([])

for _ in range(0, M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))

dist = []
for _ in range(0, N):
    dist.append(-1)

Q = []
heapq.heappush(Q, (0, 0))
dist[0] = 0

done = []
for _ in range(0, N):
    done.append(False)

while len(Q):
    d, i = heapq.heappop(Q)
    if done[i]:
        continue
    done[i] = True

    for (j, c) in G[i]:
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, (dist[j], j))
print(dist[N - 1])
