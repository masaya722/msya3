import heapq

N, M = map(int, input().split())
G = []
for _ in range(N):
    G.append([])
for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))
    G[v].append((u, c))

marked = []
for _ in range(N):
    marked.append(False)
marked_count = 0

marked[0] = True
marked_count += 1

Q = []

for v, c in G[0]:
    heapq.heappush(Q, (c, v))

sum = 0

while marked_count < N:
    c, i = heapq.heappop(Q)
    if marked[i]:
        continue
    marked[i] = True
    marked_count += 1
    sum += c
    for (v, c) in G[i]:
        if marked[v]:
            continue
        heapq.heappush(Q, (c, v))

print(sum)