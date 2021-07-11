from collections import deque

N,M = map(int,input().split())

edges = [[]for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a -=1
    b -=1
    edges[a].append(b)
    edges[b].append(a)


Q = deque()

for i in range(N):
    dist = [-1 for _ in range(N)]
    dist[i] = 0
    Q.append(i)
    while Q:
        x = Q.popleft()
        for j in edges[x]:
            if dist[j] != -1:
                continue
            dist[j] = dist[x]+1
            Q.append(j)
    print(dist.count(2)) 