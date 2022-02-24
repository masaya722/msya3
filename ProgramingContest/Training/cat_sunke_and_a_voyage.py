import heapq

N, M = map(int, input().split())
G = []
for _ in range(N):
    G.append([])

for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)

dist = []
for _ in range(N):
    dist.append(-1)
dist[0] = 0

done = []
for _ in range(N):
    done.append(False)

Q = []
heapq.heappush(Q, (0, 0))

while len(Q) > 0:
    d, i = heapq.heappop(Q)
    if done[i]:
        continue
    done[i] = True

    X = 1
    for j in G[i]:
        if dist[j] == -1 or dist[j] > dist[i] + X:
            dist[j] = dist[i] + X
            heapq.heappush(Q, (dist[j], j))
if dist[N-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
