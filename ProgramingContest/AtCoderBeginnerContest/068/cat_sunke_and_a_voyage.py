import heapq

N, M = map(int, input().split())

G = []
for _ in range(N):
    G.append([])

for _ in range(M):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    G[ai].append(bi)
    G[bi].append(ai)

dist = []
for _ in range(N):
    dist.append(-1)

Q = []
heapq.heappush(Q, (0, 0))

dist[0] = 0

done = []
for _ in range(0, N):
    done.append(False)
while len(Q) > 0:
    d, i = heapq.heappop(Q)

    if done[i]:
        continue
    done[i] = True

    for j in G[i]:
        x = 1

        if dist[j] == -1 or dist[j] > dist[i] + x:
            dist[j] = dist[i] + x
            heapq.heappush(Q, (dist[j], j))

if dist[N - 1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
