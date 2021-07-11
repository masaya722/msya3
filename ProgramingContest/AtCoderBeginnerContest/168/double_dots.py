from collections import deque

INF = 10**6
N,M = map(int,input().split())
to = [[]for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a -=1
    b -=1
    to[a].append(b)
    to[b].append(a)

Q = deque()
Q.append(0)
dist = [INF]*N
dist[0] = 0
prev = [-1]*N
while Q:
    i = Q.popleft()
    for j in to[i]:
        if dist[j] != INF:
            continue
        dist[j] =dist[i]+1
        prev[j] = i
        Q.append(j)
if INF in dist:
    print("No")
else:
    print("Yes")
    for i in range(1,N):
        print(prev[i]+1)
