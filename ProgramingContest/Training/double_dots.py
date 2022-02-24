from collections import deque

INF = 10**6
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

Q = deque()
dist = [INF]*N
prev = [-1]*N
dist[0] = 0
Q.append(0)
while Q:
    i= Q.popleft()
    for j in edge[i]:
        if dist[j] ==INF:
            dist[j] = dist[i]+1
            prev[j] = i
            Q.append(j)
if INF in dist:
    print("No")
else:
    print("Yes")
    for i in range(1,N):
        print(prev[i]+1)
