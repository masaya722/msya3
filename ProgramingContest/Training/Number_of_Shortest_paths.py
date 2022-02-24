from collections import deque

MOD = 10**9+7
N,M = map(int,input().split())
cities = [[]for _ in range(N)]
for _ in range(M):
    a,b =map(int,input().split())
    a -=1
    b -=1
    cities[a].append(b)
    cities[b].append(a)

dist = [-1 for _ in range(N)]
dist[0] = 1
count = [0 for _ in range(N)]
count[0] = 1
Q = deque()
Q.append(0)
while Q:
    st = Q.popleft()
    for i in cities[st]:
        if dist[i] == -1:
            dist[i] = dist[st]+1
            count[i] += count[st]
            Q.append(i)
        elif dist[i] == dist[st]+1:
            count[i] +=count[st]
print(count[N-1]%MOD)